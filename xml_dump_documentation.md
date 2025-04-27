# XML Dump và Trợ Năng trong OIADB

Tài liệu này mô tả chi tiết về tính năng XML Dump và Trợ Năng (Accessibility) trong thư viện OIADB, đã được tối ưu hóa cho hiệu suất cao và tương thích với tất cả các phiên bản Android, bao gồm cả Android 14.

## Giới thiệu

Tính năng XML Dump cho phép truy xuất cấu trúc XML của giao diện người dùng Android thông qua một local server. Điều này giúp:

1. Phân tích cấu trúc UI một cách nhanh chóng
2. Tìm kiếm và tương tác với các phần tử UI dựa trên nhiều tiêu chí
3. Tận dụng các tính năng trợ năng (accessibility) của Android
4. Tối ưu hóa quá trình tự động hóa kiểm thử
5. Tương thích với tất cả các phiên bản Android, bao gồm cả Android 14
6. Hỗ trợ đa dạng giao diện từ các nhà sản xuất khác nhau (Samsung, Xiaomi, Huawei, v.v.)

## Kiến trúc

Tính năng XML Dump bao gồm các thành phần chính:

1. **Local Server**: Một HTTP server chạy trên thiết bị Android, cung cấp các API để truy xuất và xử lý XML
2. **XML Parser**: Bộ phân tích XML nhanh với khả năng lọc và tìm kiếm
3. **Accessibility Integration**: Tích hợp với API trợ năng của Android
4. **Parameter Handling**: Xử lý nhiều tham số để tìm kiếm và tương tác nhanh hơn
5. **Android 14 Support**: Hỗ trợ đặc biệt cho Android 14
6. **UI Compatibility**: Tương thích với nhiều loại giao diện Android khác nhau

Dưới đây là sơ đồ kiến trúc của tính năng XML Dump:

![Kiến trúc XML Dump](docs/images/xml_dump_architecture.png)

Sơ đồ trên minh họa cách các thành phần tương tác với nhau:
- **Local Server** cung cấp các API endpoints
- **XML Parser** xử lý và phân tích dữ liệu XML
- **Parameter Handler** xử lý các tham số truy vấn
- **UI Hierarchy** đại diện cho cấu trúc UI của ứng dụng Android
- **Accessibility API** cho phép tương tác với các phần tử UI
- **Client Application** là ứng dụng sử dụng XML dump API

## Quy trình xử lý

Tính năng XML Dump có ba luồng xử lý chính:

1. **XML Dump Flow**: Truy xuất và lọc cấu trúc XML
2. **Find Elements Flow**: Tìm kiếm các phần tử UI dựa trên tiêu chí
3. **Accessibility Flow**: Thực hiện các hành động trợ năng

![Quy trình XML Dump](docs/images/xml_dump_workflow.png)

Sơ đồ trên minh họa chi tiết các bước trong mỗi luồng xử lý:
- Luồng XML Dump bắt đầu từ HTTP Request và kết thúc bằng HTTP Response
- Luồng Find Elements bao gồm việc tìm kiếm, so khớp mờ và trả về kết quả dạng JSON
- Luồng Accessibility bao gồm truy vấn, phát hiện và thực thi các hành động trợ năng

## Cải tiến hiệu suất

Phiên bản mới nhất của tính năng XML Dump đã được tối ưu hóa đáng kể về hiệu suất:

1. **Caching thông minh**: Sử dụng LRU cache để lưu trữ kết quả XML dump và tránh truy vấn lặp lại
2. **Phân tích XML hiệu quả**: Sử dụng thư viện lxml thay vì regex để phân tích XML nhanh hơn
3. **Thuật toán so khớp cải tiến**: Sử dụng SequenceMatcher để so khớp chuỗi chính xác hơn
4. **Xử lý bất đồng bộ**: Server chạy trong thread riêng để không chặn luồng chính
5. **Giảm thiểu logging**: Tắt logging không cần thiết để tăng tốc độ xử lý
6. **Nhiều phương thức truy xuất XML**: Hỗ trợ nhiều cách để lấy XML dump, tự động chọn phương thức nhanh nhất

Những cải tiến này giúp tăng tốc độ xử lý lên đến 3-5 lần so với phiên bản trước.

## Hỗ trợ Android 14

Tính năng XML Dump đã được cập nhật để hỗ trợ đầy đủ Android 14 với các tính năng mới:

1. **Phát hiện phiên bản Android**: Tự động phát hiện phiên bản Android để sử dụng các API phù hợp
2. **Hành động trợ năng mới**: Hỗ trợ các hành động trợ năng mới trong Android 14
3. **Tương thích với thay đổi UI**: Thích ứng với các thay đổi trong giao diện người dùng của Android 14
4. **Hỗ trợ cử chỉ mới**: Hỗ trợ các cử chỉ mới được giới thiệu trong Android 14
5. **Quản lý quyền cải tiến**: Hỗ trợ mô hình quyền mới trong Android 14

Các hành động trợ năng mới trong Android 14:
- `contextClick`: Tương đương với nhấp chuột phải
- `showTooltip`: Hiển thị tooltip cho phần tử
- `dismiss`: Đóng phần tử (ví dụ: đóng hộp thoại)

## Tương thích giao diện

Tính năng XML Dump giờ đây hỗ trợ đa dạng giao diện từ các nhà sản xuất khác nhau:

1. **Stock Android**: Giao diện Android nguyên bản
2. **Samsung OneUI**: Giao diện của Samsung
3. **Xiaomi MIUI**: Giao diện của Xiaomi
4. **Huawei EMUI**: Giao diện của Huawei
5. **Oppo ColorOS**: Giao diện của Oppo
6. **OnePlus OxygenOS**: Giao diện của OnePlus

Hệ thống tự động phát hiện nhà sản xuất thiết bị và điều chỉnh cách tìm kiếm phần tử UI để đảm bảo tương thích tối đa.

## Yêu cầu quyền trợ năng

Để sử dụng đầy đủ tính năng XML Dump và trợ năng, bạn cần cấp quyền trợ năng cho ứng dụng:

1. **Bật dịch vụ trợ năng trên thiết bị Android**:
   - Vào Cài đặt > Trợ năng > Dịch vụ đã cài đặt
   - Hoặc Cài đặt > Quyền riêng tư > Trợ năng (tùy phiên bản Android)

2. **Cấp quyền ADB để điều khiển trợ năng**:
   ```bash
   adb shell settings put secure enabled_accessibility_services com.android.uiautomator/com.google.android.marvin.talkback.TalkBackService
   adb shell settings put secure accessibility_enabled 1
   ```

Lưu ý: Trên Android 14, quy trình cấp quyền có thể khác một chút. Sử dụng module `android14_support` để xử lý các trường hợp đặc biệt:

```python
from oiadb.commands import android14_support

# Bật dịch vụ trợ năng trên Android 14
android14_support.enable_accessibility_service()
```

## Các API Endpoint

### 1. `/get_xml`

Trả về cấu trúc XML của giao diện người dùng hiện tại.

**Tham số:**
- `id`: Lọc theo resource ID
- `value`: Lọc theo giá trị text
- `content_desc`: Lọc theo content description
- `class`: Lọc theo class name
- `threshold`: Ngưỡng tương đồng cho việc so khớp mờ (mặc định: 0.8)

**Ví dụ:**
```
http://192.168.1.1:8000/get_xml?id=button_login&threshold=0.7
```

### 2. `/find_elements`

Tìm các phần tử UI khớp với tiêu chí và trả về dưới dạng JSON.

**Tham số:**
- `id`: Tìm theo resource ID
- `value`: Tìm theo giá trị text
- `content_desc`: Tìm theo content description
- `class`: Tìm theo class name
- `threshold`: Ngưỡng tương đồng cho việc so khớp mờ (mặc định: 0.8)

**Ví dụ:**
```
http://192.168.1.1:8000/find_elements?class=android.widget.Button&value=Login
```

### 3. `/accessibility_actions`

Trả về danh sách các hành động trợ năng có sẵn cho một node cụ thể.

**Tham số:**
- `node_id`: ID của node cần lấy thông tin

**Ví dụ:**
```
http://192.168.1.1:8000/accessibility_actions?node_id=button_login
```

## Sử dụng trong Python

### Khởi động Server

```python
from oiadb.commands import xml_dump

# Khởi động server trên cổng 8000
server, server_thread = xml_dump.start_xml_server(port=8000)

# Thiết lập port forwarding
xml_dump.setup_port_forwarding(device_port=8000, host_port=8000)

# Lấy địa chỉ IP của thiết bị
device_ip = xml_dump.get_device_ip()
print(f"XML dump available at: http://{device_ip}:8000/get_xml")
```

### Lấy XML Dump

```python
# Lấy toàn bộ XML
xml_content = xml_dump.get_xml_dump()

# Lấy XML với bộ lọc
filtered_xml = xml_dump.get_xml_dump(
    resource_id="button_login",
    text_value="Login",
    threshold=0.7
)

# Sử dụng cache để tăng tốc độ
cached_xml = xml_dump.get_xml_dump(
    resource_id="button_login",
    use_cache=True
)
```

### Tìm Phần Tử UI

```python
# Tìm tất cả các nút
buttons = xml_dump.find_elements_by_criteria({"class": "android.widget.Button"})

# Tìm phần tử với nhiều tiêu chí
login_buttons = xml_dump.find_elements_by_criteria({
    "class": "android.widget.Button",
    "value": "Login",
    "threshold": 0.7
})
```

### Sử dụng UI Compatibility

```python
from oiadb.commands import ui_compatibility

# Tìm nút đăng nhập trên bất kỳ giao diện nào
login_button = ui_compatibility.find_ui_element(
    element_type="button",
    text="Login"
)

# Nhấp vào nút
ui_compatibility.click_ui_element(
    element_type="button",
    text="Login"
)

# Nhập text vào trường nhập liệu
ui_compatibility.input_text_to_element(
    element_type="text_field",
    resource_id="username_field",
    input_value="my_username"
)

# Tìm phần tử bằng XPath
element = ui_compatibility.find_element_by_xpath("//button[@text='Login']")
```

### Sử dụng Android 14 Support

```python
from oiadb.commands import android14_support

# Kiểm tra xem thiết bị có chạy Android 14 không
if android14_support.is_android_14_or_higher():
    # Bật dịch vụ trợ năng
    android14_support.enable_accessibility_service()
    
    # Thực hiện cử chỉ đặc biệt của Android 14
    android14_support.perform_android14_gesture(
        gesture_type="double_tap",
        x1=500,
        y1=500
    )
    
    # Xử lý thông báo
    notifications = android14_support.handle_android14_notifications()
    
    # Chụp ảnh màn hình chất lượng cao
    android14_support.capture_android14_screenshot("/path/to/screenshot.png")
```

### Thực Hiện Hành Động Trợ Năng

```python
# Nhấp vào nút có text "Login"
xml_dump.perform_accessibility_action(
    "click", 
    {"value": "Login", "threshold": 0.7}
)

# Nhập text vào trường EditText
xml_dump.perform_accessibility_action(
    "setText", 
    {"class": "android.widget.EditText"}, 
    "Hello from XML dump!"
)

# Sử dụng hành động mới trong Android 14
if android14_support.is_android_14_or_higher():
    xml_dump.perform_accessibility_action(
        "contextClick",
        {"id": "context_menu_button"}
    )
```

### Xóa Cache để Làm Mới Dữ Liệu

```python
# Xóa tất cả cache để đảm bảo dữ liệu mới nhất
xml_dump.clear_cache()
```

## So Khớp Mờ và Ngưỡng Tương Đồng

Tính năng XML Dump hỗ trợ so khớp mờ (fuzzy matching) với ngưỡng tương đồng có thể điều chỉnh:

- Ngưỡng 1.0: Khớp chính xác 100%
- Ngưỡng 0.8 (mặc định): Cho phép khớp gần đúng
- Ngưỡng thấp hơn: Cho phép khớp lỏng lẻo hơn

Điều này đặc biệt hữu ích khi:
- Text có thể thay đổi nhẹ giữa các phiên bản
- Cần tìm phần tử với text tương tự
- Xử lý các trường hợp không chắc chắn

Thuật toán so khớp mờ đã được cải tiến để sử dụng `SequenceMatcher` thay vì phương pháp đơn giản trước đây, giúp tăng độ chính xác của việc so khớp.

## Tối Ưu Hóa Hiệu Suất

Tính năng XML Dump được tối ưu hóa để xử lý nhanh:

1. **Phân Tích Hiệu Quả**: Sử dụng lxml thay vì regex để phân tích XML nhanh và chính xác hơn
2. **Caching Thông Minh**: Sử dụng LRU cache để lưu trữ kết quả và tránh truy vấn lặp lại
3. **Lọc Sớm**: Lọc dữ liệu ngay từ đầu để giảm khối lượng xử lý
4. **Truy Vấn Có Chỉ Mục**: Tìm kiếm nhanh các phần tử dựa trên thuộc tính
5. **Xử Lý Bất Đồng Bộ**: Server chạy trong thread riêng để không chặn luồng chính
6. **Giảm Thiểu Logging**: Tắt logging không cần thiết để tăng tốc độ xử lý
7. **Nhiều Phương Thức Truy Xuất**: Tự động chọn phương thức nhanh nhất để lấy XML dump

## Ví Dụ Thực Tế

### Tìm và Nhấp vào Nút Đăng Nhập trên Bất Kỳ Giao Diện Nào

```python
from oiadb.commands import ui_compatibility

# Tìm nút đăng nhập với text tương tự "Login" hoặc "Sign in"
login_button = ui_compatibility.find_ui_element(
    element_type="button",
    text="Login",
    threshold=0.7
)

# Nếu tìm thấy, nhấp vào nút
if login_button:
    ui_compatibility.click_ui_element(
        element_type="button",
        text="Login"
    )
```

### Điền Form Đăng Nhập với Hiệu Suất Cao

```python
from oiadb.commands import ui_compatibility, xml_dump

# Xóa cache để đảm bảo dữ liệu mới nhất
xml_dump.clear_cache()

# Tìm và nhập vào trường username
ui_compatibility.input_text_to_element(
    element_type="text_field",
    resource_id="username_field",
    input_value="my_username"
)

# Tìm và nhập vào trường password
ui_compatibility.input_text_to_element(
    element_type="text_field",
    resource_id="password_field",
    input_value="my_password"
)

# Nhấp vào nút submit
ui_compatibility.click_ui_element(
    element_type="button",
    resource_id="submit_button"
)
```

### Xử Lý Thông Báo trên Android 14

```python
from oiadb.commands import android14_support

# Kiểm tra xem thiết bị có chạy Android 14 không
if android14_support.is_android_14_or_higher():
    # Lấy danh sách thông báo
    notifications = android14_support.handle_android14_notifications()
    
    # Xử lý từng thông báo
    for notification in notifications:
        print(f"Title: {notification['title']}")
        print(f"Content: {notification['content']}")
```

### Sử Dụng XPath để Tìm Phần Tử

```python
from oiadb.commands import ui_compatibility

# Tìm nút đăng nhập bằng XPath
login_button = ui_compatibility.find_element_by_xpath("//button[@text='Login']")

# Tìm trường nhập liệu bằng XPath
username_field = ui_compatibility.find_element_by_xpath("//input[@id='username_field']")

# Tìm tất cả các checkbox
checkboxes = ui_compatibility.find_all_elements_by_xpath("//checkbox")
```

## Kết Luận

Tính năng XML Dump và Trợ Năng đã được cải tiến đáng kể với:

1. **Hiệu Suất Cao**: Xử lý XML nhanh hơn 3-5 lần so với phiên bản trước
2. **Tương Thích Rộng**: Hỗ trợ tất cả các phiên bản Android, bao gồm cả Android 14
3. **Đa Dạng Giao Diện**: Tương thích với nhiều loại giao diện từ các nhà sản xuất khác nhau
4. **API Linh Hoạt**: Cung cấp nhiều cách để tìm kiếm và tương tác với phần tử UI
5. **Dễ Sử Dụng**: API đơn giản và trực quan

Tính năng này đặc biệt hữu ích cho việc tự động hóa kiểm thử, phân tích UI và tương tác với ứng dụng Android trên mọi thiết bị và phiên bản.
