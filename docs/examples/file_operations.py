"""
Ví dụ về thao tác file với thư viện OIADB.
"""

from oiadb import MyADB
from oiadb.commands import file_ops
import os

def file_operations_example():
    """
    Ví dụ về cách thao tác file với OIADB.
    """
    # Khởi tạo ADB
    adb = MyADB()
    
    # Tạo file văn bản cục bộ để đẩy lên thiết bị
    local_file_path = "./test_file.txt"
    with open(local_file_path, "w") as f:
        f.write("Đây là file test được tạo bởi OIADB.")
    
    # Đường dẫn trên thiết bị
    remote_dir = "/sdcard/oiadb_test"
    remote_file_path = f"{remote_dir}/test_file.txt"
    
    # Tạo thư mục trên thiết bị
    print(f"Đang tạo thư mục {remote_dir}...")
    if file_ops.create_dir(remote_dir):
        print(f"Đã tạo thư mục {remote_dir}")
    else:
        print(f"Không thể tạo thư mục {remote_dir}")
    
    # Đẩy file lên thiết bị
    print(f"Đang đẩy file {local_file_path} lên {remote_file_path}...")
    if file_ops.push(local_file_path, remote_file_path):
        print("Đã đẩy file lên thiết bị thành công!")
    else:
        print("Không thể đẩy file lên thiết bị!")
        return
    
    # Kiểm tra file tồn tại
    if file_ops.file_exists(remote_file_path):
        print(f"File {remote_file_path} tồn tại trên thiết bị")
        
        # Lấy kích thước file
        size = file_ops.get_file_size(remote_file_path)
        print(f"Kích thước file: {size} bytes")
        
        # Lấy quyền file
        permissions = file_ops.get_file_permissions(remote_file_path)
        print(f"Quyền file: {permissions}")
        
        # Đặt quyền file
        print("Đang đặt quyền file thành 644...")
        file_ops.set_file_permissions(remote_file_path, "644")
        
        # Liệt kê file trong thư mục
        files = file_ops.list_files(remote_dir)
        print(f"Các file trong {remote_dir}: {files}")
        
        # Tạo file sao chép
        remote_copy_path = f"{remote_dir}/test_file_copy.txt"
        print(f"Đang sao chép file {remote_file_path} thành {remote_copy_path}...")
        file_ops.copy_file(remote_file_path, remote_copy_path)
        
        # Tạo file di chuyển
        remote_move_path = f"{remote_dir}/test_file_moved.txt"
        print(f"Đang di chuyển file {remote_copy_path} thành {remote_move_path}...")
        file_ops.move_file(remote_copy_path, remote_move_path)
        
        # Lấy file từ thiết bị
        local_download_path = "./downloaded_file.txt"
        print(f"Đang lấy file {remote_file_path} về {local_download_path}...")
        if file_ops.pull(remote_file_path, local_download_path):
            print("Đã lấy file từ thiết bị thành công!")
            
            # Đọc nội dung file đã tải về
            with open(local_download_path, "r") as f:
                content = f.read()
                print(f"Nội dung file: {content}")
            
            # Xóa file cục bộ đã tải về
            os.remove(local_download_path)
        else:
            print("Không thể lấy file từ thiết bị!")
        
        # Xóa các file trên thiết bị
        print(f"Đang xóa file {remote_file_path}...")
        file_ops.remove_file(remote_file_path)
        
        print(f"Đang xóa file {remote_move_path}...")
        file_ops.remove_file(remote_move_path)
        
        # Xóa thư mục
        print(f"Đang xóa thư mục {remote_dir}...")
        file_ops.remove_dir(remote_dir)
    else:
        print(f"File {remote_file_path} không tồn tại trên thiết bị")
    
    # Xóa file cục bộ
    os.remove(local_file_path)
    print("Đã xóa file cục bộ")

if __name__ == "__main__":
    file_operations_example()
