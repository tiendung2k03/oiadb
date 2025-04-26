"""
Ví dụ về nhận diện hình ảnh và tương tác dựa trên hình ảnh với thư viện OIADB.
"""

from oiadb import MyADB
from oiadb.commands import image_interaction, interaction
import time
import os

def image_recognition_example():
    """
    Ví dụ về cách sử dụng chức năng nhận diện hình ảnh với OIADB.
    """
    # Khởi tạo ADB
    adb = MyADB()
    
    # Tạo thư mục để lưu ảnh mẫu và ảnh màn hình
    templates_dir = "./templates"
    os.makedirs(templates_dir, exist_ok=True)
    
    # Chụp ảnh màn hình để sử dụng làm ví dụ
    screenshot_path = f"{templates_dir}/screenshot.png"
    print("Đang chụp ảnh màn hình...")
    interaction.take_screenshot(screenshot_path)
    print(f"Đã chụp ảnh màn hình và lưu vào {screenshot_path}")
    
    # Giả định: Đã có sẵn các ảnh mẫu trong thư mục templates
    # Trong thực tế, bạn cần chuẩn bị các ảnh mẫu trước
    button_template = f"{templates_dir}/button.png"
    icon_template = f"{templates_dir}/icon.png"
    
    # Tìm hình ảnh trên màn hình
    print(f"Đang tìm hình ảnh {button_template} trên màn hình...")
    result = image_interaction.find_image(
        template_path=button_template,
        threshold=0.8,  # Ngưỡng tương đồng (0.0-1.0)
        scale_range=(0.8, 1.2),  # Phạm vi tỷ lệ để tìm kiếm
        scale_steps=5,  # Số bước tỷ lệ
        use_gray=True,  # Sử dụng ảnh xám để tăng tốc độ
        use_canny=False  # Sử dụng phát hiện cạnh Canny
    )
    
    if result:
        x, y, confidence = result
        print(f"Đã tìm thấy hình ảnh tại ({x}, {y}) với độ tương đồng {confidence}")
        
        # Nhấp vào hình ảnh đã tìm thấy
        print(f"Đang nhấp vào tọa độ ({x}, {y})...")
        interaction.tap(x, y)
    else:
        print("Không tìm thấy hình ảnh trên màn hình")
    
    # Tìm tất cả các hình ảnh tương tự
    print(f"Đang tìm tất cả các hình ảnh tương tự {icon_template} trên màn hình...")
    results = image_interaction.find_all_images(
        template_path=icon_template,
        threshold=0.7,
        max_results=5  # Số kết quả tối đa
    )
    
    if results:
        print(f"Đã tìm thấy {len(results)} hình ảnh tương tự:")
        for i, (x, y, confidence) in enumerate(results):
            print(f"  {i+1}. Tại ({x}, {y}) với độ tương đồng {confidence}")
    else:
        print("Không tìm thấy hình ảnh tương tự trên màn hình")
    
    # Ví dụ về đợi hình ảnh xuất hiện
    print("Ví dụ về đợi hình ảnh xuất hiện (giả lập)...")
    print("Nhấn nút Home để mở màn hình chính...")
    interaction.home()
    
    # Đợi một biểu tượng xuất hiện trên màn hình chính
    print(f"Đang đợi hình ảnh {icon_template} xuất hiện...")
    result = image_interaction.wait_for_image(
        template_path=icon_template,
        timeout=10,  # Thời gian tối đa đợi (giây)
        interval=1.0,  # Khoảng thời gian giữa các lần tìm kiếm (giây)
        threshold=0.7
    )
    
    if result:
        print(f"Hình ảnh đã xuất hiện tại ({result[0]}, {result[1]}) sau khi đợi")
    else:
        print("Hình ảnh không xuất hiện trong thời gian chờ")
    
    # Ví dụ về tương tác nâng cao với hình ảnh
    print("Ví dụ về tương tác nâng cao với hình ảnh (giả lập)...")
    
    # Nhấn giữ vào hình ảnh
    print(f"Đang nhấn giữ vào hình ảnh {button_template}...")
    if image_interaction.long_press_image(
        template_path=button_template,
        duration=1000  # Thời gian nhấn giữ (ms)
    ):
        print("Đã nhấn giữ vào hình ảnh thành công")
    else:
        print("Không tìm thấy hình ảnh để nhấn giữ")
    
    # Nhấp đúp vào hình ảnh
    print(f"Đang nhấp đúp vào hình ảnh {button_template}...")
    if image_interaction.double_tap_image(
        template_path=button_template,
        tap_delay=0.1  # Thời gian giữa hai lần nhấp (giây)
    ):
        print("Đã nhấp đúp vào hình ảnh thành công")
    else:
        print("Không tìm thấy hình ảnh để nhấp đúp")
    
    # Ví dụ về xử lý các điều kiện màn hình khác nhau
    print("Ví dụ về xử lý các điều kiện màn hình khác nhau...")
    
    # Tìm trên màn hình phân giải cao
    print("Đang tìm trên màn hình phân giải cao...")
    result_high_res = image_interaction.find_image(
        template_path=button_template,
        threshold=0.7,
        scale_range=(1.0, 1.5),  # Tỷ lệ lớn hơn cho màn hình phân giải cao
        scale_steps=5
    )
    
    if result_high_res:
        print(f"Đã tìm thấy hình ảnh trên màn hình phân giải cao tại ({result_high_res[0]}, {result_high_res[1]})")
    else:
        print("Không tìm thấy hình ảnh trên màn hình phân giải cao")
    
    # Tìm hình ảnh mờ
    print("Đang tìm hình ảnh mờ...")
    result_blurry = image_interaction.find_image(
        template_path=button_template,
        threshold=0.6,  # Ngưỡng thấp hơn cho hình ảnh mờ
        use_canny=True  # Sử dụng phát hiện cạnh Canny cho hình ảnh mờ
    )
    
    if result_blurry:
        print(f"Đã tìm thấy hình ảnh mờ tại ({result_blurry[0]}, {result_blurry[1]})")
    else:
        print("Không tìm thấy hình ảnh mờ")
    
    print("Hoàn thành ví dụ về nhận diện hình ảnh!")

if __name__ == "__main__":
    image_recognition_example()
