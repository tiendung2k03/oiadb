# OIADB - Hướng dẫn sử dụng nhanh

## Giới thiệu

OIADB (OpenCV Image Android Debug Bridge) là thư viện Python wrapper cho Android Debug Bridge (ADB) với chức năng nhận diện hình ảnh sử dụng OpenCV. Thư viện này giúp đơn giản hóa việc tự động hóa các tác vụ trên thiết bị Android.

## Cài đặt

```bash
# Cài đặt từ PyPI
pip install oiadb

# Hoặc cài đặt từ mã nguồn
git clone https://github.com/tiendung102k3/oiadb
cd oiadb
pip install -e .
```

## Tính năng chính

- Tương tác với ADB thông qua Python
- Quản lý ứng dụng (cài đặt, gỡ cài đặt, khởi động, dừng)
- Thao tác file (đẩy, kéo, quản lý)
- Tương tác thiết bị (chạm, vuốt, nhập văn bản)
- Nhận diện hình ảnh (tìm và tương tác với phần tử dựa trên hình ảnh)
- Xử lý log và debug

## Ví dụ cơ bản

```python
from oiadb import MyADB
from oiadb.commands import interaction

# Khởi tạo ADB
adb = MyADB()

# Liệt kê thiết bị
devices = adb.get_devices()
print(f"Thiết bị đã kết nối: {devices}")

# Chụp ảnh màn hình
interaction.take_screenshot("screenshot.png")

# Nhấn vào tọa độ
interaction.tap(500, 500)
```

## Tài liệu chi tiết

Tài liệu đầy đủ có sẵn trong thư mục `docs/`:
- [Tài liệu chi tiết](oiadb_documentation.md)
- [Ví dụ cơ bản](examples/basic_usage.py)
- [Quản lý ứng dụng](examples/app_management.py)
- [Thao tác file](examples/file_operations.py)
- [Nhận diện hình ảnh](examples/image_recognition.py)
