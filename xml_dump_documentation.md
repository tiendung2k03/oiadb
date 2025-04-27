# XML Dump và Trợ Năng trong OIADB

Tài liệu này mô tả chi tiết về tính năng XML Dump và Trợ Năng (Accessibility) trong thư viện OIADB.

## Giới thiệu

Tính năng XML Dump cho phép truy xuất cấu trúc XML của giao diện người dùng Android thông qua một local server. Điều này giúp:

1. Phân tích cấu trúc UI một cách nhanh chóng
2. Tìm kiếm và tương tác với các phần tử UI dựa trên nhiều tiêu chí
3. Tận dụng các tính năng trợ năng (accessibility) của Android
4. Tối ưu hóa quá trình tự động hóa kiểm thử

## Kiến trúc

Tính năng XML Dump bao gồm các thành phần chính:

1. **Local Server**: Một HTTP server chạy trên thiết bị Android, cung cấp các API để truy xuất và xử lý XML
2. **XML Parser**: Bộ phân tích XML nhanh với khả năng lọc và tìm kiếm
3. **Accessibility Integration**: Tích hợp với API trợ năng của Android
4. **Parameter Handling**: Xử lý nhiều tham số để tìm kiếm và tương tác nhanh hơn

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
```

### Lấy Hành Động Trợ Năng Có Sẵn

```python
# Lấy các hành động có sẵn cho một node cụ thể
actions = xml_dump.get_accessibility_actions("button_login")
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

## Tối Ưu Hóa Hiệu Suất

Tính năng XML Dump được tối ưu hóa để xử lý nhanh:

1. **Phân Tích Hiệu Quả**: Sử dụng regex và kỹ thuật phân tích nhẹ thay vì phân tích XML đầy đủ
2. **Lọc Sớm**: Lọc dữ liệu ngay từ đầu để giảm khối lượng xử lý
3. **Truy Vấn Có Chỉ Mục**: Tìm kiếm nhanh các phần tử dựa trên thuộc tính
4. **Xử Lý Bất Đồng Bộ**: Server chạy trong thread riêng để không chặn luồng chính

## Ví Dụ Thực Tế

### Tìm và Nhấp vào Nút Đăng Nhập

```python
# Tìm nút đăng nhập với text tương tự "Login" hoặc "Sign in"
login_buttons = xml_dump.find_elements_by_criteria({
    "class": "android.widget.Button",
    "value": "Login",
    "threshold": 0.7
})

# Nếu tìm thấy, nhấp vào nút đầu tiên
if login_buttons:
    xml_dump.perform_accessibility_action(
        "click", 
        {"id": login_buttons[0].get('resource-id')}
    )
```

### Điền Form Đăng Nhập

```python
# Tìm trường username
xml_dump.perform_accessibility_action(
    "setText", 
    {"id": "username_field"}, 
    "my_username"
)

# Tìm trường password
xml_dump.perform_accessibility_action(
    "setText", 
    {"id": "password_field"}, 
    "my_password"
)

# Nhấp vào nút submit
xml_dump.perform_accessibility_action(
    "click", 
    {"id": "submit_button"}
)
```

## Kết Luận

Tính năng XML Dump và Trợ Năng mang lại nhiều lợi ích:

1. **Tốc Độ**: Xử lý XML nhanh hơn với các kỹ thuật tối ưu
2. **Linh Hoạt**: Hỗ trợ nhiều tham số và tiêu chí tìm kiếm
3. **Trợ Năng**: Tích hợp với API trợ năng của Android
4. **Dễ Sử Dụng**: API đơn giản và trực quan

Tính năng này đặc biệt hữu ích cho việc tự động hóa kiểm thử, phân tích UI và tương tác với ứng dụng Android.
