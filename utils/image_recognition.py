"""
Tiện ích nhận diện hình ảnh cho thư viện OIADB.
"""

import os
import cv2
import numpy as np
import logging
from typing import Optional, Tuple, List, Dict, Any, Union

# Thiết lập logging
logger = logging.getLogger('oiadb')

class ImageRecognition:
    """
    Lớp cung cấp các chức năng nhận diện hình ảnh trên màn hình thiết bị Android.
    Hỗ trợ nhận diện hình ảnh trên nhiều loại màn hình với các điều kiện khác nhau
    (phân giải cao/thấp, hình ảnh nét/mờ/vỡ).
    """
    
    def __init__(self, adb_runner):
        """
        Khởi tạo đối tượng ImageRecognition.
        
        Args:
            adb_runner: Đối tượng thực thi lệnh ADB
        """
        self.adb = adb_runner
        self.temp_screenshot_path = "/tmp/oiadb_screenshot.png"
    
    def _take_screenshot(self) -> np.ndarray:
        """
        Chụp ảnh màn hình thiết bị và chuyển đổi thành mảng numpy.
        
        Returns:
            Mảng numpy chứa ảnh màn hình
            
        Raises:
            Exception: Nếu không thể chụp ảnh màn hình
        """
        try:
            # Chụp ảnh màn hình và lưu vào thiết bị
            remote_path = "/sdcard/oiadb_screenshot.png"
            self.adb.run(f"shell screencap -p {remote_path}")
            
            # Kéo ảnh từ thiết bị về máy tính
            self.adb.run(f"pull {remote_path} {self.temp_screenshot_path}")
            
            # Xóa ảnh trên thiết bị
            self.adb.run(f"shell rm {remote_path}")
            
            # Đọc ảnh bằng OpenCV
            img = cv2.imread(self.temp_screenshot_path)
            if img is None:
                raise Exception(f"Không thể đọc ảnh từ {self.temp_screenshot_path}")
            
            return img
        
        except Exception as e:
            logger.error(f"Lỗi khi chụp ảnh màn hình: {str(e)}")
            raise
    
    def find_image(self, template_path: str, threshold: float = 0.8, 
                  multiple: bool = False, region: Optional[Tuple[int, int, int, int]] = None,
                  scale_range: Tuple[float, float] = (0.8, 1.2), scale_steps: int = 5,
                  rotation_range: Tuple[float, float] = (0, 0), rotation_steps: int = 1,
                  use_gray: bool = True, use_canny: bool = False) -> Union[Tuple[int, int, float], List[Tuple[int, int, float]], None]:
        """
        Tìm hình ảnh mẫu trên màn hình thiết bị.
        
        Args:
            template_path: Đường dẫn đến hình ảnh mẫu cần tìm
            threshold: Ngưỡng tương đồng (0.0 - 1.0), cao hơn = chính xác hơn
            multiple: Trả về tất cả các kết quả tìm thấy thay vì chỉ kết quả tốt nhất
            region: Vùng tìm kiếm (x, y, width, height), None = toàn màn hình
            scale_range: Phạm vi tỷ lệ để tìm kiếm (min_scale, max_scale)
            scale_steps: Số bước tỷ lệ trong phạm vi
            rotation_range: Phạm vi góc xoay để tìm kiếm (min_angle, max_angle) tính bằng độ
            rotation_steps: Số bước góc xoay trong phạm vi
            use_gray: Sử dụng ảnh xám để tăng tốc độ tìm kiếm
            use_canny: Sử dụng phát hiện cạnh Canny để cải thiện kết quả với hình ảnh mờ
            
        Returns:
            Nếu multiple=False: Tuple (x, y, confidence) của kết quả tốt nhất hoặc None nếu không tìm thấy
            Nếu multiple=True: Danh sách các tuple (x, y, confidence) hoặc danh sách rỗng nếu không tìm thấy
            
        Raises:
            Exception: Nếu không thể đọc hình ảnh mẫu
        """
        try:
            # Đọc hình ảnh mẫu
            template = cv2.imread(template_path)
            if template is None:
                raise Exception(f"Không thể đọc hình ảnh mẫu từ {template_path}")
            
            # Chụp ảnh màn hình
            screenshot = self._take_screenshot()
            
            # Cắt vùng tìm kiếm nếu được chỉ định
            if region:
                x, y, w, h = region
                screenshot = screenshot[y:y+h, x:x+w]
            
            # Chuyển đổi sang ảnh xám nếu cần
            if use_gray:
                screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
                template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
            
            # Sử dụng phát hiện cạnh Canny nếu cần
            if use_canny:
                if use_gray:
                    screenshot_processed = cv2.Canny(screenshot_gray, 50, 200)
                    template_processed = cv2.Canny(template_gray, 50, 200)
                else:
                    screenshot_processed = cv2.Canny(cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY), 50, 200)
                    template_processed = cv2.Canny(cv2.cvtColor(template, cv2.COLOR_BGR2GRAY), 50, 200)
            else:
                if use_gray:
                    screenshot_processed = screenshot_gray
                    template_processed = template_gray
                else:
                    screenshot_processed = screenshot
                    template_processed = template
            
            # Tính toán các tỷ lệ và góc xoay
            scales = np.linspace(scale_range[0], scale_range[1], scale_steps)
            angles = np.linspace(rotation_range[0], rotation_range[1], rotation_steps if rotation_steps > 1 else 1)
            
            best_result = None
            best_confidence = -1
            all_results = []
            
            # Thử với các tỷ lệ và góc xoay khác nhau
            for scale in scales:
                for angle in angles:
                    # Điều chỉnh kích thước mẫu
                    if scale != 1.0:
                        width = int(template_processed.shape[1] * scale)
                        height = int(template_processed.shape[0] * scale)
                        dim = (width, height)
                        resized_template = cv2.resize(template_processed, dim, interpolation=cv2.INTER_AREA)
                    else:
                        resized_template = template_processed
                    
                    # Xoay mẫu nếu cần
                    if angle != 0:
                        center = (resized_template.shape[1] // 2, resized_template.shape[0] // 2)
                        rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
                        rotated_template = cv2.warpAffine(resized_template, rotation_matrix, 
                                                         (resized_template.shape[1], resized_template.shape[0]))
                    else:
                        rotated_template = resized_template
                    
                    # Thực hiện so khớp mẫu
                    if len(screenshot_processed.shape) == 3 and len(rotated_template.shape) == 3:
                        # Ảnh màu
                        result = cv2.matchTemplate(screenshot_processed, rotated_template, cv2.TM_CCOEFF_NORMED)
                    else:
                        # Ảnh xám
                        result = cv2.matchTemplate(screenshot_processed, rotated_template, cv2.TM_CCOEFF_NORMED)
                    
                    # Tìm vị trí có độ tương đồng cao nhất
                    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
                    confidence = max_val
                    
                    if confidence > best_confidence:
                        best_confidence = confidence
                        h, w = rotated_template.shape[:2]
                        x, y = max_loc
                        # Điều chỉnh tọa độ trung tâm của hình ảnh
                        center_x = x + w // 2
                        center_y = y + h // 2
                        
                        # Điều chỉnh tọa độ nếu đang tìm kiếm trong vùng cụ thể
                        if region:
                            center_x += region[0]
                            center_y += region[1]
                        
                        best_result = (center_x, center_y, confidence)
                    
                    # Nếu cần tìm nhiều kết quả
                    if multiple:
                        # Tìm tất cả vị trí có độ tương đồng vượt ngưỡng
                        locations = np.where(result >= threshold)
                        h, w = rotated_template.shape[:2]
                        
                        for pt in zip(*locations[::-1]):
                            # Điều chỉnh tọa độ trung tâm của hình ảnh
                            center_x = pt[0] + w // 2
                            center_y = pt[1] + h // 2
                            
                            # Điều chỉnh tọa độ nếu đang tìm kiếm trong vùng cụ thể
                            if region:
                                center_x += region[0]
                                center_y += region[1]
                            
                            result_confidence = result[pt[1], pt[0]]
                            all_results.append((center_x, center_y, float(result_confidence)))
            
            # Lọc và sắp xếp kết quả nếu tìm nhiều kết quả
            if multiple and all_results:
                # Sắp xếp theo độ tương đồng giảm dần
                all_results.sort(key=lambda x: x[2], reverse=True)
                
                # Lọc các kết quả quá gần nhau
                filtered_results = []
                for result in all_results:
                    if not filtered_results:
                        filtered_results.append(result)
                        continue
                    
                    # Kiểm tra khoảng cách với các kết quả đã lọc
                    too_close = False
                    for filtered in filtered_results:
                        distance = ((result[0] - filtered[0]) ** 2 + (result[1] - filtered[1]) ** 2) ** 0.5
                        if distance < max(template.shape[0], template.shape[1]) / 2:
                            too_close = True
                            break
                    
                    if not too_close:
                        filtered_results.append(result)
                
                return filtered_results
            
            # Trả về kết quả tốt nhất nếu vượt ngưỡng
            if best_result and best_confidence >= threshold:
                return best_result
            
            return None
        
        except Exception as e:
            logger.error(f"Lỗi khi tìm hình ảnh: {str(e)}")
            if multiple:
                return []
            return None
    
    def wait_for_image(self, template_path: str, timeout: int = 10, interval: float = 0.5, 
                      threshold: float = 0.8, region: Optional[Tuple[int, int, int, int]] = None,
                      scale_range: Tuple[float, float] = (0.8, 1.2), scale_steps: int = 5,
                      use_gray: bool = True, use_canny: bool = False) -> Optional[Tuple[int, int, float]]:
        """
        Đợi cho đến khi hình ảnh xuất hiện trên màn hình.
        
        Args:
            template_path: Đường dẫn đến hình ảnh mẫu cần tìm
            timeout: Thời gian tối đa đợi (giây)
            interval: Khoảng thời gian giữa các lần tìm kiếm (giây)
            threshold: Ngưỡng tương đồng (0.0 - 1.0)
            region: Vùng tìm kiếm (x, y, width, height), None = toàn màn hình
            scale_range: Phạm vi tỷ lệ để tìm kiếm (min_scale, max_scale)
            scale_steps: Số bước tỷ lệ trong phạm vi
            use_gray: Sử dụng ảnh xám để tăng tốc độ tìm kiếm
            use_canny: Sử dụng phát hiện cạnh Canny để cải thiện kết quả với hình ảnh mờ
            
        Returns:
            Tuple (x, y, confidence) hoặc None nếu hết thời gian chờ
        """
        import time
        
        start_time = time.time()
        while time.time() - start_time < timeout:
            result = self.find_image(
                template_path=template_path,
                threshold=threshold,
                multiple=False,
                region=region,
                scale_range=scale_range,
                scale_steps=scale_steps,
                use_gray=use_gray,
                use_canny=use_canny
            )
            
            if result:
                return result
            
            time.sleep(interval)
        
        return None
    
    def find_all_images(self, template_path: str, threshold: float = 0.8, 
                       region: Optional[Tuple[int, int, int, int]] = None,
                       scale_range: Tuple[float, float] = (0.8, 1.2), scale_steps: int = 5,
                       use_gray: bool = True, use_canny: bool = False) -> List[Tuple[int, int, float]]:
        """
        Tìm tất cả các vị trí của hình ảnh mẫu trên màn hình.
        
        Args:
            template_path: Đường dẫn đến hình ảnh mẫu cần tìm
            threshold: Ngưỡng tương đồng (0.0 - 1.0)
            region: Vùng tìm kiếm (x, y, width, height), None = toàn màn hình
            scale_range: Phạm vi tỷ lệ để tìm kiếm (min_scale, max_scale)
            scale_steps: Số bước tỷ lệ trong phạm vi
            use_gray: Sử dụng ảnh xám để tăng tốc độ tìm kiếm
            use_canny: Sử dụng phát hiện cạnh Canny để cải thiện kết quả với hình ảnh mờ
            
        Returns:
            Danh sách các tuple (x, y, confidence) hoặc danh sách rỗng nếu không tìm thấy
        """
        return self.find_image(
            template_path=template_path,
            threshold=threshold,
            multiple=True,
            region=region,
            scale_range=scale_range,
            scale_steps=scale_steps,
            use_gray=use_gray,
            use_canny=use_canny
        ) or []
    
    def find_and_click(self, template_path: str, threshold: float = 0.8, 
                      region: Optional[Tuple[int, int, int, int]] = None,
                      scale_range: Tuple[float, float] = (0.8, 1.2), scale_steps: int = 5,
                      use_gray: bool = True, use_canny: bool = False,
                      click_offset: Tuple[int, int] = (0, 0)) -> bool:
        """
        Tìm hình ảnh trên màn hình và nhấp vào vị trí tìm thấy.
        
        Args:
            template_path: Đường dẫn đến hình ảnh mẫu cần tìm
            threshold: Ngưỡng tương đồng (0.0 - 1.0)
            region: Vùng tìm kiếm (x, y, width, height), None = toàn màn hình
            scale_range: Phạm vi tỷ lệ để tìm kiếm (min_scale, max_scale)
            scale_steps: Số bước tỷ lệ trong phạm vi
            use_gray: Sử dụng ảnh xám để tăng tốc độ tìm kiếm
            use_canny: Sử dụng phát hiện cạnh Canny để cải thiện kết quả với hình ảnh mờ
            click_offset: Độ lệch (dx, dy) khi nhấp chuột so với tâm hình ảnh
            
        Returns:
            True nếu tìm thấy và nhấp thành công, False nếu không
        """
        result = self.find_image(
            template_path=template_path,
            threshold=threshold,
            multiple=False,
            region=region,
            scale_range=scale_range,
            scale_steps=scale_steps,
            use_gray=use_gray,
            use_canny=use_canny
        )
        
        if result:
            x, y, confidence = result
            # Áp dụng độ lệch
            x += click_offset[0]
            y += click_offset[1]
            
            # Thực hiện nhấp chuột
            self.adb.run(f"shell input tap {x} {y}")
            return True
        
        return False
    
    def wait_and_click(self, template_path: str, timeout: int = 10, interval: float = 0.5,
                      threshold: float = 0.8, region: Optional[Tuple[int, int, int, int]] = None,
                      scale_range: Tuple[float, float] = (0.8, 1.2), scale_steps: int = 5,
                      use_gray: bool = True, use_canny: bool = False,
                      click_offset: Tuple[int, int] = (0, 0)) -> bool:
        """
        Đợi cho đến khi hình ảnh xuất hiện trên màn hình và nhấp vào vị trí đó.
        
        Args:
            template_path: Đường dẫn đến hình ảnh mẫu cần tìm
            timeout: Thời gian tối đa đợi (giây)
            interval: Khoảng thời gian giữa các lần tìm kiếm (giây)
            threshold: Ngưỡng tương đồng (0.0 - 1.0)
            region: Vùng tìm kiếm (x, y, width, height), None = toàn màn hình
            scale_range: Phạm vi tỷ lệ để tìm kiếm (min_scale, max_scale)
            scale_steps: Số bước tỷ lệ trong phạm vi
            use_gray: Sử dụng ảnh xám để tăng tốc độ tìm kiếm
            use_canny: Sử dụng phát hiện cạnh Canny để cải thiện kết quả với hình ảnh mờ
            click_offset: Độ lệch (dx, dy) khi nhấp chuột so với tâm hình ảnh
            
        Returns:
            True nếu tìm thấy và nhấp thành công, False nếu hết thời gian chờ
        """
        result = self.wait_for_image(
            template_path=template_path,
            timeout=timeout,
            interval=interval,
            threshold=threshold,
            region=region,
            scale_range=scale_range,
            scale_steps=scale_steps,
            use_gray=use_gray,
            use_canny=use_canny
        )
        
        if result:
            x, y, confidence = result
            # Áp dụng độ lệch
            x += click_offset[0]
            y += click_offset[1]
            
            # Thực hiện nhấp chuột
            self.adb.run(f"shell input tap {x} {y}")
            return True
        
        return False
    
    def find_and_click_all(self, template_path: str, threshold: float = 0.8,
                          region: Optional[Tuple[int, int, int, int]] = None,
                          scale_range: Tuple[float, float] = (0.8, 1.2), scale_steps: int = 5,
                          use_gray: bool = True, use_canny: bool = False,
                          click_offset: Tuple[int, int] = (0, 0),
                          click_delay: float = 0.5) -> int:
        """
        Tìm tất cả các vị trí của hình ảnh mẫu trên màn hình và nhấp vào từng vị trí.
        
        Args:
            template_path: Đường dẫn đến hình ảnh mẫu cần tìm
            threshold: Ngưỡng tương đồng (0.0 - 1.0)
            region: Vùng tìm kiếm (x, y, width, height), None = toàn màn hình
            scale_range: Phạm vi tỷ lệ để tìm kiếm (min_scale, max_scale)
            scale_steps: Số bước tỷ lệ trong phạm vi
            use_gray: Sử dụng ảnh xám để tăng tốc độ tìm kiếm
            use_canny: Sử dụng phát hiện cạnh Canny để cải thiện kết quả với hình ảnh mờ
            click_offset: Độ lệch (dx, dy) khi nhấp chuột so với tâm hình ảnh
            click_delay: Thời gian chờ giữa các lần nhấp (giây)
            
        Returns:
            Số lượng vị trí đã nhấp
        """
        import time
        
        results = self.find_all_images(
            template_path=template_path,
            threshold=threshold,
            region=region,
            scale_range=scale_range,
            scale_steps=scale_steps,
            use_gray=use_gray,
            use_canny=use_canny
        )
        
        click_count = 0
        for x, y, confidence in results:
            # Áp dụng độ lệch
            x += click_offset[0]
            y += click_offset[1]
            
            # Thực hiện nhấp chuột
            self.adb.run(f"shell input tap {x} {y}")
            click_count += 1
            
            # Chờ giữa các lần nhấp
            if click_count < len(results):
                time.sleep(click_delay)
        
        return click_count
    
    def get_image_location(self, template_path: str, threshold: float = 0.8,
                          region: Optional[Tuple[int, int, int, int]] = None,
                          scale_range: Tuple[float, float] = (0.8, 1.2), scale_steps: int = 5,
                          use_gray: bool = True, use_canny: bool = False) -> Optional[Tuple[int, int]]:
        """
        Lấy vị trí của hình ảnh trên màn hình.
        
        Args:
            template_path: Đường dẫn đến hình ảnh mẫu cần tìm
            threshold: Ngưỡng tương đồng (0.0 - 1.0)
            region: Vùng tìm kiếm (x, y, width, height), None = toàn màn hình
            scale_range: Phạm vi tỷ lệ để tìm kiếm (min_scale, max_scale)
            scale_steps: Số bước tỷ lệ trong phạm vi
            use_gray: Sử dụng ảnh xám để tăng tốc độ tìm kiếm
            use_canny: Sử dụng phát hiện cạnh Canny để cải thiện kết quả với hình ảnh mờ
            
        Returns:
            Tuple (x, y) hoặc None nếu không tìm thấy
        """
        result = self.find_image(
            template_path=template_path,
            threshold=threshold,
            multiple=False,
            region=region,
            scale_range=scale_range,
            scale_steps=scale_steps,
            use_gray=use_gray,
            use_canny=use_canny
        )
        
        if result:
            x, y, confidence = result
            return (x, y)
        
        return None
    
    def is_image_present(self, template_path: str, threshold: float = 0.8,
                        region: Optional[Tuple[int, int, int, int]] = None,
                        scale_range: Tuple[float, float] = (0.8, 1.2), scale_steps: int = 5,
                        use_gray: bool = True, use_canny: bool = False) -> bool:
        """
        Kiểm tra xem hình ảnh có xuất hiện trên màn hình không.
        
        Args:
            template_path: Đường dẫn đến hình ảnh mẫu cần tìm
            threshold: Ngưỡng tương đồng (0.0 - 1.0)
            region: Vùng tìm kiếm (x, y, width, height), None = toàn màn hình
            scale_range: Phạm vi tỷ lệ để tìm kiếm (min_scale, max_scale)
            scale_steps: Số bước tỷ lệ trong phạm vi
            use_gray: Sử dụng ảnh xám để tăng tốc độ tìm kiếm
            use_canny: Sử dụng phát hiện cạnh Canny để cải thiện kết quả với hình ảnh mờ
            
        Returns:
            True nếu hình ảnh xuất hiện, False nếu không
        """
        result = self.find_image(
            template_path=template_path,
            threshold=threshold,
            multiple=False,
            region=region,
            scale_range=scale_range,
            scale_steps=scale_steps,
            use_gray=use_gray,
            use_canny=use_canny
        )
        
        return result is not None
    
    def wait_until_image_disappears(self, template_path: str, timeout: int = 10, interval: float = 0.5,
                                   threshold: float = 0.8, region: Optional[Tuple[int, int, int, int]] = None,
                                   scale_range: Tuple[float, float] = (0.8, 1.2), scale_steps: int = 5,
                                   use_gray: bool = True, use_canny: bool = False) -> bool:
        """
        Đợi cho đến khi hình ảnh biến mất khỏi màn hình.
        
        Args:
            template_path: Đường dẫn đến hình ảnh mẫu cần tìm
            timeout: Thời gian tối đa đợi (giây)
            interval: Khoảng thời gian giữa các lần tìm kiếm (giây)
            threshold: Ngưỡng tương đồng (0.0 - 1.0)
            region: Vùng tìm kiếm (x, y, width, height), None = toàn màn hình
            scale_range: Phạm vi tỷ lệ để tìm kiếm (min_scale, max_scale)
            scale_steps: Số bước tỷ lệ trong phạm vi
            use_gray: Sử dụng ảnh xám để tăng tốc độ tìm kiếm
            use_canny: Sử dụng phát hiện cạnh Canny để cải thiện kết quả với hình ảnh mờ
            
        Returns:
            True nếu hình ảnh biến mất trong thời gian chờ, False nếu không
        """
        import time
        
        start_time = time.time()
        while time.time() - start_time < timeout:
            result = self.find_image(
                template_path=template_path,
                threshold=threshold,
                multiple=False,
                region=region,
                scale_range=scale_range,
                scale_steps=scale_steps,
                use_gray=use_gray,
                use_canny=use_canny
            )
            
            if not result:
                return True
            
            time.sleep(interval)
        
        return False
