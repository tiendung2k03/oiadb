"""
Ví dụ cơ bản về cách sử dụng thư viện OIADB.
"""

from oiadb import MyADB
from oiadb.commands import interaction, device_info, apps

def basic_usage_example():
    """
    Ví dụ cơ bản về cách sử dụng thư viện OIADB.
    """
    # Khởi tạo ADB
    adb = MyADB()
    
    # Liệt kê các thiết bị đã kết nối
    devices = adb.get_devices()
    print(f"Các thiết bị đã kết nối: {devices}")
    
    # Lấy thông tin thiết bị
    model = device_info.get_device_model()
    android_version = device_info.get_android_version()
    screen_resolution = device_info.get_screen_resolution()
    
    print(f"Model thiết bị: {model}")
    print(f"Phiên bản Android: {android_version}")
    print(f"Độ phân giải màn hình: {screen_resolution[0]}x{screen_resolution[1]}")
    
    # Chụp ảnh màn hình
    screenshot_path = "./screenshot.png"
    interaction.take_screenshot(screenshot_path)
    print(f"Đã chụp ảnh màn hình và lưu vào {screenshot_path}")
    
    # Liệt kê ứng dụng đã cài đặt
    installed_apps = apps.list_installed_apps()
    print(f"Số lượng ứng dụng đã cài đặt: {len(installed_apps)}")
    print(f"5 ứng dụng đầu tiên: {installed_apps[:5]}")
    
    # Thực hiện một số thao tác cơ bản
    print("Nhấn nút Home...")
    interaction.home()
    
    print("Mở màn hình ứng dụng gần đây...")
    interaction.recent_apps()
    
    print("Nhấn nút Back...")
    interaction.back()
    
    # Chạy lệnh ADB tùy chỉnh
    result = adb.run("shell dumpsys battery")
    print(f"Thông tin pin:\n{result}")

if __name__ == "__main__":
    basic_usage_example()
