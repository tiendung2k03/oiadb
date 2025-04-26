# Hướng dẫn sử dụng chức năng nhận diện hình ảnh trong OIADB

## Giới thiệu

Tài liệu này cung cấp hướng dẫn chi tiết về cách sử dụng chức năng nhận diện hình ảnh mới trong thư viện OIADB. Chức năng này cho phép bạn tìm kiếm, nhận diện và tương tác với các phần tử trên màn hình thiết bị Android dựa trên hình ảnh mẫu, thay vì phải dựa vào tọa độ cố định.

Chức năng nhận diện hình ảnh trong OIADB được thiết kế để hoạt động hiệu quả trên nhiều loại màn hình với các điều kiện khác nhau:
- Màn hình có phân giải cao/thấp khác nhau
- Hình ảnh nét/mờ/vỡ
- Hình ảnh có thể bị xoay hoặc biến dạng nhẹ
- Hình ảnh có thể có kích thước khác nhau

## Cài đặt

Để sử dụng chức năng nhận diện hình ảnh, bạn cần cài đặt OIADB với các phụ thuộc cần thiết:

```bash
pip install oiadb
```

Hoặc cài đặt từ mã nguồn:

```bash
git clone https://github.com/tiendung102k3/oiadb
cd oiadb
pip install -e .
```

Thư viện sẽ tự động cài đặt các phụ thuộc cần thiết bao gồm OpenCV và NumPy.

## Kiến trúc

Chức năng nhận diện hình ảnh trong OIADB được tổ chức thành hai lớp chính:

1. **ImageRecognition**: Lớp cơ sở cung cấp các chức năng nhận diện hình ảnh cấp thấp, nằm trong `utils/image_recognition.py`.
2. **ImageInteractionCommands**: Lớp cấp cao cung cấp các phương thức tương tác dựa trên nhận diện hình ảnh, nằm trong `commands/image_interaction.py`.

## Chuẩn bị hình ảnh mẫu

Trước khi sử dụng chức năng nhận diện hình ảnh, bạn cần chuẩn bị các hình ảnh mẫu:

1. **Chụp ảnh màn hình thiết bị**:
   ```python
   adb = MyADB()
   adb.take_screenshot("/path/to/screenshot.png")
   ```

2. **Cắt phần tử cần tìm kiếm**: Sử dụng công cụ chỉnh sửa ảnh để cắt phần tử cụ thể bạn muốn tìm kiếm từ ảnh chụp màn hình.

3. **Lưu ý khi chuẩn bị hình ảnh mẫu**:
   - Hình ảnh mẫu nên chỉ chứa phần tử cần tìm kiếm, không nên có quá nhiều nền xung quanh
   - Hình ảnh mẫu nên có độ tương phản tốt
   - Định dạng PNG được khuyến nghị để giữ chất lượng tốt nhất
   - Kích thước hình ảnh mẫu không quá lớn hoặc quá nhỏ so với kích thước thực tế trên màn hình

## Sử dụng cơ bản

### Khởi tạo

```python
from oiadb import MyADB
from commands.image_interaction import ImageInteractionCommands

# Khởi tạo ADB
adb = MyADB()

# Khởi tạo đối tượng tương tác hình ảnh
image_interaction = ImageInteractionCommands(adb)
```

### Tìm hình ảnh trên màn hình

```python
# Tìm hình ảnh đơn
result = image_interaction.find_image(
    template_path="/path/to/template.png",
    threshold=0.8,  # Ngưỡng tương đồng (0.0 - 1.0)
    region=None,    # Vùng tìm kiếm (x, y, width, height), None = toàn màn hình
    scale_range=(0.8, 1.2),  # Phạm vi tỷ lệ để tìm kiếm
    scale_steps=5,  # Số bước tỷ lệ
    rotation_range=(0, 0),  # Phạm vi góc xoay (độ)
    rotation_steps=1,  # Số bước góc xoay
    use_gray=True,  # Sử dụng ảnh xám để tăng tốc độ
    use_canny=False  # Sử dụng phát hiện cạnh Canny cho hình ảnh mờ
)

if result:
    x, y, confidence = result
    print(f"Đã tìm thấy hình ảnh tại ({x}, {y}) với độ tương đồng {confidence}")
else:
    print("Không tìm thấy hình ảnh")

# Tìm tất cả các hình ảnh
results = image_interaction.find_all_images(
    template_path="/path/to/template.png",
    threshold=0.8
)

for i, (x, y, confidence) in enumerate(results):
    print(f"Kết quả {i+1}: ({x}, {y}) với độ tương đồng {confidence}")
```

### Tìm và nhấp vào hình ảnh

```python
# Tìm và nhấp vào hình ảnh
success = image_interaction.tap_image(
    template_path="/path/to/button.png",
    threshold=0.8,
    tap_offset=(0, 0)  # Độ lệch (dx, dy) khi nhấp so với tâm hình ảnh
)

if success:
    print("Đã nhấp vào hình ảnh thành công")
else:
    print("Không tìm thấy hình ảnh để nhấp")
```

### Đợi hình ảnh xuất hiện và nhấp vào

```python
# Đợi hình ảnh xuất hiện và nhấp vào
success = image_interaction.wait_and_tap_image(
    template_path="/path/to/button.png",
    timeout=10,  # Thời gian tối đa đợi (giây)
    interval=0.5,  # Khoảng thời gian giữa các lần tìm kiếm (giây)
    threshold=0.8
)

if success:
    print("Đã đợi và nhấp vào hình ảnh thành công")
else:
    print("Hình ảnh không xuất hiện trong thời gian chờ")
```

### Kiểm tra sự hiện diện của hình ảnh

```python
# Kiểm tra xem hình ảnh có xuất hiện trên màn hình không
is_present = image_interaction.is_image_present(
    template_path="/path/to/element.png",
    threshold=0.8
)

if is_present:
    print("Hình ảnh xuất hiện trên màn hình")
else:
    print("Hình ảnh không xuất hiện trên màn hình")
```

### Đợi hình ảnh biến mất

```python
# Đợi hình ảnh biến mất khỏi màn hình
disappeared = image_interaction.wait_until_image_disappears(
    template_path="/path/to/loading.png",
    timeout=30,  # Thời gian tối đa đợi (giây)
    interval=1.0,  # Khoảng thời gian giữa các lần tìm kiếm (giây)
    threshold=0.8
)

if disappeared:
    print("Hình ảnh đã biến mất trong thời gian chờ")
else:
    print("Hình ảnh vẫn còn hiển thị sau thời gian chờ")
```

## Tương tác nâng cao

### Nhấp vào tất cả các hình ảnh tìm thấy

```python
# Tìm và nhấp vào tất cả các hình ảnh tương tự trên màn hình
count = image_interaction.tap_all_images(
    template_path="/path/to/button.png",
    threshold=0.8,
    tap_delay=0.5  # Thời gian chờ giữa các lần nhấp (giây)
)

print(f"Đã nhấp vào {count} hình ảnh")
```

### Kéo từ hình ảnh này đến hình ảnh khác

```python
# Kéo từ hình ảnh nguồn đến hình ảnh đích
success = image_interaction.drag_image_to_image(
    source_template_path="/path/to/source.png",
    target_template_path="/path/to/target.png",
    duration=800,  # Thời gian kéo (ms)
    threshold=0.8,
    source_offset=(0, 0),  # Độ lệch cho điểm nguồn
    target_offset=(0, 0)   # Độ lệch cho điểm đích
)

if success:
    print("Đã kéo thành công từ nguồn đến đích")
else:
    print("Không thể kéo vì không tìm thấy một hoặc cả hai hình ảnh")
```

### Nhấn giữ vào hình ảnh

```python
# Nhấn giữ vào hình ảnh
success = image_interaction.long_press_image(
    template_path="/path/to/element.png",
    duration=1000,  # Thời gian nhấn giữ (ms)
    threshold=0.8
)

if success:
    print("Đã nhấn giữ vào hình ảnh thành công")
else:
    print("Không tìm thấy hình ảnh để nhấn giữ")
```

### Nhấp đúp vào hình ảnh

```python
# Nhấp đúp vào hình ảnh
success = image_interaction.double_tap_image(
    template_path="/path/to/element.png",
    threshold=0.8,
    tap_delay=0.1  # Thời gian giữa hai lần nhấp (giây)
)

if success:
    print("Đã nhấp đúp vào hình ảnh thành công")
else:
    print("Không tìm thấy hình ảnh để nhấp đúp")
```

### Vuốt giữa hai hình ảnh

```python
# Vuốt từ hình ảnh đầu tiên đến hình ảnh thứ hai
success = image_interaction.swipe_between_images(
    start_template_path="/path/to/start.png",
    end_template_path="/path/to/end.png",
    duration=500,  # Thời gian vuốt (ms)
    threshold=0.8
)

if success:
    print("Đã vuốt thành công giữa hai hình ảnh")
else:
    print("Không thể vuốt vì không tìm thấy một hoặc cả hai hình ảnh")
```

## Xử lý các điều kiện màn hình khác nhau

OIADB cung cấp nhiều tùy chọn để xử lý các điều kiện màn hình khác nhau:

### Màn hình phân giải cao/thấp

```python
# Tìm trên màn hình phân giải cao
result_high_res = image_interaction.find_image(
    template_path="/path/to/template.png",
    threshold=0.8,
    scale_range=(1.0, 1.5),  # Tỷ lệ lớn hơn cho màn hình phân giải cao
    scale_steps=5
)

# Tìm trên màn hình phân giải thấp
result_low_res = image_interaction.find_image(
    template_path="/path/to/template.png",
    threshold=0.8,
    scale_range=(0.5, 1.0),  # Tỷ lệ nhỏ hơn cho màn hình phân giải thấp
    scale_steps=5
)
```

### Hình ảnh mờ/vỡ

```python
# Tìm hình ảnh mờ
result_blurry = image_interaction.find_image(
    template_path="/path/to/template.png",
    threshold=0.7,  # Ngưỡng thấp hơn cho hình ảnh mờ
    scale_range=(0.8, 1.2),
    scale_steps=5,
    use_canny=True  # Sử dụng phát hiện cạnh Canny cho hình ảnh mờ
)
```

### Hình ảnh xoay

```python
# Tìm hình ảnh có thể bị xoay
result_rotated = image_interaction.find_image(
    template_path="/path/to/template.png",
    threshold=0.7,
    scale_range=(0.8, 1.2),
    scale_steps=3,
    rotation_range=(-15, 15),  # Tìm với góc xoay từ -15 đến 15 độ
    rotation_steps=5
)
```

## Tối ưu hóa hiệu suất

### Giới hạn vùng tìm kiếm

```python
# Tìm trong một vùng cụ thể của màn hình
region = (100, 200, 300, 400)  # (x, y, width, height)
result = image_interaction.find_image(
    template_path="/path/to/template.png",
    threshold=0.8,
    region=region
)
```

### Điều chỉnh ngưỡng tương đồng

- **Ngưỡng cao (0.9-1.0)**: Tìm kiếm chính xác, ít kết quả sai nhưng có thể bỏ sót
- **Ngưỡng trung bình (0.7-0.8)**: Cân bằng giữa độ chính xác và khả năng tìm thấy
- **Ngưỡng thấp (0.5-0.6)**: Tìm kiếm linh hoạt, nhiều kết quả nhưng có thể có kết quả sai

```python
# Tìm kiếm chính xác
result_exact = image_interaction.find_image(
    template_path="/path/to/template.png",
    threshold=0.9
)

# Tìm kiếm linh hoạt
result_flexible = image_interaction.find_image(
    template_path="/path/to/template.png",
    threshold=0.6
)
```

### Sử dụng ảnh xám và phát hiện cạnh

```python
# Tìm kiếm nhanh với ảnh xám
result_fast = image_interaction.find_image(
    template_path="/path/to/template.png",
    threshold=0.8,
    use_gray=True,
    use_canny=False
)

# Tìm kiếm mạnh mẽ với phát hiện cạnh
result_robust = image_interaction.find_image(
    template_path="/path/to/template.png",
    threshold=0.7,
    use_gray=True,
    use_canny=True
)
```

## Ví dụ thực tế

### Tự động đăng nhập ứng dụng

```python
from oiadb import MyADB
from commands.image_interaction import ImageInteractionCommands

# Khởi tạo
adb = MyADB()
image_interaction = ImageInteractionCommands(adb)

# Đường dẫn đến các hình ảnh mẫu
app_icon_path = "./templates/app_icon.png"
login_button_path = "./templates/login_button.png"
username_field_path = "./templates/username_field.png"
password_field_path = "./templates/password_field.png"
submit_button_path = "./templates/submit_button.png"
loading_icon_path = "./templates/loading_icon.png"
home_screen_path = "./templates/home_screen.png"

# 1. Mở ứng dụng
if not image_interaction.tap_image(app_icon_path, threshold=0.8):
    print("Không tìm thấy biểu tượng ứng dụng.")
    exit(1)

# 2. Đợi màn hình đăng nhập xuất hiện
if not image_interaction.wait_for_image(login_button_path, timeout=10, threshold=0.8):
    print("Không tìm thấy màn hình đăng nhập.")
    exit(1)

# 3. Nhập tên người dùng
if image_interaction.tap_image(username_field_path, threshold=0.8):
    adb.run("shell input text 'testuser'")
else:
    print("Không tìm thấy trường tên người dùng.")
    exit(1)

# 4. Nhập mật khẩu
if image_interaction.tap_image(password_field_path, threshold=0.8):
    adb.run("shell input text 'password123'")
else:
    print("Không tìm thấy trường mật khẩu.")
    exit(1)

# 5. Nhấp vào nút đăng nhập
if not image_interaction.tap_image(submit_button_path, threshold=0.8):
    print("Không tìm thấy nút đăng nhập.")
    exit(1)

# 6. Đợi quá trình đăng nhập hoàn tất
if image_interaction.wait_for_image(loading_icon_path, timeout=5, threshold=0.7):
    if not image_interaction.wait_until_image_disappears(loading_icon_path, timeout=30, threshold=0.7):
        print("Quá trình đăng nhập mất quá nhiều thời gian.")
        exit(1)

# 7. Xác minh đã đăng nhập thành công
if image_interaction.is_image_present(home_screen_path, threshold=0.8):
    print("Đăng nhập thành công!")
else:
    print("Không thể xác minh đăng nhập thành công.")
```

### Tự động chơi game đơn giản

```python
from oiadb import MyADB
from commands.image_interaction import ImageInteractionCommands
import time

# Khởi tạo
adb = MyADB()
image_interaction = ImageInteractionCommands(adb)

# Đường dẫn đến các hình ảnh mẫu
game_icon_path = "./templates/game_icon.png"
play_button_path = "./templates/play_button.png"
character_path = "./templates/character.png"
obstacle_path = "./templates/obstacle.png"
coin_path = "./templates/coin.png"
game_over_path = "./templates/game_over.png"

# Mở game
image_interaction.tap_image(game_icon_path)
image_interaction.wait_and_tap_image(play_button_path, timeout=10)

# Vòng lặp chơi game
game_running = True
while game_running:
    # Thu thập tất cả các đồng xu
    coins = image_interaction.find_all_images(coin_path, threshold=0.7)
    for x, y, _ in coins:
        adb.run(f"shell input tap {x} {y}")
        time.sleep(0.2)
    
    # Tránh chướng ngại vật
    obstacles = image_interaction.find_all_images(obstacle_path, threshold=0.7)
    if obstacles:
        # Tìm vị trí nhân vật
        character = image_interaction.find_image(character_path)
        if character:
            char_x, char_y, _ = character
            
            # Tính toán hướng di chuyển để tránh chướng ngại vật gần nhất
            nearest_obstacle = min(obstacles, key=lambda o: ((o[0]-char_x)**2 + (o[1]-char_y)**2)**0.5)
            obs_x, obs_y, _ = nearest_obstacle
            
            # Di chuyển theo hướng ngược lại
            move_x = char_x + (char_x - obs_x)
            move_y = char_y + (char_y - obs_y)
            
            # Giới hạn trong màn hình
            move_x = max(50, min(move_x, 1030))
            move_y = max(50, min(move_y, 1870))
            
            # Thực hiện di chuyển
            adb.run(f"shell input tap {move_x} {move_y}")
    
    # Kiểm tra game over
    if image_interaction.is_image_present(game_over_path, threshold=0.8):
        print("Game over!")
        # Chơi lại
        image_interaction.tap_image(play_button_path)
    
    # Tạm dừng để giảm tải CPU
    time.sleep(0.1)
```

## Xử lý lỗi và gỡ rối

### Không tìm thấy hình ảnh

Nếu không tìm thấy hình ảnh, hãy thử các cách sau:

1. **Giảm ngưỡng tương đồng**: Thử giảm giá trị `threshold` xuống (ví dụ: 0.7 hoặc 0.6)
2. **Mở rộng phạm vi tỷ lệ**: Thử mở rộng `scale_range` (ví dụ: (0.5, 1.5))
3. **Sử dụng phát hiện cạnh**: Đặt `use_canny=True` để cải thiện kết quả với hình ảnh mờ
4. **Thử với góc xoay**: Đặt `rotation_range=(-15, 15)` và `rotation_steps=5` để tìm hình ảnh có thể bị xoay
5. **Chụp lại hình ảnh mẫu**: Hình ảnh mẫu có thể đã cũ hoặc không phù hợp với giao diện hiện tại

### Hiệu suất chậm

Nếu quá trình tìm kiếm hình ảnh quá chậm:

1. **Giới hạn vùng tìm kiếm**: Sử dụng tham số `region` để chỉ tìm trong một phần của màn hình
2. **Giảm số bước tỷ lệ và góc xoay**: Giảm `scale_steps` và `rotation_steps`
3. **Sử dụng ảnh xám**: Đảm bảo `use_gray=True` và `use_canny=False`
4. **Tối ưu hóa hình ảnh mẫu**: Sử dụng hình ảnh mẫu nhỏ hơn nhưng vẫn đủ đặc trưng

### Kết quả sai

Nếu tìm thấy kết quả không chính xác:

1. **Tăng ngưỡng tương đồng**: Thử tăng giá trị `threshold` lên (ví dụ: 0.85 hoặc 0.9)
2. **Sử dụng hình ảnh mẫu cụ thể hơn**: Chọn phần độc đáo của phần tử thay vì toàn bộ phần tử
3. **Thêm bối cảnh xung quanh**: Trong một số trường hợp, bao gồm một phần nhỏ của bối cảnh xung quanh có thể giúp phân biệt phần tử

## Thực hành tốt nhất

1. **Tổ chức hình ảnh mẫu**: Lưu trữ hình ảnh mẫu trong một thư mục riêng và đặt tên có ý nghĩa
2. **Sử dụng hình ảnh mẫu chất lượng cao**: Hình ảnh mẫu nên rõ ràng, không bị mờ hoặc nhiễu
3. **Xử lý lỗi**: Luôn kiểm tra kết quả trả về trước khi thực hiện các hành động tiếp theo
4. **Đặt thời gian chờ hợp lý**: Sử dụng `timeout` và `interval` phù hợp với tốc độ của ứng dụng
5. **Kết hợp với các phương thức ADB khác**: Sử dụng kết hợp nhận diện hình ảnh với các lệnh ADB khác để tạo quy trình tự động mạnh mẽ

## Giới hạn và lưu ý

1. **Phụ thuộc vào giao diện**: Nếu giao diện ứng dụng thay đổi, hình ảnh mẫu có thể không còn hiệu quả
2. **Tài nguyên hệ thống**: Nhận diện hình ảnh đòi hỏi nhiều tài nguyên CPU hơn so với các phương pháp tương tác khác
3. **Độ chính xác**: Kết quả có thể bị ảnh hưởng bởi các yếu tố như độ sáng màn hình, chủ đề, ngôn ngữ
4. **Hiệu suất**: Tìm kiếm với nhiều tỷ lệ và góc xoay có thể làm giảm hiệu suất

## Kết luận

Chức năng nhận diện hình ảnh trong OIADB cung cấp một cách mạnh mẽ và linh hoạt để tự động hóa tương tác với thiết bị Android. Bằng cách sử dụng nhận diện hình ảnh thay vì tọa độ cố định, bạn có thể tạo ra các quy trình tự động hoạt động trên nhiều thiết bị với kích thước màn hình và phân giải khác nhau.

Với khả năng xử lý các điều kiện màn hình khác nhau như hình ảnh mờ, vỡ hoặc xoay, OIADB cung cấp giải pháp mạnh mẽ cho việc tự động hóa thử nghiệm và tương tác với ứng dụng Android.

## Tham khảo

- [Tài liệu OpenCV](https://docs.opencv.org/)
- [Tài liệu NumPy](https://numpy.org/doc/)
- [Tài liệu ADB](https://developer.android.com/studio/command-line/adb)
