"""
Ví dụ về quản lý ứng dụng với thư viện OIADB.
"""

from oiadb import MyADB
from oiadb.commands import apps, app_info
import time

def app_management_example():
    """
    Ví dụ về cách quản lý ứng dụng với OIADB.
    """
    # Khởi tạo ADB
    adb = MyADB()
    
    # Đường dẫn đến file APK (thay thế bằng đường dẫn thực tế)
    apk_path = "./example_app.apk"
    package_name = "com.example.app"
    
    # Kiểm tra ứng dụng đã cài đặt chưa
    if apps.is_app_installed(package_name):
        print(f"Ứng dụng {package_name} đã được cài đặt")
        
        # Lấy thông tin phiên bản
        version = app_info.get_app_version(package_name)
        print(f"Phiên bản hiện tại: {version}")
        
        # Lấy đường dẫn cài đặt
        app_path = app_info.get_app_path(package_name)
        print(f"Đường dẫn cài đặt: {app_path}")
        
        # Khởi động ứng dụng
        print(f"Đang khởi động ứng dụng {package_name}...")
        apps.start_app(package_name)
        
        # Đợi ứng dụng khởi động
        time.sleep(3)
        
        # Dừng ứng dụng
        print(f"Đang dừng ứng dụng {package_name}...")
        apps.stop_app(package_name)
        
        # Xóa dữ liệu ứng dụng
        print(f"Đang xóa dữ liệu ứng dụng {package_name}...")
        apps.clear_app_data(package_name)
        
        # Gỡ cài đặt ứng dụng
        print(f"Đang gỡ cài đặt ứng dụng {package_name}...")
        apps.uninstall(package_name)
        print(f"Đã gỡ cài đặt ứng dụng {package_name}")
    else:
        print(f"Ứng dụng {package_name} chưa được cài đặt")
        
        # Cài đặt ứng dụng (bỏ comment nếu có file APK thực tế)
        # print(f"Đang cài đặt ứng dụng từ {apk_path}...")
        # if apps.install(apk_path):
        #     print("Cài đặt thành công!")
        # else:
        #     print("Cài đặt thất bại!")
    
    # Liệt kê các ứng dụng hệ thống
    system_apps = [app for app in apps.list_installed_apps() if app.startswith("com.android") or app.startswith("com.google")]
    print(f"Số lượng ứng dụng hệ thống: {len(system_apps)}")
    print(f"5 ứng dụng hệ thống đầu tiên: {system_apps[:5]}")
    
    # Liệt kê các ứng dụng người dùng
    user_apps = [app for app in apps.list_installed_apps() if not (app.startswith("com.android") or app.startswith("com.google"))]
    print(f"Số lượng ứng dụng người dùng: {len(user_apps)}")
    print(f"5 ứng dụng người dùng đầu tiên: {user_apps[:5]}")

if __name__ == "__main__":
    app_management_example()
