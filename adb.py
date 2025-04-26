"""
Lớp chính của thư viện My ADB Lib.
"""

import os
import logging
import subprocess
from typing import Optional, List, Dict, Any, Union

from .exceptions import (
    ADBError, ADBCommandError, DeviceNotFoundError, 
    DeviceConnectionError, PackageNotFoundError,
    InstallationError, UninstallationError, FileOperationError
)
from .utils.advanced import CommandResult, ResultCache, DeviceMonitor, AsyncCommandExecutor

# Thiết lập logging
logger = logging.getLogger('my_adb_lib')

class MyADB:
    """
    Lớp chính để tương tác với ADB (Android Debug Bridge).
    
    Attributes:
        device_id (str): ID của thiết bị Android để tương tác
        cache_enabled (bool): Bật/tắt cache kết quả lệnh
        timeout (int): Thời gian chờ tối đa cho các lệnh (giây)
    """
    
    def __init__(self, device_id: Optional[str] = None, cache_enabled: bool = True, 
                 timeout: int = 30, adb_path: Optional[str] = None):
        """
        Khởi tạo đối tượng MyADB.
        
        Args:
            device_id: ID của thiết bị Android (serial number)
            cache_enabled: Bật/tắt cache kết quả lệnh
            timeout: Thời gian chờ tối đa cho các lệnh (giây)
            adb_path: Đường dẫn tùy chỉnh đến executable ADB
        """
        self.device_id = device_id
        self.timeout = timeout
        self.cache_enabled = cache_enabled
        self.adb_path = adb_path or "adb"
        
        # Khởi tạo cache và executor
        self._cache = ResultCache() if cache_enabled else None
        self._async_executor = AsyncCommandExecutor()
        
        # Kiểm tra ADB đã được cài đặt
        self._check_adb_installed()
        
        # Kiểm tra thiết bị nếu đã chỉ định
        if device_id:
            self._check_device()
    
    def _check_adb_installed(self) -> None:
        """
        Kiểm tra ADB đã được cài đặt và có thể truy cập.
        
        Raises:
            ADBError: Nếu ADB không được cài đặt hoặc không thể truy cập
        """
        try:
            result = subprocess.run(
                [self.adb_path, "version"], 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE,
                text=True,
                timeout=self.timeout
            )
            if result.returncode != 0:
                raise ADBError(f"Không thể chạy ADB. Lỗi: {result.stderr}")
            logger.debug(f"ADB version: {result.stdout.splitlines()[0]}")
        except FileNotFoundError:
            raise ADBError("ADB không được cài đặt hoặc không có trong PATH")
        except Exception as e:
            raise ADBError(f"Lỗi khi kiểm tra ADB: {str(e)}")
    
    def _check_device(self) -> None:
        """
        Kiểm tra thiết bị đã được kết nối.
        
        Raises:
            DeviceNotFoundError: Nếu thiết bị không được tìm thấy
        """
        devices = self.get_devices_list()
        if self.device_id not in devices:
            raise DeviceNotFoundError(self.device_id)
    
    def run(self, command: str, use_cache: bool = True) -> str:
        """
        Chạy lệnh ADB và trả về kết quả dưới dạng chuỗi.
        
        Args:
            command: Lệnh ADB cần thực thi (không bao gồm "adb")
            use_cache: Có sử dụng cache hay không
            
        Returns:
            Kết quả lệnh dưới dạng chuỗi
            
        Raises:
            ADBCommandError: Nếu lệnh thất bại
        """
        # Kiểm tra cache
        cache_key = f"{self.device_id}:{command}" if self.device_id else command
        if self.cache_enabled and use_cache:
            cached_result = self._cache.get(cache_key)
            if cached_result:
                logger.debug(f"Using cached result for command: {command}")
                return cached_result
        
        # Tạo lệnh đầy đủ
        full_command = [self.adb_path]
        if self.device_id:
            full_command.extend(["-s", self.device_id])
        full_command.extend(command.split())
        
        # Thực thi lệnh
        try:
            logger.debug(f"Executing command: {' '.join(full_command)}")
            result = subprocess.run(
                full_command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=self.timeout
            )
            
            if result.returncode != 0:
                raise ADBCommandError(
                    command=' '.join(full_command),
                    error_message=result.stderr,
                    return_code=result.returncode
                )
            
            # Lưu vào cache nếu thành công
            if self.cache_enabled and use_cache:
                self._cache.set(cache_key, result.stdout)
            
            return result.stdout
        
        except subprocess.TimeoutExpired:
            raise ADBCommandError(
                command=' '.join(full_command),
                error_message=f"Command timed out after {self.timeout} seconds"
            )
        except Exception as e:
            if isinstance(e, ADBCommandError):
                raise
            raise ADBCommandError(
                command=' '.join(full_command),
                error_message=str(e)
            )
    
    def run_async(self, command: str, callback=None) -> str:
        """
        Chạy lệnh ADB bất đồng bộ.
        
        Args:
            command: Lệnh ADB cần thực thi (không bao gồm "adb")
            callback: Hàm callback khi lệnh hoàn thành
            
        Returns:
            ID của lệnh đang chạy
        """
        # Tạo ID duy nhất cho lệnh
        import uuid
        command_id = str(uuid.uuid4())
        
        # Tạo lệnh đầy đủ
        full_command = [self.adb_path]
        if self.device_id:
            full_command.extend(["-s", self.device_id])
        full_command.extend(command.split())
        
        # Thực thi lệnh bất đồng bộ
        self._async_executor.execute(
            command_id=command_id,
            command=full_command,
            callback=callback,
            timeout=self.timeout
        )
        
        return command_id
    
    def get_async_result(self, command_id: str) -> Optional[CommandResult]:
        """
        Lấy kết quả của lệnh bất đồng bộ.
        
        Args:
            command_id: ID của lệnh
            
        Returns:
            CommandResult hoặc None nếu lệnh chưa hoàn thành
        """
        return self._async_executor.get_result(command_id)
    
    def is_async_running(self, command_id: str) -> bool:
        """
        Kiểm tra xem lệnh bất đồng bộ có đang chạy không.
        
        Args:
            command_id: ID của lệnh
            
        Returns:
            True nếu lệnh đang chạy, False nếu không
        """
        return self._async_executor.is_running(command_id)
    
    def kill_async(self, command_id: str) -> bool:
        """
        Hủy lệnh bất đồng bộ đang chạy.
        
        Args:
            command_id: ID của lệnh
            
        Returns:
            True nếu lệnh đã bị hủy thành công, False nếu không
        """
        return self._async_executor.kill(command_id)
    
    def clear_cache(self) -> None:
        """Xóa toàn bộ cache."""
        if self.cache_enabled and self._cache:
            self._cache.clear()
    
    def get_devices(self) -> str:
        """
        Liệt kê các thiết bị kết nối dưới dạng chuỗi.
        
        Returns:
            Chuỗi chứa danh sách thiết bị
        """
        return self.run("devices", use_cache=False)
    
    def get_devices_list(self) -> List[str]:
        """
        Liệt kê các thiết bị kết nối dưới dạng danh sách.
        
        Returns:
            Danh sách các ID thiết bị
        """
        output = self.get_devices()
        devices = []
        
        for line in output.splitlines()[1:]:  # Bỏ qua dòng tiêu đề
            if not line.strip():
                continue
            
            parts = line.split('\t')
            if len(parts) >= 2 and parts[1] == 'device':
                devices.append(parts[0])
        
        return devices
    
    def reboot_device(self) -> str:
        """
        Khởi động lại thiết bị.
        
        Returns:
            Kết quả lệnh
        """
        return self.run("reboot")
    
    def reboot_to_recovery(self) -> str:
        """
        Khởi động lại thiết bị vào chế độ recovery.
        
        Returns:
            Kết quả lệnh
        """
        return self.run("reboot recovery")
    
    def reboot_to_bootloader(self) -> str:
        """
        Khởi động lại thiết bị vào chế độ bootloader.
        
        Returns:
            Kết quả lệnh
        """
        return self.run("reboot bootloader")
    
    def install_app(self, apk_path: str, replace: bool = False, 
                   grant_permissions: bool = False) -> str:
        """
        Cài đặt ứng dụng từ đường dẫn .apk.
        
        Args:
            apk_path: Đường dẫn đến file APK
            replace: Thay thế ứng dụng nếu đã tồn tại
            grant_permissions: Tự động cấp tất cả quyền cho ứng dụng
            
        Returns:
            Kết quả lệnh
            
        Raises:
            InstallationError: Nếu cài đặt thất bại
        """
        if not os.path.exists(apk_path):
            raise InstallationError(apk_path, "File APK không tồn tại")
        
        options = []
        if replace:
            options.append("-r")
        if grant_permissions:
            options.append("-g")
        
        try:
            return self.run(f"install {' '.join(options)} {apk_path}")
        except ADBCommandError as e:
            raise InstallationError(apk_path, e.error_message)
    
    def uninstall_app(self, package_name: str, keep_data: bool = False) -> str:
        """
        Gỡ cài đặt ứng dụng theo tên package.
        
        Args:
            package_name: Tên package của ứng dụng
            keep_data: Giữ lại dữ liệu và cache
            
        Returns:
            Kết quả lệnh
            
        Raises:
            UninstallationError: Nếu gỡ cài đặt thất bại
        """
        options = ["-k"] if keep_data else []
        
        try:
            return self.run(f"uninstall {' '.join(options)} {package_name}")
        except ADBCommandError as e:
            raise UninstallationError(package_name, e.error_message)
    
    def push_file(self, local_path: str, remote_path: str) -> str:
        """
        Đẩy file từ máy tính vào thiết bị.
        
        Args:
            local_path: Đường dẫn file trên máy tính
            remote_path: Đường dẫn đích trên thiết bị
            
        Returns:
            Kết quả lệnh
            
        Raises:
            FileOperationError: Nếu thao tác thất bại
        """
        if not os.path.exists(local_path):
            raise FileOperationError("push", local_path, remote_path, "File nguồn không tồn tại")
        
        try:
            return self.run(f"push {local_path} {remote_path}")
        except ADBCommandError as e:
            raise FileOperationError("push", local_path, remote_path, e.error_message)
    
    def pull_file(self, remote_path: str, local_path: str) -> str:
        """
        Lấy file từ thiết bị về máy tính.
        
        Args:
            remote_path: Đường dẫn file trên thiết bị
            local_path: Đường dẫn đích trên máy tính
            
        Returns:
            Kết quả lệnh
            
        Raises:
            FileOperationError: Nếu thao tác thất bại
        """
        try:
            return self.run(f"pull {remote_path} {local_path}")
        except ADBCommandError as e:
            raise FileOperationError("pull", remote_path, local_path, e.error_message)
    
    def get_device_info(self) -> Dict[str, str]:
        """
        Lấy thông tin thiết bị.
        
        Returns:
            Dictionary chứa thông tin thiết bị
        """
        try:
            output = self.run("shell getprop")
            properties = {}
            
            for line in output.splitlines():
                line = line.strip()
                if not line or ': ' not in line:
                    continue
                
                key, value = line.split(': ', 1)
                key = key.strip('[]')
                value = value.strip('[]')
                properties[key] = value
            
            return properties
        except ADBCommandError as e:
            logger.error(f"Error getting device info: {e}")
            return {}
    
    def start_app(self, package_name: str, activity: Optional[str] = None) -> str:
        """
        Khởi động ứng dụng.
        
        Args:
            package_name: Tên package của ứng dụng
            activity: Tên activity để khởi động (tùy chọn)
            
        Returns:
            Kết quả lệnh
        """
        if activity:
            return self.run(f"shell am start -n {package_name}/{activity}")
        else:
            return self.run(f"shell monkey -p {package_name} -c android.intent.category.LAUNCHER 1")
    
    def stop_app(self, package_name: str) -> str:
        """
        Dừng ứng dụng.
        
        Args:
            package_name: Tên package của ứng dụng
            
        Returns:
            Kết quả lệnh
        """
        return self.run(f"shell am force-stop {package_name}")
    
    def clear_app_data(self, package_name: str) -> str:
        """
        Xóa dữ liệu ứng dụng.
        
        Args:
            package_name: Tên package của ứng dụng
            
        Returns:
            Kết quả lệnh
        """
        return self.run(f"shell pm clear {package_name}")
    
    def get_app_version(self, package_name: str) -> str:
        """
        Lấy phiên bản của ứng dụng.
        
        Args:
            package_name: Tên package của ứng dụng
            
        Returns:
            Phiên bản ứng dụng
            
        Raises:
            PackageNotFoundError: Nếu package không tồn tại
        """
        try:
            output = self.run(f"shell dumpsys package {package_name}")
            for line in output.splitlines():
                if "versionName" in line:
                    return line.split("=", 1)[1].strip()
            
            raise PackageNotFoundError(package_name)
        except ADBCommandError:
            raise PackageNotFoundError(package_name)
    
    def is_app_installed(self, package_name: str) -> bool:
        """
        Kiểm tra xem ứng dụng đã được cài đặt chưa.
        
        Args:
            package_name: Tên package của ứng dụng
            
        Returns:
            True nếu ứng dụng đã được cài đặt, False nếu không
        """
        try:
            output = self.run(f"shell pm list packages {package_name}")
            return package_name in output
        except ADBCommandError:
            return False
    
    def take_screenshot(self, output_path: str) -> str:
        """
        Chụp ảnh màn hình thiết bị.
        
        Args:
            output_path: Đường dẫn lưu ảnh
            
        Returns:
            Kết quả lệnh
        """
        remote_path = "/sdcard/screenshot.png"
        self.run(f"shell screencap -p {remote_path}")
        result = self.pull_file(remote_path, output_path)
        self.run(f"shell rm {remote_path}")
        return result
    
    def record_screen(self, output_path: str, time_limit: int = 180, 
                     size: Optional[str] = None, bit_rate: Optional[int] = None) -> str:
        """
        Quay video màn hình thiết bị.
        
        Args:
            output_path: Đường dẫn lưu video
            time_limit: Giới hạn thời gian quay (giây)
            size: Kích thước video (ví dụ: "1280x720")
            bit_rate: Bit rate (ví dụ: 4000000 cho 4Mbps)
            
        Returns:
            ID của lệnh đang chạy
        """
        remote_path = "/sdcard/screenrecord.mp4"
        
        command = f"shell screenrecord"
        if time_limit:
            command += f" --time-limit {time_limit}"
        if size:
            command += f" --size {size}"
        if bit_rate:
            command += f" --bit-rate {bit_rate}"
        command += f" {remote_path}"
        
        def callback(result):
            if result.success:
                try:
                    self.pull_file(remote_path, output_path)
                    self.run(f"shell rm {remote_path}")
                except Exception as e:
                    logger.error(f"Error saving screen recording: {str(e)}")
        
        return self.run_async(command, callback)
    
    def tap(self, x: int, y: int) -> str:
        """
        Nhấn vào vị trí cụ thể trên màn hình.
        
        Args:
            x: Tọa độ X
            y: Tọa độ Y
            
        Returns:
            Kết quả lệnh
        """
        return self.run(f"shell input tap {x} {y}")
    
    def swipe(self, x1: int, y1: int, x2: int, y2: int, duration: int = 300) -> str:
        """
        Vuốt từ vị trí này đến vị trí khác.
        
        Args:
            x1: Tọa độ X bắt đầu
            y1: Tọa độ Y bắt đầu
            x2: Tọa độ X kết thúc
            y2: Tọa độ Y kết thúc
            duration: Thời gian vuốt (ms)
            
        Returns:
            Kết quả lệnh
        """
        return self.run(f"shell input swipe {x1} {y1} {x2} {y2} {duration}")
    
    def input_text(self, text: str) -> str:
        """
        Nhập văn bản.
        
        Args:
            text: Văn bản cần nhập
            
        Returns:
            Kết quả lệnh
        """
        # Thay thế các ký tự đặc biệt
        text = text.replace(" ", "%s").replace("'", "\\'").replace("\"", "\\\"")
        return self.run(f"shell input text '{text}'")
    
    def press_key(self, key_code: int) -> str:
        """
        Nhấn phím.
        
        Args:
            key_code: Mã phím
            
        Returns:
            Kết quả lệnh
        """
        return self.run(f"shell input keyevent {key_code}")
    
    def press_back(self) -> str:
        """
        Nhấn nút Back.
        
        Returns:
            Kết quả lệnh
        """
        return self.press_key(4)
    
    def press_home(self) -> str:
        """
        Nhấn nút Home.
        
        Returns:
            Kết quả lệnh
        """
        return self.press_key(3)
    
    def press_power(self) -> str:
        """
        Nhấn nút Power.
        
        Returns:
            Kết quả lệnh
        """
        return self.press_key(26)
    
    def get_logcat(self, options: str = "") -> str:
        """
        Lấy log từ thiết bị.
        
        Args:
            options: Các tùy chọn logcat
            
        Returns:
            Kết quả lệnh
        """
        return self.run(f"logcat {options}")
    
    def clear_logcat(self) -> str:
        """
        Xóa buffer logcat.
        
        Returns:
            Kết quả lệnh
        """
        return self.run("logcat -c")
    
    def get_battery_info(self) -> Dict[str, Any]:
        """
        Lấy thông tin pin.
        
        Returns:
            Dictionary chứa thông tin pin
        """
        try:
            output = self.run("shell dumpsys battery")
            battery_info = {}
            
            for line in output.splitlines():
                line = line.strip()
                if not line or ': ' not in line:
                    continue
                
                key, value = line.split(': ', 1)
                try:
                    # Thử chuyển đổi giá trị thành số
                    value = int(value) if value.isdigit() else float(value) if '.' in value and value.replace('.', '').isdigit() else value
                except:
                    pass
                
                battery_info[key] = value
            
            return battery_info
        except ADBCommandError as e:
            logger.error(f"Error getting battery info: {e}")
            return {}
    
    def get_screen_size(self) -> Dict[str, int]:
        """
        Lấy kích thước màn hình.
        
        Returns:
            Dictionary chứa chiều rộng và chiều cao màn hình
        """
        try:
            output = self.run("shell wm size")
            for line in output.splitlines():
                if "Physical size" in line:
                    size = line.split(": ")[1]
                    width, height = map(int, size.split("x"))
                    return {"width": width, "height": height}
            
            return {"width": 0, "height": 0}
        except Exception as e:
            logger.error(f"Error getting screen size: {e}")
            return {"width": 0, "height": 0}
    
    def connect_wireless(self, ip: str, port: int = 5555) -> str:
        """
        Kết nối đến thiết bị qua mạng không dây.
        
        Args:
            ip: Địa chỉ IP của thiết bị
            port: Cổng (mặc định là 5555)
            
        Returns:
            Kết quả lệnh
            
        Raises:
            DeviceConnectionError: Nếu kết nối thất bại
        """
        try:
            result = self.run(f"connect {ip}:{port}")
            if "connected" in result.lower():
                # Cập nhật device_id nếu kết nối thành công
                self.device_id = f"{ip}:{port}"
                return result
            else:
                raise DeviceConnectionError(f"{ip}:{port}", result)
        except ADBCommandError as e:
            raise DeviceConnectionError(f"{ip}:{port}", e.error_message)
    
    def disconnect_wireless(self, ip: Optional[str] = None, port: int = 5555) -> str:
        """
        Ngắt kết nối thiết bị không dây.
        
        Args:
            ip: Địa chỉ IP của thiết bị (None để ngắt kết nối tất cả)
            port: Cổng (mặc định là 5555)
            
        Returns:
            Kết quả lệnh
        """
        if ip:
            return self.run(f"disconnect {ip}:{port}")
        else:
            return self.run("disconnect")
    
    def wireless_pair(self, ip: str, port: int, pairing_code: str) -> str:
        """
        Ghép nối thiết bị không dây với mã ghép nối (Android 11+).
        
        Args:
            ip: Địa chỉ IP của thiết bị
            port: Cổng ghép nối
            pairing_code: Mã ghép nối
            
        Returns:
            Kết quả lệnh
        """
        return self.run(f"pair {ip}:{port} {pairing_code}")
    
    def start_server(self) -> str:
        """
        Khởi động máy chủ ADB.
        
        Returns:
            Kết quả lệnh
        """
        return self.run("start-server")
    
    def kill_server(self) -> str:
        """
        Dừng máy chủ ADB.
        
        Returns:
            Kết quả lệnh
        """
        return self.run("kill-server")
    
    def get_device_monitor(self) -> DeviceMonitor:
        """
        Lấy đối tượng theo dõi thiết bị.
        
        Returns:
            Đối tượng DeviceMonitor
        """
        monitor = DeviceMonitor()
        return monitor
