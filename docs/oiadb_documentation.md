# OIADB - Tài liệu hướng dẫn chi tiết

<img src="/docs/images/architecture.png">

## Mục lục

1. [Giới thiệu](#1-giới-thiệu)
2. [Cài đặt](#2-cài-đặt)
3. [Kiến trúc thư viện](#3-kiến-trúc-thư-viện)
4. [Lớp MyADB](#4-lớp-myadb)
5. [Module Commands](#5-module-commands)
   - [5.1. app_info - Thông tin ứng dụng](#51-app_info---thông-tin-ứng-dụng)
   - [5.2. apps - Quản lý ứng dụng](#52-apps---quản-lý-ứng-dụng)
   - [5.3. basic - Lệnh cơ bản](#53-basic---lệnh-cơ-bản)
   - [5.4. connect - Kết nối thiết bị](#54-connect---kết-nối-thiết-bị)
   - [5.5. device_actions - Hành động thiết bị](#55-device_actions---hành-động-thiết-bị)
   - [5.6. device_info - Thông tin thiết bị](#56-device_info---thông-tin-thiết-bị)
   - [5.7. file_ops - Thao tác file](#57-file_ops---thao-tác-file)
   - [5.8. interaction - Tương tác thiết bị](#58-interaction---tương-tác-thiết-bị)
   - [5.9. image_interaction - Tương tác dựa trên hình ảnh](#59-image_interaction---tương-tác-dựa-trên-hình-ảnh)
   - [5.10. logs - Xem log](#510-logs---xem-log)
   - [5.11. permissions - Quản lý quyền](#511-permissions---quản-lý-quyền)
6. [Module Utils](#6-module-utils)
   - [6.1. advanced - Tiện ích nâng cao](#61-advanced---tiện-ích-nâng-cao)
   - [6.2. image_recognition - Nhận diện hình ảnh](#62-image_recognition---nhận-diện-hình-ảnh)
   - [6.3. runner - Chạy lệnh ADB](#63-runner---chạy-lệnh-adb)
7. [Hướng dẫn sử dụng](#7-hướng-dẫn-sử-dụng)
   - [7.1. Khởi tạo và kết nối](#71-khởi-tạo-và-kết-nối)
   - [7.2. Quản lý ứng dụng](#72-quản-lý-ứng-dụng)
   - [7.3. Thao tác file](#73-thao-tác-file)
   - [7.4. Tương tác với thiết bị](#74-tương-tác-với-thiết-bị)
   - [7.5. Tương tác dựa trên hình ảnh](#75-tương-tác-dựa-trên-hình-ảnh)
   - [7.6. Xử lý log và debug](#76-xử-lý-log-và-debug)
8. [Ví dụ thực tế](#8-ví-dụ-thực-tế)
   - [8.1. Tự động cài đặt và chạy ứng dụng](#81-tự-động-cài-đặt-và-chạy-ứng-dụng)
   - [8.2. Tự động kiểm thử UI](#82-tự-động-kiểm-thử-ui)
   - [8.3. Tự động hóa dựa trên nhận diện hình ảnh](#83-tự-động-hóa-dựa-trên-nhận-diện-hình-ảnh)
9. [Xử lý lỗi và gỡ rối](#9-xử-lý-lỗi-và-gỡ-rối)
10. [Thực hành tốt nhất](#10-thực-hành-tốt-nhất)
11. [Tham khảo](#11-tham-khảo)

## 1. Giới thiệu

OIADB (OpenCV Image Android Debug Bridge) là một thư viện Python wrapper cho Android Debug Bridge (ADB) với các chức năng nâng cao, bao gồm nhận diện hình ảnh sử dụng OpenCV. Thư viện này được thiết kế để đơn giản hóa việc sử dụng các lệnh ADB trong các ứng dụng Python, tự động hóa kiểm thử, và quản lý thiết bị Android.

### 1.1. Tính năng chính

- **Tương tác với ADB**: Cung cấp giao diện Python đơn giản cho các lệnh ADB phổ biến
- **Quản lý ứng dụng**: Cài đặt, gỡ cài đặt, khởi động, dừng và quản lý ứng dụng Android
- **Thao tác file**: Đẩy, kéo và quản lý file trên thiết bị Android
- **Tương tác thiết bị**: Mô phỏng các thao tác chạm, vuốt, nhập văn bản và các tương tác khác
- **Nhận diện hình ảnh**: Tìm và tương tác với các phần tử trên màn hình dựa trên hình ảnh mẫu
- **Xử lý log**: Thu thập và phân tích log từ thiết bị Android
- **Quản lý quyền**: Cấp và thu hồi quyền ứng dụng

### 1.2. Lợi ích

- **Đơn giản hóa tự động hóa**: Giảm thiểu mã lặp lại khi làm việc với ADB
- **Tự động hóa kiểm thử**: Dễ dàng tạo các kịch bản kiểm thử tự động cho ứng dụng Android
- **Tương tác dựa trên hình ảnh**: Tự động hóa mạnh mẽ không phụ thuộc vào tọa độ cố định
- **Tích hợp dễ dàng**: Tích hợp với các framework kiểm thử và tự động hóa khác

## 2. Cài đặt

### 2.1. Yêu cầu hệ thống

- Python 3.6 trở lên
- ADB đã được cài đặt và có trong PATH
- OpenCV (tự động cài đặt khi cài đặt thư viện)
- NumPy (tự động cài đặt khi cài đặt thư viện)

### 2.2. Cài đặt ADB

Trước khi sử dụng OIADB, bạn cần cài đặt Android Debug Bridge (ADB). ADB là một phần của Android SDK Platform Tools.

**Windows:**
```
1. Tải Android SDK Platform Tools từ https://developer.android.com/studio/releases/platform-tools
2. Giải nén vào thư mục, ví dụ: C:\android-sdk\platform-tools
3. Thêm đường dẫn vào biến môi trường PATH
```

**macOS:**
```
brew install android-platform-tools
```

**Linux:**
```
sudo apt-get install android-tools-adb
```

### 2.3. Cài đặt OIADB

#### 2.3.1. Cài đặt từ PyPI

```bash
pip install oiadb
```

#### 2.3.2. Cài đặt từ mã nguồn

```bash
git clone https://github.com/tiendung102k3/oiadb
cd oiadb
pip install -e .
```

### 2.4. Xác minh cài đặt

Để xác minh rằng OIADB đã được cài đặt đúng cách, hãy chạy đoạn mã Python sau:

```python
from oiadb import MyADB

# Khởi tạo ADB
adb = MyADB()

# Liệt kê các thiết bị đã kết nối
devices = adb.get_devices()
print(devices)
```

Nếu bạn thấy danh sách các thiết bị đã kết nối (hoặc danh sách trống nếu không có thiết bị nào), thì OIADB đã được cài đặt thành công.

## 3. Kiến trúc thư viện

OIADB được tổ chức thành các module và lớp khác nhau để cung cấp một API rõ ràng và dễ sử dụng.

### 3.1. Cấu trúc thư mục

```
oiadb/
├── __init__.py         # Điểm khởi đầu của thư viện
├── adb.py              # Lớp MyADB chính
├── exceptions.py       # Các lớp ngoại lệ
├── commands/           # Các module lệnh
│   ├── __init__.py
│   ├── app_info.py     # Thông tin ứng dụng
│   ├── apps.py         # Quản lý ứng dụng
│   ├── basic.py        # Lệnh cơ bản
│   ├── connect.py      # Kết nối thiết bị
│   ├── device_actions.py # Hành động thiết bị
│   ├── device_info.py  # Thông tin thiết bị
│   ├── file_ops.py     # Thao tác file
│   ├── image_interaction.py # Tương tác dựa trên hình ảnh
│   ├── interaction.py  # Tương tác thiết bị
│   ├── logs.py         # Xem log
│   └── permissions.py  # Quản lý quyền
└── utils/              # Các tiện ích
    ├── advanced.py     # Tiện ích nâng cao
    ├── image_recognition.py # Nhận diện hình ảnh
    └── runner.py       # Chạy lệnh ADB
```

### 3.2. Luồng hoạt động

1. **Lớp MyADB** (`adb.py`): Điểm khởi đầu chính, quản lý kết nối ADB và cung cấp các phương thức cấp cao
2. **Module Commands**: Các module chuyên biệt cho từng loại chức năng (ứng dụng, file, tương tác, v.v.)
3. **Module Utils**: Các tiện ích hỗ trợ, bao gồm nhận diện hình ảnh và chạy lệnh ADB
4. **Exceptions**: Xử lý lỗi và ngoại lệ

## 4. Lớp MyADB

Lớp `MyADB` là lớp chính của thư viện, cung cấp giao diện cho tất cả các chức năng ADB.

### 4.1. Khởi tạo

```python
from oiadb import MyADB

# Khởi tạo với thiết bị mặc định (thiết bị đầu tiên được tìm thấy)
adb = MyADB()

# Khởi tạo với thiết bị cụ thể
adb = MyADB(device_id="emulator-5554")
```

### 4.2. Phương thức chính

| Phương thức | Mô tả | Tham số | Giá trị trả về |
|-------------|-------|---------|----------------|
| `run(command)` | Chạy lệnh ADB tùy chỉnh | `command`: Lệnh ADB cần chạy | Kết quả lệnh dưới dạng chuỗi |
| `get_devices()` | Liệt kê các thiết bị đã kết nối | Không có | Danh sách các ID thiết bị |
| `reboot_device()` | Khởi động lại thiết bị | Không có | `True` nếu thành công |
| `install_app(apk_path)` | Cài đặt ứng dụng từ file APK | `apk_path`: Đường dẫn đến file APK | `True` nếu thành công |
| `uninstall_app(package_name)` | Gỡ cài đặt ứng dụng | `package_name`: Tên gói ứng dụng | `True` nếu thành công |
| `push_file(local_path, remote_path)` | Đẩy file lên thiết bị | `local_path`: Đường dẫn cục bộ<br>`remote_path`: Đường dẫn trên thiết bị | `True` nếu thành công |
| `pull_file(remote_path, local_path)` | Lấy file từ thiết bị | `remote_path`: Đường dẫn trên thiết bị<br>`local_path`: Đường dẫn cục bộ | `True` nếu thành công |
| `get_device_info()` | Lấy thông tin thiết bị | Không có | Dictionary chứa thông tin thiết bị |

### 4.3. Ví dụ sử dụng

```python
from oiadb import MyADB

# Khởi tạo ADB
adb = MyADB()

# Liệt kê các thiết bị đã kết nối
devices = adb.get_devices()
print(f"Các thiết bị đã kết nối: {devices}")

# Cài đặt ứng dụng
adb.install_app("/path/to/app.apk")

# Chạy lệnh ADB tùy chỉnh
result = adb.run("shell dumpsys battery")
print(f"Thông tin pin: {result}")
```

## 5. Module Commands

Module `commands` chứa các lớp và hàm chuyên biệt cho từng loại chức năng ADB.

### 5.1. app_info - Thông tin ứng dụng

Module `app_info` cung cấp các hàm để lấy thông tin về ứng dụng đã cài đặt.

#### 5.1.1. Hàm chính

| Hàm | Mô tả | Tham số | Giá trị trả về |
|-----|-------|---------|----------------|
| `get_app_version(package_name)` | Lấy phiên bản ứng dụng | `package_name`: Tên gói ứng dụng | Chuỗi phiên bản |
| `get_app_path(package_name)` | Lấy đường dẫn cài đặt ứng dụng | `package_name`: Tên gói ứng dụng | Đường dẫn cài đặt |

#### 5.1.2. Ví dụ sử dụng

```python
from oiadb import MyADB
from oiadb.commands import app_info

adb = MyADB()

# Lấy phiên bản ứng dụng
version = app_info.get_app_version("com.example.app")
print(f"Phiên bản: {version}")

# Lấy đường dẫn cài đặt ứng dụng
path = app_info.get_app_path("com.example.app")
print(f"Đường dẫn cài đặt: {path}")
```

### 5.2. apps - Quản lý ứng dụng

Module `apps` cung cấp các hàm để quản lý ứng dụng trên thiết bị.

#### 5.2.1. Hàm chính

| Hàm | Mô tả | Tham số | Giá trị trả về |
|-----|-------|---------|----------------|
| `install(apk_path, replace=False)` | Cài đặt ứng dụng | `apk_path`: Đường dẫn đến file APK<br>`replace`: Thay thế nếu đã tồn tại | `True` nếu thành công |
| `uninstall(package_name, keep_data=False)` | Gỡ cài đặt ứng dụng | `package_name`: Tên gói ứng dụng<br>`keep_data`: Giữ lại dữ liệu | `True` nếu thành công |
| `start_app(package_name, activity=None)` | Khởi động ứng dụng | `package_name`: Tên gói ứng dụng<br>`activity`: Tên activity (tùy chọn) | `True` nếu thành công |
| `stop_app(package_name)` | Dừng ứng dụng | `package_name`: Tên gói ứng dụng | `True` nếu thành công |
| `clear_app_data(package_name)` | Xóa dữ liệu ứng dụng | `package_name`: Tên gói ứng dụng | `True` nếu thành công |
| `list_installed_apps()` | Liệt kê ứng dụng đã cài đặt | Không có | Danh sách tên gói ứng dụng |
| `is_app_installed(package_name)` | Kiểm tra ứng dụng đã cài đặt | `package_name`: Tên gói ứng dụng | `True` nếu đã cài đặt |

#### 5.2.2. Ví dụ sử dụng

```python
from oiadb import MyADB
from oiadb.commands import apps

adb = MyADB()

# Cài đặt ứng dụng
apps.install("/path/to/app.apk")

# Khởi động ứng dụng
apps.start_app("com.example.app")

# Liệt kê ứng dụng đã cài đặt
installed_apps = apps.list_installed_apps()
print(f"Ứng dụng đã cài đặt: {installed_apps}")

# Dừng ứng dụng
apps.stop_app("com.example.app")

# Xóa dữ liệu ứng dụng
apps.clear_app_data("com.example.app")

# Gỡ cài đặt ứng dụng
apps.uninstall("com.example.app")
```

### 5.3. basic - Lệnh cơ bản

Module `basic` cung cấp các hàm cơ bản để tương tác với ADB.

#### 5.3.1. Hàm chính

| Hàm | Mô tả | Tham số | Giá trị trả về |
|-----|-------|---------|----------------|
| `adb_version()` | Lấy phiên bản ADB | Không có | Chuỗi phiên bản |
| `kill_server()` | Dừng máy chủ ADB | Không có | `True` nếu thành công |
| `start_server()` | Khởi động máy chủ ADB | Không có | `True` nếu thành công |
| `wait_for_device()` | Đợi thiết bị kết nối | Không có | `True` khi thiết bị kết nối |

#### 5.3.2. Ví dụ sử dụng

```python
from oiadb import MyADB
from oiadb.commands import basic

adb = MyADB()

# Lấy phiên bản ADB
version = basic.adb_version()
print(f"Phiên bản ADB: {version}")

# Khởi động lại máy chủ ADB
basic.kill_server()
basic.start_server()

# Đợi thiết bị kết nối
basic.wait_for_device()
print("Thiết bị đã kết nối!")
```

### 5.4. connect - Kết nối thiết bị

Module `connect` cung cấp các hàm để kết nối với thiết bị qua mạng.

#### 5.4.1. Hàm chính

| Hàm | Mô tả | Tham số | Giá trị trả về |
|-----|-------|---------|----------------|
| `connect(ip, port=5555)` | Kết nối thiết bị qua mạng | `ip`: Địa chỉ IP thiết bị<br>`port`: Cổng (mặc định 5555) | `True` nếu thành công |
| `disconnect(ip=None, port=5555)` | Ngắt kết nối thiết bị | `ip`: Địa chỉ IP thiết bị (tùy chọn)<br>`port`: Cổng (mặc định 5555) | `True` nếu thành công |
| `list_connected_devices()` | Liệt kê thiết bị đã kết nối | Không có | Danh sách ID thiết bị |

#### 5.4.2. Ví dụ sử dụng

```python
from oiadb import MyADB
from oiadb.commands import connect

adb = MyADB()

# Kết nối thiết bị qua mạng
connect.connect("192.168.1.100")
print("Đã kết nối thiết bị qua mạng!")

# Liệt kê thiết bị đã kết nối
devices = connect.list_connected_devices()
print(f"Thiết bị đã kết nối: {devices}")

# Ngắt kết nối thiết bị
connect.disconnect("192.168.1.100")
print("Đã ngắt kết nối thiết bị!")
```

### 5.5. device_actions - Hành động thiết bị

Module `device_actions` cung cấp các hàm để thực hiện các hành động trên thiết bị.

#### 5.5.1. Hàm chính

| Hàm | Mô tả | Tham số | Giá trị trả về |
|-----|-------|---------|----------------|
| `reboot()` | Khởi động lại thiết bị | Không có | `True` nếu thành công |
| `reboot_to_bootloader()` | Khởi động lại vào bootloader | Không có | `True` nếu thành công |
| `reboot_to_recovery()` | Khởi động lại vào recovery | Không có | `True` nếu thành công |
| `shutdown()` | Tắt thiết bị | Không có | `True` nếu thành công |
| `sleep()` | Đưa thiết bị vào chế độ ngủ | Không có | `True` nếu thành công |
| `wake()` | Đánh thức thiết bị | Không có | `True` nếu thành công |

#### 5.5.2. Ví dụ sử dụng

```python
from oiadb import MyADB
from oiadb.commands import device_actions

adb = MyADB()

# Đánh thức thiết bị
device_actions.wake()
print("Đã đánh thức thiết bị!")

# Đưa thiết bị vào chế độ ngủ
device_actions.sleep()
print("Đã đưa thiết bị vào chế độ ngủ!")

# Khởi động lại thiết bị
device_actions.reboot()
print("Đang khởi động lại thiết bị...")
```

### 5.6. device_info - Thông tin thiết bị

Module `device_info` cung cấp các hàm để lấy thông tin về thiết bị.

#### 5.6.1. Hàm chính

| Hàm | Mô tả | Tham số | Giá trị trả về |
|-----|-------|---------|----------------|
| `get_device_model()` | Lấy model thiết bị | Không có | Chuỗi model |
| `get_android_version()` | Lấy phiên bản Android | Không có | Chuỗi phiên bản |
| `get_screen_resolution()` | Lấy độ phân giải màn hình | Không có | Tuple (width, height) |
| `get_battery_info()` | Lấy thông tin pin | Không có | Dictionary thông tin pin |
| `get_imei()` | Lấy IMEI thiết bị | Không có | Chuỗi IMEI |
| `get_serial_number()` | Lấy số serial thiết bị | Không có | Chuỗi serial |
| `get_ip_address()` | Lấy địa chỉ IP thiết bị | Không có | Chuỗi IP |
| `get_memory_info()` | Lấy thông tin bộ nhớ | Không có | Dictionary thông tin bộ nhớ |
| `get_cpu_info()` | Lấy thông tin CPU | Không có | Dictionary thông tin CPU |

#### 5.6.2. Ví dụ sử dụng

```python
from oiadb import MyADB
from oiadb.commands import device_info

adb = MyADB()

# Lấy model thiết bị
model = device_info.get_device_model()
print(f"Model thiết bị: {model}")

# Lấy phiên bản Android
android_version = device_info.get_android_version()
print(f"Phiên bản Android: {android_version}")

# Lấy độ phân giải màn hình
width, height = device_info.get_screen_resolution()
print(f"Độ phân giải màn hình: {width}x{height}")

# Lấy thông tin pin
battery_info = device_info.get_battery_info()
print(f"Thông tin pin: {battery_info}")
```

### 5.7. file_ops - Thao tác file

Module `file_ops` cung cấp các hàm để thao tác với file trên thiết bị.

#### 5.7.1. Hàm chính

| Hàm | Mô tả | Tham số | Giá trị trả về |
|-----|-------|---------|----------------|
| `push(local_path, remote_path)` | Đẩy file lên thiết bị | `local_path`: Đường dẫn cục bộ<br>`remote_path`: Đường dẫn trên thiết bị | `True` nếu thành công |
| `pull(remote_path, local_path)` | Lấy file từ thiết bị | `remote_path`: Đường dẫn trên thiết bị<br>`local_path`: Đường dẫn cục bộ | `True` nếu thành công |
| `list_files(remote_path)` | Liệt kê file trong thư mục | `remote_path`: Đường dẫn thư mục trên thiết bị | Danh sách tên file |
| `file_exists(remote_path)` | Kiểm tra file tồn tại | `remote_path`: Đường dẫn file trên thiết bị | `True` nếu tồn tại |
| `create_dir(remote_path)` | Tạo thư mục | `remote_path`: Đường dẫn thư mục trên thiết bị | `True` nếu thành công |
| `remove_file(remote_path)` | Xóa file | `remote_path`: Đường dẫn file trên thiết bị | `True` nếu thành công |
| `remove_dir(remote_path)` | Xóa thư mục | `remote_path`: Đường dẫn thư mục trên thiết bị | `True` nếu thành công |
| `copy_file(source_path, dest_path)` | Sao chép file | `source_path`: Đường dẫn nguồn<br>`dest_path`: Đường dẫn đích | `True` nếu thành công |
| `move_file(source_path, dest_path)` | Di chuyển file | `source_path`: Đường dẫn nguồn<br>`dest_path`: Đường dẫn đích | `True` nếu thành công |
| `get_file_size(remote_path)` | Lấy kích thước file | `remote_path`: Đường dẫn file trên thiết bị | Kích thước file (bytes) |
| `get_file_permissions(remote_path)` | Lấy quyền file | `remote_path`: Đường dẫn file trên thiết bị | Chuỗi quyền (ví dụ: "rwxr-xr--") |
| `set_file_permissions(remote_path, permissions)` | Đặt quyền file | `remote_path`: Đường dẫn file trên thiết bị<br>`permissions`: Quyền (ví dụ: "755") | `True` nếu thành công |

#### 5.7.2. Ví dụ sử dụng

```python
from oiadb import MyADB
from oiadb.commands import file_ops

adb = MyADB()

# Đẩy file lên thiết bị
file_ops.push("/path/on/computer/file.txt", "/sdcard/file.txt")
print("Đã đẩy file lên thiết bị!")

# Liệt kê file trong thư mục
files = file_ops.list_files("/sdcard")
print(f"Các file trong /sdcard: {files}")

# Kiểm tra file tồn tại
if file_ops.file_exists("/sdcard/file.txt"):
    print("File tồn tại trên thiết bị!")

# Lấy kích thước file
size = file_ops.get_file_size("/sdcard/file.txt")
print(f"Kích thước file: {size} bytes")

# Lấy file từ thiết bị
file_ops.pull("/sdcard/file.txt", "/path/on/computer/downloaded_file.txt")
print("Đã lấy file từ thiết bị!")

# Xóa file
file_ops.remove_file("/sdcard/file.txt")
print("Đã xóa file trên thiết bị!")
```

### 5.8. interaction - Tương tác thiết bị

Module `interaction` cung cấp các hàm để tương tác với thiết bị thông qua các thao tác chạm, vuốt, nhập văn bản, v.v.

#### 5.8.1. Hàm chính

| Hàm | Mô tả | Tham số | Giá trị trả về |
|-----|-------|---------|----------------|
| `tap(x, y)` | Nhấn vào tọa độ | `x`: Tọa độ X<br>`y`: Tọa độ Y | `True` nếu thành công |
| `long_press(x, y, duration=1000)` | Nhấn giữ vào tọa độ | `x`: Tọa độ X<br>`y`: Tọa độ Y<br>`duration`: Thời gian (ms) | `True` nếu thành công |
| `swipe(start_x, start_y, end_x, end_y, duration=300)` | Vuốt từ điểm này đến điểm khác | `start_x`, `start_y`: Điểm bắt đầu<br>`end_x`, `end_y`: Điểm kết thúc<br>`duration`: Thời gian (ms) | `True` nếu thành công |
| `text_input(text)` | Nhập văn bản | `text`: Văn bản cần nhập | `True` nếu thành công |
| `key_event(keycode)` | Gửi sự kiện phím | `keycode`: Mã phím | `True` nếu thành công |
| `back()` | Nhấn nút Back | Không có | `True` nếu thành công |
| `home()` | Nhấn nút Home | Không có | `True` nếu thành công |
| `recent_apps()` | Mở màn hình ứng dụng gần đây | Không có | `True` nếu thành công |
| `power()` | Nhấn nút nguồn | Không có | `True` nếu thành công |
| `volume_up()` | Tăng âm lượng | Không có | `True` nếu thành công |
| `volume_down()` | Giảm âm lượng | Không có | `True` nếu thành công |
| `mute()` | Tắt âm | Không có | `True` nếu thành công |
| `take_screenshot(output_path)` | Chụp ảnh màn hình | `output_path`: Đường dẫn lưu ảnh | `True` nếu thành công |

#### 5.8.2. Ví dụ sử dụng

```python
from oiadb import MyADB
from oiadb.commands import interaction
import time

adb = MyADB()

# Mở màn hình chính
interaction.home()

# Chụp ảnh màn hình
interaction.take_screenshot("/path/on/computer/screenshot.png")
print("Đã chụp ảnh màn hình!")

# Vuốt để mở ngăn thông báo
interaction.swipe(500, 0, 500, 1000)

# Đợi ngăn thông báo mở
time.sleep(1)

# Nhấn vào tọa độ
interaction.tap(500, 500)

# Nhập văn bản
interaction.text_input("Hello World")

# Nhấn nút Back
interaction.back()
```

### 5.9. image_interaction - Tương tác dựa trên hình ảnh

Module `image_interaction` cung cấp các hàm để tương tác với thiết bị dựa trên nhận diện hình ảnh.

#### 5.9.1. Hàm chính

| Hàm | Mô tả | Tham số | Giá trị trả về |
|-----|-------|---------|----------------|
| `find_image(template_path, threshold=0.8, region=None, scale_range=(0.8, 1.2), scale_steps=5, rotation_range=(0, 0), rotation_steps=1, use_gray=True, use_canny=False)` | Tìm hình ảnh trên màn hình | `template_path`: Đường dẫn hình ảnh mẫu<br>`threshold`: Ngưỡng tương đồng (0.0-1.0)<br>`region`: Vùng tìm kiếm (x, y, width, height)<br>`scale_range`: Phạm vi tỷ lệ<br>`scale_steps`: Số bước tỷ lệ<br>`rotation_range`: Phạm vi góc xoay<br>`rotation_steps`: Số bước góc xoay<br>`use_gray`: Sử dụng ảnh xám<br>`use_canny`: Sử dụng phát hiện cạnh | Tuple (x, y, confidence) hoặc None |
| `find_all_images(template_path, threshold=0.8, region=None, scale_range=(0.8, 1.2), scale_steps=5, max_results=10, use_gray=True, use_canny=False)` | Tìm tất cả các hình ảnh tương tự | Tương tự `find_image`<br>`max_results`: Số kết quả tối đa | Danh sách các tuple (x, y, confidence) |
| `tap_image(template_path, threshold=0.8, tap_offset=(0, 0), scale_range=(0.8, 1.2), scale_steps=5, use_gray=True, use_canny=False)` | Tìm và nhấp vào hình ảnh | Tương tự `find_image`<br>`tap_offset`: Độ lệch khi nhấp | `True` nếu thành công |
| `wait_for_image(template_path, timeout=30, interval=1.0, threshold=0.8, region=None, scale_range=(0.8, 1.2), scale_steps=5, use_gray=True, use_canny=False)` | Đợi hình ảnh xuất hiện | Tương tự `find_image`<br>`timeout`: Thời gian tối đa đợi (giây)<br>`interval`: Khoảng thời gian giữa các lần tìm kiếm (giây) | Tuple (x, y, confidence) hoặc None |
| `wait_until_image_disappears(template_path, timeout=30, interval=1.0, threshold=0.8, region=None, scale_range=(0.8, 1.2), scale_steps=5, use_gray=True, use_canny=False)` | Đợi hình ảnh biến mất | Tương tự `wait_for_image` | `True` nếu hình ảnh biến mất |
| `is_image_present(template_path, threshold=0.8, region=None, scale_range=(0.8, 1.2), scale_steps=5, use_gray=True, use_canny=False)` | Kiểm tra hình ảnh có xuất hiện | Tương tự `find_image` | `True` nếu hình ảnh xuất hiện |
| `wait_and_tap_image(template_path, timeout=30, interval=1.0, threshold=0.8, tap_offset=(0, 0), scale_range=(0.8, 1.2), scale_steps=5, use_gray=True, use_canny=False)` | Đợi và nhấp vào hình ảnh | Kết hợp `wait_for_image` và `tap_image` | `True` nếu thành công |
| `tap_all_images(template_path, threshold=0.8, tap_delay=0.5, scale_range=(0.8, 1.2), scale_steps=5, use_gray=True, use_canny=False)` | Nhấp vào tất cả các hình ảnh tương tự | Tương tự `find_all_images`<br>`tap_delay`: Thời gian giữa các lần nhấp (giây) | Số lượng hình ảnh đã nhấp |
| `drag_image_to_image(source_template_path, target_template_path, duration=800, threshold=0.8, scale_range=(0.8, 1.2), scale_steps=5, source_offset=(0, 0), target_offset=(0, 0), use_gray=True, use_canny=False)` | Kéo từ hình ảnh này đến hình ảnh khác | `source_template_path`: Hình ảnh nguồn<br>`target_template_path`: Hình ảnh đích<br>Các tham số khác tương tự | `True` nếu thành công |
| `long_press_image(template_path, duration=1000, threshold=0.8, scale_range=(0.8, 1.2), scale_steps=5, use_gray=True, use_canny=False)` | Nhấn giữ vào hình ảnh | Tương tự `tap_image`<br>`duration`: Thời gian nhấn giữ (ms) | `True` nếu thành công |
| `double_tap_image(template_path, threshold=0.8, tap_delay=0.1, scale_range=(0.8, 1.2), scale_steps=5, use_gray=True, use_canny=False)` | Nhấp đúp vào hình ảnh | Tương tự `tap_image`<br>`tap_delay`: Thời gian giữa hai lần nhấp (giây) | `True` nếu thành công |
| `swipe_between_images(start_template_path, end_template_path, duration=500, threshold=0.8, scale_range=(0.8, 1.2), scale_steps=5, use_gray=True, use_canny=False)` | Vuốt giữa hai hình ảnh | Tương tự `drag_image_to_image` | `True` nếu thành công |

#### 5.9.2. Ví dụ sử dụng

```python
from oiadb import MyADB
from oiadb.commands import image_interaction
import time

adb = MyADB()

# Tìm hình ảnh trên màn hình
result = image_interaction.find_image("/path/to/button.png", threshold=0.8)
if result:
    x, y, confidence = result
    print(f"Đã tìm thấy hình ảnh tại ({x}, {y}) với độ tương đồng {confidence}")
else:
    print("Không tìm thấy hình ảnh")

# Tìm và nhấp vào hình ảnh
if image_interaction.tap_image("/path/to/button.png", threshold=0.8):
    print("Đã nhấp vào hình ảnh thành công")
else:
    print("Không tìm thấy hình ảnh để nhấp")

# Đợi hình ảnh xuất hiện và nhấp vào
if image_interaction.wait_and_tap_image("/path/to/button.png", timeout=10, threshold=0.8):
    print("Đã đợi và nhấp vào hình ảnh thành công")
else:
    print("Hình ảnh không xuất hiện trong thời gian chờ")

# Kéo từ hình ảnh này đến hình ảnh khác
if image_interaction.drag_image_to_image("/path/to/source.png", "/path/to/target.png", duration=800):
    print("Đã kéo thành công từ nguồn đến đích")
else:
    print("Không thể kéo vì không tìm thấy một hoặc cả hai hình ảnh")
```

### 5.10. logs - Xem log

Module `logs` cung cấp các hàm để xem và phân tích log từ thiết bị.

#### 5.10.1. Hàm chính

| Hàm | Mô tả | Tham số | Giá trị trả về |
|-----|-------|---------|----------------|
| `logcat(options=None)` | Xem logcat | `options`: Tùy chọn logcat (ví dụ: "-v time") | Chuỗi log |
| `clear_logcat()` | Xóa logcat | Không có | `True` nếu thành công |
| `logcat_to_file(output_path, options=None)` | Lưu logcat vào file | `output_path`: Đường dẫn file<br>`options`: Tùy chọn logcat | `True` nếu thành công |
| `filter_logcat(tag=None, priority=None, message=None)` | Lọc logcat | `tag`: Tag cần lọc<br>`priority`: Mức ưu tiên<br>`message`: Nội dung cần lọc | Chuỗi log đã lọc |
| `bugreport(output_path=None)` | Tạo báo cáo lỗi | `output_path`: Đường dẫn file (tùy chọn) | Chuỗi báo cáo hoặc `True` nếu lưu vào file |

#### 5.10.2. Ví dụ sử dụng

```python
from oiadb import MyADB
from oiadb.commands import logs

adb = MyADB()

# Xóa logcat
logs.clear_logcat()
print("Đã xóa logcat!")

# Xem logcat
logcat_output = logs.logcat("-v time")
print(f"Logcat: {logcat_output}")

# Lọc logcat
filtered_log = logs.filter_logcat(tag="ActivityManager", priority="E")
print(f"Logcat đã lọc: {filtered_log}")

# Lưu logcat vào file
logs.logcat_to_file("/path/on/computer/logcat.txt")
print("Đã lưu logcat vào file!")

# Tạo báo cáo lỗi
logs.bugreport("/path/on/computer/bugreport.zip")
print("Đã tạo báo cáo lỗi!")
```

### 5.11. permissions - Quản lý quyền

Module `permissions` cung cấp các hàm để quản lý quyền ứng dụng.

#### 5.11.1. Hàm chính

| Hàm | Mô tả | Tham số | Giá trị trả về |
|-----|-------|---------|----------------|
| `grant(package_name, permission)` | Cấp quyền cho ứng dụng | `package_name`: Tên gói ứng dụng<br>`permission`: Quyền cần cấp | `True` nếu thành công |
| `revoke(package_name, permission)` | Thu hồi quyền từ ứng dụng | `package_name`: Tên gói ứng dụng<br>`permission`: Quyền cần thu hồi | `True` nếu thành công |
| `list_permissions(package_name)` | Liệt kê quyền của ứng dụng | `package_name`: Tên gói ứng dụng | Danh sách quyền |
| `has_permission(package_name, permission)` | Kiểm tra ứng dụng có quyền | `package_name`: Tên gói ứng dụng<br>`permission`: Quyền cần kiểm tra | `True` nếu có quyền |

#### 5.11.2. Ví dụ sử dụng

```python
from oiadb import MyADB
from oiadb.commands import permissions

adb = MyADB()

# Liệt kê quyền của ứng dụng
perms = permissions.list_permissions("com.example.app")
print(f"Quyền của ứng dụng: {perms}")

# Kiểm tra ứng dụng có quyền
if permissions.has_permission("com.example.app", "android.permission.CAMERA"):
    print("Ứng dụng có quyền truy cập camera!")
else:
    print("Ứng dụng không có quyền truy cập camera!")

# Cấp quyền cho ứng dụng
permissions.grant("com.example.app", "android.permission.CAMERA")
print("Đã cấp quyền truy cập camera cho ứng dụng!")

# Thu hồi quyền từ ứng dụng
permissions.revoke("com.example.app", "android.permission.CAMERA")
print("Đã thu hồi quyền truy cập camera từ ứng dụng!")
```

## 6. Module Utils

Module `utils` chứa các tiện ích hỗ trợ cho thư viện.

### 6.1. advanced - Tiện ích nâng cao

Module `advanced` cung cấp các tiện ích nâng cao cho thư viện.

#### 6.1.1. Hàm chính

| Hàm | Mô tả | Tham số | Giá trị trả về |
|-----|-------|---------|----------------|
| `get_focused_window()` | Lấy cửa sổ đang focus | Không có | Tên cửa sổ |
| `get_current_activity()` | Lấy activity hiện tại | Không có | Tên activity |
| `get_view_hierarchy()` | Lấy cây phân cấp view | Không có | Chuỗi XML |
| `dump_ui_xml(output_path=None)` | Xuất UI thành XML | `output_path`: Đường dẫn file (tùy chọn) | Chuỗi XML hoặc `True` nếu lưu vào file |
| `get_view_properties(view_id)` | Lấy thuộc tính của view | `view_id`: ID của view | Dictionary thuộc tính |
| `find_view_by_text(text)` | Tìm view theo text | `text`: Text cần tìm | Danh sách view ID |
| `find_view_by_id(resource_id)` | Tìm view theo ID | `resource_id`: ID tài nguyên | Danh sách view ID |
| `find_view_by_class(class_name)` | Tìm view theo class | `class_name`: Tên class | Danh sách view ID |

#### 6.1.2. Ví dụ sử dụng

```python
from oiadb import MyADB
from oiadb.utils import advanced

adb = MyADB()

# Lấy activity hiện tại
activity = advanced.get_current_activity()
print(f"Activity hiện tại: {activity}")

# Lấy cửa sổ đang focus
window = advanced.get_focused_window()
print(f"Cửa sổ đang focus: {window}")

# Xuất UI thành XML
xml = advanced.dump_ui_xml()
print(f"UI XML: {xml}")

# Tìm view theo text
views = advanced.find_view_by_text("Login")
print(f"Các view có text 'Login': {views}")
```

### 6.2. image_recognition - Nhận diện hình ảnh

Module `image_recognition` cung cấp các chức năng nhận diện hình ảnh cấp thấp.

#### 6.2.1. Lớp ImageRecognition

Lớp `ImageRecognition` cung cấp các phương thức để nhận diện hình ảnh trên màn hình thiết bị.

| Phương thức | Mô tả | Tham số | Giá trị trả về |
|-------------|-------|---------|----------------|
| `__init__(adb_instance)` | Khởi tạo | `adb_instance`: Đối tượng MyADB | Không có |
| `find_template(screenshot, template, threshold=0.8, region=None, use_gray=True, use_canny=False)` | Tìm mẫu trong ảnh | `screenshot`: Ảnh màn hình<br>`template`: Ảnh mẫu<br>`threshold`: Ngưỡng tương đồng<br>`region`: Vùng tìm kiếm<br>`use_gray`: Sử dụng ảnh xám<br>`use_canny`: Sử dụng phát hiện cạnh | Tuple (x, y, confidence) hoặc None |
| `find_all_templates(screenshot, template, threshold=0.8, region=None, max_results=10, use_gray=True, use_canny=False)` | Tìm tất cả các mẫu | Tương tự `find_template`<br>`max_results`: Số kết quả tối đa | Danh sách các tuple (x, y, confidence) |
| `find_template_with_scale(screenshot, template, threshold=0.8, region=None, scale_range=(0.8, 1.2), scale_steps=5, use_gray=True, use_canny=False)` | Tìm mẫu với nhiều tỷ lệ | Tương tự `find_template`<br>`scale_range`: Phạm vi tỷ lệ<br>`scale_steps`: Số bước tỷ lệ | Tuple (x, y, confidence, scale) hoặc None |
| `find_template_with_rotation(screenshot, template, threshold=0.8, region=None, rotation_range=(-15, 15), rotation_steps=5, use_gray=True, use_canny=False)` | Tìm mẫu với nhiều góc xoay | Tương tự `find_template`<br>`rotation_range`: Phạm vi góc xoay<br>`rotation_steps`: Số bước góc xoay | Tuple (x, y, confidence, angle) hoặc None |
| `find_template_with_scale_and_rotation(screenshot, template, threshold=0.8, region=None, scale_range=(0.8, 1.2), scale_steps=5, rotation_range=(-15, 15), rotation_steps=5, use_gray=True, use_canny=False)` | Tìm mẫu với nhiều tỷ lệ và góc xoay | Kết hợp các tham số trên | Tuple (x, y, confidence, scale, angle) hoặc None |
| `take_screenshot()` | Chụp ảnh màn hình | Không có | Ảnh màn hình (numpy array) |
| `load_template(template_path)` | Tải ảnh mẫu | `template_path`: Đường dẫn ảnh mẫu | Ảnh mẫu (numpy array) |

#### 6.2.2. Ví dụ sử dụng

```python
from oiadb import MyADB
from oiadb.utils.image_recognition import ImageRecognition
import cv2

adb = MyADB()
image_recognition = ImageRecognition(adb)

# Chụp ảnh màn hình
screenshot = image_recognition.take_screenshot()

# Tải ảnh mẫu
template = image_recognition.load_template("/path/to/button.png")

# Tìm mẫu trong ảnh
result = image_recognition.find_template(screenshot, template, threshold=0.8)
if result:
    x, y, confidence = result
    print(f"Đã tìm thấy mẫu tại ({x}, {y}) với độ tương đồng {confidence}")
else:
    print("Không tìm thấy mẫu")

# Tìm mẫu với nhiều tỷ lệ
result = image_recognition.find_template_with_scale(
    screenshot, template, threshold=0.8, scale_range=(0.8, 1.2), scale_steps=5
)
if result:
    x, y, confidence, scale = result
    print(f"Đã tìm thấy mẫu tại ({x}, {y}) với độ tương đồng {confidence} và tỷ lệ {scale}")
else:
    print("Không tìm thấy mẫu")
```

### 6.3. runner - Chạy lệnh ADB

Module `runner` cung cấp các hàm để chạy lệnh ADB.

#### 6.3.1. Hàm chính

| Hàm | Mô tả | Tham số | Giá trị trả về |
|-----|-------|---------|----------------|
| `run_adb_command(command, device_id=None)` | Chạy lệnh ADB | `command`: Lệnh ADB<br>`device_id`: ID thiết bị (tùy chọn) | Chuỗi kết quả |
| `run_shell_command(command, device_id=None)` | Chạy lệnh shell | `command`: Lệnh shell<br>`device_id`: ID thiết bị (tùy chọn) | Chuỗi kết quả |
| `get_adb_path()` | Lấy đường dẫn ADB | Không có | Đường dẫn ADB |

#### 6.3.2. Ví dụ sử dụng

```python
from oiadb.utils import runner

# Chạy lệnh ADB
result = runner.run_adb_command("devices")
print(f"Kết quả lệnh ADB: {result}")

# Chạy lệnh shell
result = runner.run_shell_command("ls /sdcard")
print(f"Kết quả lệnh shell: {result}")

# Lấy đường dẫn ADB
adb_path = runner.get_adb_path()
print(f"Đường dẫn ADB: {adb_path}")
```

## 7. Hướng dẫn sử dụng

### 7.1. Khởi tạo và kết nối

#### 7.1.1. Khởi tạo ADB

```python
from oiadb import MyADB

# Khởi tạo với thiết bị mặc định
adb = MyADB()

# Khởi tạo với thiết bị cụ thể
adb = MyADB(device_id="emulator-5554")
```

#### 7.1.2. Kết nối thiết bị qua mạng

```python
from oiadb import MyADB
from oiadb.commands import connect

adb = MyADB()

# Kết nối thiết bị qua mạng
connect.connect("192.168.1.100")

# Liệt kê thiết bị đã kết nối
devices = connect.list_connected_devices()
print(f"Thiết bị đã kết nối: {devices}")

# Ngắt kết nối thiết bị
connect.disconnect("192.168.1.100")
```

#### 7.1.3. Khởi động lại máy chủ ADB

```python
from oiadb import MyADB
from oiadb.commands import basic

adb = MyADB()

# Khởi động lại máy chủ ADB
basic.kill_server()
basic.start_server()

# Đợi thiết bị kết nối
basic.wait_for_device()
print("Thiết bị đã kết nối!")
```

### 7.2. Quản lý ứng dụng

#### 7.2.1. Cài đặt và gỡ cài đặt ứng dụng

```python
from oiadb import MyADB
from oiadb.commands import apps

adb = MyADB()

# Cài đặt ứng dụng
apps.install("/path/to/app.apk")

# Kiểm tra ứng dụng đã cài đặt
if apps.is_app_installed("com.example.app"):
    print("Ứng dụng đã được cài đặt!")

# Gỡ cài đặt ứng dụng
apps.uninstall("com.example.app")
```

#### 7.2.2. Khởi động và dừng ứng dụng

```python
from oiadb import MyADB
from oiadb.commands import apps

adb = MyADB()

# Khởi động ứng dụng
apps.start_app("com.example.app")

# Dừng ứng dụng
apps.stop_app("com.example.app")

# Xóa dữ liệu ứng dụng
apps.clear_app_data("com.example.app")
```

#### 7.2.3. Lấy thông tin ứng dụng

```python
from oiadb import MyADB
from oiadb.commands import app_info

adb = MyADB()

# Lấy phiên bản ứng dụng
version = app_info.get_app_version("com.example.app")
print(f"Phiên bản: {version}")

# Lấy đường dẫn cài đặt ứng dụng
path = app_info.get_app_path("com.example.app")
print(f"Đường dẫn cài đặt: {path}")
```

### 7.3. Thao tác file

#### 7.3.1. Đẩy và lấy file

```python
from oiadb import MyADB
from oiadb.commands import file_ops

adb = MyADB()

# Đẩy file lên thiết bị
file_ops.push("/path/on/computer/file.txt", "/sdcard/file.txt")

# Lấy file từ thiết bị
file_ops.pull("/sdcard/file.txt", "/path/on/computer/downloaded_file.txt")
```

#### 7.3.2. Quản lý file và thư mục

```python
from oiadb import MyADB
from oiadb.commands import file_ops

adb = MyADB()

# Liệt kê file trong thư mục
files = file_ops.list_files("/sdcard")
print(f"Các file trong /sdcard: {files}")

# Kiểm tra file tồn tại
if file_ops.file_exists("/sdcard/file.txt"):
    print("File tồn tại trên thiết bị!")

# Tạo thư mục
file_ops.create_dir("/sdcard/my_folder")

# Sao chép file
file_ops.copy_file("/sdcard/file.txt", "/sdcard/my_folder/file_copy.txt")

# Di chuyển file
file_ops.move_file("/sdcard/file.txt", "/sdcard/moved_file.txt")

# Xóa file
file_ops.remove_file("/sdcard/moved_file.txt")

# Xóa thư mục
file_ops.remove_dir("/sdcard/my_folder")
```

#### 7.3.3. Quản lý quyền file

```python
from oiadb import MyADB
from oiadb.commands import file_ops

adb = MyADB()

# Lấy quyền file
permissions = file_ops.get_file_permissions("/sdcard/file.txt")
print(f"Quyền file: {permissions}")

# Đặt quyền file
file_ops.set_file_permissions("/sdcard/file.txt", "755")
```

### 7.4. Tương tác với thiết bị

#### 7.4.1. Thao tác chạm và vuốt

```python
from oiadb import MyADB
from oiadb.commands import interaction

adb = MyADB()

# Nhấn vào tọa độ
interaction.tap(500, 500)

# Nhấn giữ vào tọa độ
interaction.long_press(500, 500, duration=1000)

# Vuốt từ điểm này đến điểm khác
interaction.swipe(100, 500, 600, 500, duration=300)
```

#### 7.4.2. Nhập văn bản và phím

```python
from oiadb import MyADB
from oiadb.commands import interaction

adb = MyADB()

# Nhập văn bản
interaction.text_input("Hello World")

# Gửi sự kiện phím
interaction.key_event(4)  # 4 là mã phím Back

# Nhấn nút Back
interaction.back()

# Nhấn nút Home
interaction.home()

# Mở màn hình ứng dụng gần đây
interaction.recent_apps()
```

#### 7.4.3. Chụp ảnh màn hình

```python
from oiadb import MyADB
from oiadb.commands import interaction

adb = MyADB()

# Chụp ảnh màn hình
interaction.take_screenshot("/path/on/computer/screenshot.png")
```

### 7.5. Tương tác dựa trên hình ảnh

#### 7.5.1. Tìm và nhấp vào hình ảnh

```python
from oiadb import MyADB
from oiadb.commands import image_interaction

adb = MyADB()

# Tìm hình ảnh trên màn hình
result = image_interaction.find_image("/path/to/button.png", threshold=0.8)
if result:
    x, y, confidence = result
    print(f"Đã tìm thấy hình ảnh tại ({x}, {y}) với độ tương đồng {confidence}")
else:
    print("Không tìm thấy hình ảnh")

# Tìm và nhấp vào hình ảnh
if image_interaction.tap_image("/path/to/button.png", threshold=0.8):
    print("Đã nhấp vào hình ảnh thành công")
else:
    print("Không tìm thấy hình ảnh để nhấp")
```

#### 7.5.2. Đợi hình ảnh xuất hiện hoặc biến mất

```python
from oiadb import MyADB
from oiadb.commands import image_interaction

adb = MyADB()

# Đợi hình ảnh xuất hiện
result = image_interaction.wait_for_image(
    template_path="/path/to/button.png",
    timeout=10,  # Thời gian tối đa đợi (giây)
    interval=0.5,  # Khoảng thời gian giữa các lần tìm kiếm (giây)
    threshold=0.8
)
if result:
    print(f"Đã tìm thấy hình ảnh tại ({result[0]}, {result[1]}) sau khi đợi")
else:
    print("Hình ảnh không xuất hiện trong thời gian chờ")

# Đợi hình ảnh biến mất
if image_interaction.wait_until_image_disappears(
    template_path="/path/to/loading.png",
    timeout=30,
    interval=1.0,
    threshold=0.8
):
    print("Hình ảnh đã biến mất trong thời gian chờ")
else:
    print("Hình ảnh vẫn còn hiển thị sau thời gian chờ")
```

#### 7.5.3. Tương tác nâng cao với hình ảnh

```python
from oiadb import MyADB
from oiadb.commands import image_interaction

adb = MyADB()

# Kéo từ hình ảnh này đến hình ảnh khác
if image_interaction.drag_image_to_image(
    source_template_path="/path/to/source.png",
    target_template_path="/path/to/target.png",
    duration=800
):
    print("Đã kéo thành công từ nguồn đến đích")
else:
    print("Không thể kéo vì không tìm thấy một hoặc cả hai hình ảnh")

# Nhấn giữ vào hình ảnh
if image_interaction.long_press_image(
    template_path="/path/to/element.png",
    duration=1000
):
    print("Đã nhấn giữ vào hình ảnh thành công")
else:
    print("Không tìm thấy hình ảnh để nhấn giữ")

# Nhấp đúp vào hình ảnh
if image_interaction.double_tap_image(
    template_path="/path/to/element.png",
    tap_delay=0.1
):
    print("Đã nhấp đúp vào hình ảnh thành công")
else:
    print("Không tìm thấy hình ảnh để nhấp đúp")
```

#### 7.5.4. Xử lý các điều kiện màn hình khác nhau

```python
from oiadb import MyADB
from oiadb.commands import image_interaction

adb = MyADB()

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

# Tìm hình ảnh mờ
result_blurry = image_interaction.find_image(
    template_path="/path/to/template.png",
    threshold=0.7,  # Ngưỡng thấp hơn cho hình ảnh mờ
    scale_range=(0.8, 1.2),
    scale_steps=5,
    use_canny=True  # Sử dụng phát hiện cạnh Canny cho hình ảnh mờ
)

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

### 7.6. Xử lý log và debug

#### 7.6.1. Xem và lọc logcat

```python
from oiadb import MyADB
from oiadb.commands import logs

adb = MyADB()

# Xóa logcat
logs.clear_logcat()

# Xem logcat
logcat_output = logs.logcat("-v time")
print(f"Logcat: {logcat_output}")

# Lọc logcat
filtered_log = logs.filter_logcat(tag="ActivityManager", priority="E")
print(f"Logcat đã lọc: {filtered_log}")

# Lưu logcat vào file
logs.logcat_to_file("/path/on/computer/logcat.txt")
```

#### 7.6.2. Tạo báo cáo lỗi

```python
from oiadb import MyADB
from oiadb.commands import logs

adb = MyADB()

# Tạo báo cáo lỗi
logs.bugreport("/path/on/computer/bugreport.zip")
```

#### 7.6.3. Phân tích UI

```python
from oiadb import MyADB
from oiadb.utils import advanced

adb = MyADB()

# Xuất UI thành XML
xml = advanced.dump_ui_xml("/path/on/computer/ui.xml")

# Tìm view theo text
views = advanced.find_view_by_text("Login")
print(f"Các view có text 'Login': {views}")

# Tìm view theo ID
views = advanced.find_view_by_id("com.example.app:id/login_button")
print(f"Các view có ID 'login_button': {views}")
```

## 8. Ví dụ thực tế

### 8.1. Tự động cài đặt và chạy ứng dụng

```python
from oiadb import MyADB
from oiadb.commands import apps, interaction
import time

def install_and_run_app(apk_path, package_name):
    adb = MyADB()
    
    # Kiểm tra ứng dụng đã cài đặt chưa
    if apps.is_app_installed(package_name):
        print(f"Ứng dụng {package_name} đã được cài đặt, gỡ cài đặt trước...")
        apps.uninstall(package_name)
    
    # Cài đặt ứng dụng
    print(f"Đang cài đặt ứng dụng từ {apk_path}...")
    if apps.install(apk_path):
        print("Cài đặt thành công!")
    else:
        print("Cài đặt thất bại!")
        return False
    
    # Khởi động ứng dụng
    print(f"Đang khởi động ứng dụng {package_name}...")
    apps.start_app(package_name)
    
    # Đợi ứng dụng khởi động
    time.sleep(3)
    
    # Chụp ảnh màn hình
    screenshot_path = f"/path/on/computer/{package_name}_screenshot.png"
    interaction.take_screenshot(screenshot_path)
    print(f"Đã chụp ảnh màn hình và lưu vào {screenshot_path}")
    
    return True

# Sử dụng hàm
install_and_run_app("/path/to/app.apk", "com.example.app")
```

### 8.2. Tự động kiểm thử UI

```python
from oiadb import MyADB
from oiadb.commands import apps, interaction
from oiadb.utils import advanced
import time

def test_login_functionality(package_name, username, password):
    adb = MyADB()
    
    # Khởi động ứng dụng
    print(f"Đang khởi động ứng dụng {package_name}...")
    apps.start_app(package_name)
    
    # Đợi ứng dụng khởi động
    time.sleep(3)
    
    # Tìm trường username
    username_views = advanced.find_view_by_id(f"{package_name}:id/username")
    if not username_views:
        print("Không tìm thấy trường username!")
        return False
    
    # Lấy tọa độ trường username
    username_props = advanced.get_view_properties(username_views[0])
    username_x = int(username_props.get("bounds").get("left")) + 100
    username_y = int(username_props.get("bounds").get("top")) + 20
    
    # Nhấp vào trường username
    interaction.tap(username_x, username_y)
    time.sleep(1)
    
    # Nhập username
    interaction.text_input(username)
    time.sleep(1)
    
    # Tìm trường password
    password_views = advanced.find_view_by_id(f"{package_name}:id/password")
    if not password_views:
        print("Không tìm thấy trường password!")
        return False
    
    # Lấy tọa độ trường password
    password_props = advanced.get_view_properties(password_views[0])
    password_x = int(password_props.get("bounds").get("left")) + 100
    password_y = int(password_props.get("bounds").get("top")) + 20
    
    # Nhấp vào trường password
    interaction.tap(password_x, password_y)
    time.sleep(1)
    
    # Nhập password
    interaction.text_input(password)
    time.sleep(1)
    
    # Tìm nút đăng nhập
    login_views = advanced.find_view_by_text("Login")
    if not login_views:
        print("Không tìm thấy nút đăng nhập!")
        return False
    
    # Lấy tọa độ nút đăng nhập
    login_props = advanced.get_view_properties(login_views[0])
    login_x = int(login_props.get("bounds").get("left")) + 50
    login_y = int(login_props.get("bounds").get("top")) + 20
    
    # Nhấp vào nút đăng nhập
    interaction.tap(login_x, login_y)
    time.sleep(3)
    
    # Kiểm tra đăng nhập thành công
    home_views = advanced.find_view_by_text("Welcome")
    if home_views:
        print("Đăng nhập thành công!")
        return True
    else:
        print("Đăng nhập thất bại!")
        return False

# Sử dụng hàm
test_login_functionality("com.example.app", "testuser", "password123")
```

### 8.3. Tự động hóa dựa trên nhận diện hình ảnh

```python
from oiadb import MyADB
from oiadb.commands import apps, image_interaction
import time

def automate_with_image_recognition(package_name):
    adb = MyADB()
    
    # Khởi động ứng dụng
    print(f"Đang khởi động ứng dụng {package_name}...")
    apps.start_app(package_name)
    
    # Đợi ứng dụng khởi động
    time.sleep(3)
    
    # Đợi và nhấp vào nút đăng nhập
    print("Đang tìm nút đăng nhập...")
    if image_interaction.wait_and_tap_image(
        template_path="/path/to/login_button.png",
        timeout=10,
        threshold=0.8
    ):
        print("Đã nhấp vào nút đăng nhập!")
    else:
        print("Không tìm thấy nút đăng nhập!")
        return False
    
    # Đợi màn hình đăng nhập xuất hiện
    print("Đang đợi màn hình đăng nhập xuất hiện...")
    if not image_interaction.wait_for_image(
        template_path="/path/to/username_field.png",
        timeout=10,
        threshold=0.8
    ):
        print("Không tìm thấy màn hình đăng nhập!")
        return False
    
    # Nhấp vào trường username
    print("Đang nhấp vào trường username...")
    if image_interaction.tap_image("/path/to/username_field.png", threshold=0.8):
        # Nhập username
        adb.run("shell input text 'testuser'")
    else:
        print("Không tìm thấy trường username!")
        return False
    
    # Nhấp vào trường password
    print("Đang nhấp vào trường password...")
    if image_interaction.tap_image("/path/to/password_field.png", threshold=0.8):
        # Nhập password
        adb.run("shell input text 'password123'")
    else:
        print("Không tìm thấy trường password!")
        return False
    
    # Nhấp vào nút đăng nhập
    print("Đang nhấp vào nút đăng nhập...")
    if not image_interaction.tap_image("/path/to/submit_button.png", threshold=0.8):
        print("Không tìm thấy nút đăng nhập!")
        return False
    
    # Đợi biểu tượng tải xuất hiện và biến mất
    print("Đang đợi quá trình đăng nhập hoàn tất...")
    if image_interaction.wait_for_image("/path/to/loading_icon.png", timeout=5, threshold=0.7):
        # Đợi biểu tượng tải biến mất
        if not image_interaction.wait_until_image_disappears("/path/to/loading_icon.png", timeout=30, threshold=0.7):
            print("Quá trình đăng nhập mất quá nhiều thời gian!")
            return False
    
    # Xác minh đã đăng nhập thành công
    print("Đang xác minh đăng nhập thành công...")
    if image_interaction.is_image_present("/path/to/home_screen.png", threshold=0.8):
        print("Đăng nhập thành công!")
        return True
    else:
        print("Không thể xác minh đăng nhập thành công!")
        return False

# Sử dụng hàm
automate_with_image_recognition("com.example.app")
```

## 9. Xử lý lỗi và gỡ rối

### 9.1. Xử lý ngoại lệ

```python
from oiadb import MyADB
from oiadb.exceptions import ADBError, DeviceNotFoundError, CommandError

try:
    adb = MyADB()
    result = adb.run("invalid command")
except DeviceNotFoundError:
    print("Không tìm thấy thiết bị! Hãy kết nối thiết bị và thử lại.")
except CommandError as e:
    print(f"Lỗi khi chạy lệnh: {e}")
except ADBError as e:
    print(f"Lỗi ADB: {e}")
```

### 9.2. Gỡ rối kết nối ADB

```python
from oiadb import MyADB
from oiadb.commands import basic
from oiadb.utils import runner

# Kiểm tra đường dẫn ADB
adb_path = runner.get_adb_path()
print(f"Đường dẫn ADB: {adb_path}")

# Kiểm tra phiên bản ADB
version = basic.adb_version()
print(f"Phiên bản ADB: {version}")

# Khởi động lại máy chủ ADB
basic.kill_server()
basic.start_server()

# Liệt kê thiết bị đã kết nối
adb = MyADB()
devices = adb.get_devices()
print(f"Thiết bị đã kết nối: {devices}")
```

### 9.3. Gỡ rối nhận diện hình ảnh

```python
from oiadb import MyADB
from oiadb.commands import interaction, image_interaction
from oiadb.utils.image_recognition import ImageRecognition
import cv2
import numpy as np
import os

def debug_image_recognition(template_path):
    adb = MyADB()
    image_rec = ImageRecognition(adb)
    
    # Tạo thư mục debug
    debug_dir = "/path/on/computer/debug"
    os.makedirs(debug_dir, exist_ok=True)
    
    # Chụp ảnh màn hình
    screenshot_path = f"{debug_dir}/screenshot.png"
    interaction.take_screenshot(screenshot_path)
    print(f"Đã chụp ảnh màn hình và lưu vào {screenshot_path}")
    
    # Tải ảnh màn hình và mẫu
    screenshot = image_rec.load_template(screenshot_path)
    template = image_rec.load_template(template_path)
    
    # Lưu ảnh mẫu để kiểm tra
    template_debug_path = f"{debug_dir}/template.png"
    cv2.imwrite(template_debug_path, template)
    
    # Thử với các ngưỡng khác nhau
    thresholds = [0.9, 0.8, 0.7, 0.6, 0.5]
    for threshold in thresholds:
        # Tìm mẫu với ngưỡng hiện tại
        result = image_rec.find_template(screenshot, template, threshold=threshold)
        
        # Tạo bản sao ảnh màn hình để vẽ kết quả
        debug_image = screenshot.copy()
        
        if result:
            x, y, confidence = result
            print(f"Ngưỡng {threshold}: Đã tìm thấy tại ({x}, {y}) với độ tương đồng {confidence}")
            
            # Vẽ hình chữ nhật xung quanh kết quả
            h, w = template.shape[:2]
            cv2.rectangle(debug_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(debug_image, f"{confidence:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        else:
            print(f"Ngưỡng {threshold}: Không tìm thấy")
        
        # Lưu ảnh debug
        debug_image_path = f"{debug_dir}/result_threshold_{threshold}.png"
        cv2.imwrite(debug_image_path, debug_image)
        print(f"Đã lưu ảnh debug vào {debug_image_path}")
    
    # Thử với ảnh xám và phát hiện cạnh
    for use_gray in [True, False]:
        for use_canny in [True, False]:
            result = image_rec.find_template(screenshot, template, threshold=0.7, use_gray=use_gray, use_canny=use_canny)
            
            mode = f"gray_{use_gray}_canny_{use_canny}"
            if result:
                x, y, confidence = result
                print(f"Chế độ {mode}: Đã tìm thấy tại ({x}, {y}) với độ tương đồng {confidence}")
            else:
                print(f"Chế độ {mode}: Không tìm thấy")
    
    # Thử với nhiều tỷ lệ
    result = image_rec.find_template_with_scale(screenshot, template, threshold=0.7, scale_range=(0.5, 1.5), scale_steps=10)
    if result:
        x, y, confidence, scale = result
        print(f"Tỷ lệ: Đã tìm thấy tại ({x}, {y}) với độ tương đồng {confidence} và tỷ lệ {scale}")
    else:
        print("Tỷ lệ: Không tìm thấy")

# Sử dụng hàm
debug_image_recognition("/path/to/button.png")
```

## 10. Thực hành tốt nhất

### 10.1. Tối ưu hóa hiệu suất

1. **Giới hạn vùng tìm kiếm**: Sử dụng tham số `region` để chỉ tìm trong một phần của màn hình
2. **Sử dụng ảnh xám**: Đặt `use_gray=True` để tăng tốc độ tìm kiếm
3. **Giảm số bước tỷ lệ và góc xoay**: Chỉ sử dụng nhiều bước khi cần thiết
4. **Tối ưu hóa hình ảnh mẫu**: Sử dụng hình ảnh mẫu nhỏ nhưng đủ đặc trưng
5. **Sử dụng timeout hợp lý**: Đặt giá trị timeout phù hợp với tốc độ của ứng dụng

### 10.2. Tổ chức mã nguồn

1. **Tạo lớp wrapper**: Tạo lớp wrapper cho ứng dụng cụ thể để tái sử dụng mã
2. **Tổ chức hình ảnh mẫu**: Lưu trữ hình ảnh mẫu trong một thư mục riêng và đặt tên có ý nghĩa
3. **Tách biệt logic**: Tách biệt logic kiểm thử và logic tự động hóa
4. **Sử dụng hằng số**: Định nghĩa các hằng số cho đường dẫn, tọa độ, v.v.
5. **Ghi log**: Sử dụng logging để ghi lại các hoạt động và lỗi

### 10.3. Xử lý lỗi

1. **Kiểm tra kết quả**: Luôn kiểm tra kết quả trả về trước khi thực hiện các hành động tiếp theo
2. **Sử dụng try-except**: Bắt và xử lý các ngoại lệ có thể xảy ra
3. **Thêm timeout**: Sử dụng timeout để tránh treo khi đợi các sự kiện
4. **Kiểm tra điều kiện**: Kiểm tra các điều kiện trước khi thực hiện các hành động
5. **Thử lại**: Thực hiện thử lại khi gặp lỗi tạm thời

### 10.4. Tạo kịch bản tự động hóa mạnh mẽ

1. **Sử dụng nhận diện hình ảnh**: Ưu tiên sử dụng nhận diện hình ảnh thay vì tọa độ cố định
2. **Đợi phần tử**: Luôn đợi phần tử xuất hiện trước khi tương tác
3. **Xác minh trạng thái**: Xác minh trạng thái sau mỗi hành động
4. **Xử lý các trường hợp đặc biệt**: Xử lý các trường hợp đặc biệt như thông báo, hộp thoại, v.v.
5. **Dọn dẹp**: Dọn dẹp sau khi hoàn thành (đóng ứng dụng, xóa dữ liệu tạm, v.v.)

## 11. Tham khảo

### 11.1. Tài liệu ADB

- [Android Debug Bridge (ADB)](https://developer.android.com/studio/command-line/adb)
- [ADB Shell Commands](https://developer.android.com/studio/command-line/adb#shellcommands)
- [UI Automator](https://developer.android.com/training/testing/ui-automator)

### 11.2. Tài liệu OpenCV

- [OpenCV Documentation](https://docs.opencv.org/)
- [Template Matching](https://docs.opencv.org/4.x/d4/dc6/tutorial_py_template_matching.html)
- [Feature Detection](https://docs.opencv.org/4.x/d7/d66/tutorial_feature_detection.html)

### 11.3. Tài liệu Python

- [Python Documentation](https://docs.python.org/3/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Subprocess Module](https://docs.python.org/3/library/subprocess.html)

### 11.4. Tài liệu OIADB

- [GitHub Repository](https://github.com/tiendung102k3/oiadb)
- [PyPI Package](https://pypi.org/project/oiadb/)
- [Image Recognition Documentation](image_recognition_documentation.md)
