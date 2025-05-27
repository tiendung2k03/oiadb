# OIADB - Tài liệu Hướng dẫn Toàn diện

## Mục lục

*   [1. Giới thiệu](#1-giới-thiệu)
    *   [1.1. OIADB là gì?](#11-oiadb-là-gì)
    *   [1.2. Tại sao chọn OIADB?](#12-tại-sao-chọn-oiadb)
    *   [1.3. Các tính năng chính](#13-các-tính-năng-chính)
    *   [1.4. Đối tượng sử dụng](#14-đối-tượng-sử-dụng)
*   [2. Cài đặt và Thiết lập](#2-cài-đặt-và-thiết-lập)
    *   [2.1. Yêu cầu tiên quyết](#21-yêu-cầu-tiên-quyết)
        *   [2.1.1. Python](#211-python)
        *   [2.1.2. ADB (Android Debug Bridge)](#212-adb-android-debug-bridge)
        *   [2.1.3. OpenCV và NumPy (Tùy chọn, cho Nhận diện Hình ảnh)](#213-opencv-và-numpy-tùy-chọn-cho-nhận-diện-hình-ảnh)
    *   [2.2. Cài đặt ADB](#22-cài-đặt-adb)
        *   [2.2.1. Windows](#221-windows)
        *   [2.2.2. macOS](#222-macos)
        *   [2.2.3. Linux (Debian/Ubuntu)](#223-linux-debianubuntu)
        *   [2.2.4. Kiểm tra cài đặt ADB](#224-kiểm-tra-cài-đặt-adb)
    *   [2.3. Cài đặt OIADB](#23-cài-đặt-oiadb)
        *   [2.3.1. Cài đặt từ PyPI (Khuyến nghị)](#231-cài-đặt-từ-pypi-khuyến-nghị)
        *   [2.3.2. Cài đặt với hỗ trợ Nhận diện Hình ảnh](#232-cài-đặt-với-hỗ-trợ-nhận-diện-hình-ảnh)
        *   [2.3.3. Cài đặt từ Mã nguồn (Cho nhà phát triển)](#233-cài-đặt-từ-mã-nguồn-cho-nhà-phát-triển)
    *   [2.4. Thiết lập Thiết bị Android](#24-thiết-lập-thiết-bị-android)
        *   [2.4.1. Bật Tùy chọn Nhà phát triển](#241-bật-tùy-chọn-nhà-phát-triển)
        *   [2.4.2. Bật Gỡ lỗi USB](#242-bật-gỡ-lỗi-usb)
        *   [2.4.3. Ủy quyền Kết nối ADB](#243-ủy-quyền-kết-nối-adb)
        *   [2.4.4. Gỡ lỗi qua Wi-Fi (Tùy chọn)](#244-gỡ-lỗi-qua-wi-fi-tùy-chọn)
    *   [2.5. Xác minh Cài đặt OIADB](#25-xác-minh-cài-đặt-oiadb)
*   [3. Kiến trúc Thư viện](#3-kiến-trúc-thư-viện)
    *   [3.1. Tổng quan](#31-tổng-quan)
    *   [3.2. Cấu trúc Module](#32-cấu-trúc-module)
    *   [3.3. Luồng hoạt động chính](#33-luồng-hoạt-động-chính)
    *   [3.4. Xử lý Lỗi và Ngoại lệ](#34-xử-lý-lỗi-và-ngoại-lệ)
*   [4. Lớp MyADB - Cốt lõi Tương tác](#4-lớp-myadb---cốt-lõi-tương-tác)
    *   [4.1. Khởi tạo và Cấu hình](#41-khởi-tạo-và-cấu-hình)
    *   [4.2. Các Phương thức Chính](#42-các-phương-thức-chính)
    *   [4.3. Tự động Cài đặt và Quản lý Server](#43-tự-động-cài-đặt-và-quản-lý-server)
    *   [4.4. Ví dụ Sử dụng Cơ bản](#44-ví-dụ-sử-dụng-cơ-bản)
*   [5. Module Commands - Bộ lệnh Chi tiết](#5-module-commands---bộ-lệnh-chi-tiết)
    *   [5.1. `app_info`: Lấy Thông tin Ứng dụng](#51-app_info-lấy-thông-tin-ứng-dụng)
    *   [5.2. `apps`: Quản lý Vòng đời Ứng dụng](#52-apps-quản-lý-vòng-đời-ứng-dụng)
    *   [5.3. `basic`: Các Lệnh ADB Cơ bản](#53-basic-các-lệnh-adb-cơ-bản)
    *   [5.4. `connect`: Quản lý Kết nối Thiết bị](#54-connect-quản-lý-kết-nối-thiết-bị)
    *   [5.5. `device_actions`: Hành động trên Thiết bị](#55-device_actions-hành-động-trên-thiết-bị)
    *   [5.6. `device_info`: Thu thập Thông tin Thiết bị](#56-device_info-thu-thập-thông-tin-thiết-bị)
    *   [5.7. `file_ops`: Thao tác với Hệ thống Tệp](#57-file_ops-thao-tác-với-hệ-thống-tệp)
    *   [5.8. `interaction`: Mô phỏng Tương tác Người dùng](#58-interaction-mô-phỏng-tương-tác-người-dùng)
    *   [5.9. `image_interaction`: Tương tác Dựa trên Hình ảnh](#59-image_interaction-tương-tác-dựa-trên-hình-ảnh)
    *   [5.10. `logs`: Thu thập và Quản lý Log](#510-logs-thu-thập-và-quản-lý-log)
    *   [5.11. `permissions`: Quản lý Quyền Ứng dụng](#511-permissions-quản-lý-quyền-ứng-dụng)
    *   [5.12. `xml_dump`: Phân tích Giao diện Người dùng](#512-xml_dump-phân-tích-giao-diện-người-dùng)
    *   [5.13. `android14_support` & `ui_compatibility`: Hỗ trợ Tương thích](#513-android14_support--ui_compatibility-hỗ-trợ-tương-thích)
*   [6. Module Utils - Các Tiện ích Hỗ trợ](#6-module-utils---các-tiện-ích-hỗ-trợ)
    *   [6.1. `advanced`: Tiện ích Nâng cao (Cache, Async, Monitor)](#61-advanced-tiện-ích-nâng-cao-cache-async-monitor)
    *   [6.2. `image_recognition`: Xử lý Nhận diện Hình ảnh](#62-image_recognition-xử-lý-nhận-diện-hình-ảnh)
    *   [6.3. `runner`: Thực thi Lệnh ADB](#63-runner-thực-thi-lệnh-adb)
    *   [6.4. `platform_utils`: Tiện ích Đa nền tảng](#64-platform_utils-tiện-ích-đa-nền-tảng)
    *   [6.5. `adb_manager`: Quản lý Phiên bản ADB](#65-adb_manager-quản-lý-phiên-bản-adb)
*   [7. Hướng dẫn Sử dụng Chi tiết](#7-hướng-dẫn-sử-dụng-chi-tiết)
    *   [7.1. Kết nối và Quản lý Thiết bị](#71-kết-nối-và-quản-lý-thiết-bị)
    *   [7.2. Quản lý Ứng dụng (Cài đặt, Gỡ, Chạy, Dừng)](#72-quản-lý-ứng-dụng-cài-đặt-gỡ-chạy-dừng)
    *   [7.3. Thao tác với File và Thư mục](#73-thao-tác-với-file-và-thư-mục)
    *   [7.4. Mô phỏng Tương tác (Chạm, Vuốt, Nhập liệu)](#74-mô-phỏng-tương-tác-chạm-vuốt-nhập-liệu)
    *   [7.5. Tự động hóa với Nhận diện Hình ảnh](#75-tự-động-hóa-với-nhận-diện-hình-ảnh)
    *   [7.6. Thu thập Log và Gỡ lỗi](#76-thu-thập-log-và-gỡ-lỗi)
    *   [7.7. Phân tích Giao diện với XML Dump](#77-phân-tích-giao-diện-với-xml-dump)
    *   [7.8. Sử dụng các Tính năng Nâng cao (Async, Cache)](#78-sử-dụng-các-tính-năng-nâng-cao-async-cache)
*   [8. Ví dụ Thực tế và Kịch bản Nâng cao](#8-ví-dụ-thực-tế-và-kịch-bản-nâng-cao)
    *   [8.1. Kịch bản Kiểm thử Tự động Đơn giản](#81-kịch-bản-kiểm-thử-tự-động-đơn-giản)
    *   [8.2. Tự động hóa Tác vụ Lặp lại](#82-tự-động-hóa-tác-vụ-lặp-lại)
    *   [8.3. Kiểm thử Giao diện Phức tạp với Nhận diện Hình ảnh](#83-kiểm-thử-giao-diện-phức-tạp-với-nhận-diện-hình-ảnh)
    *   [8.4. Thu thập Dữ liệu từ Nhiều Thiết bị](#84-thu-thập-dữ-liệu-từ-nhiều-thiết-bị)
*   [9. Xử lý Lỗi và Gỡ rối (Troubleshooting)](#9-xử-lý-lỗi-và-gỡ-rối-troubleshooting)
    *   [9.1. Các Lỗi Thường gặp và Cách Khắc phục](#91-các-lỗi-thường-gặp-và-cách-khắc-phục)
    *   [9.2. Gỡ rối Kết nối ADB](#92-gỡ-rối-kết-nối-adb)
    *   [9.3. Gỡ rối Nhận diện Hình ảnh](#93-gỡ-rối-nhận-diện-hình-ảnh)
    *   [9.4. Gỡ rối XML Dump](#94-gỡ-rối-xml-dump)
    *   [9.5. Báo cáo Lỗi và Tìm kiếm Hỗ trợ](#95-báo-cáo-lỗi-và-tìm-kiếm-hỗ-trợ)
*   [10. Thực hành Tốt nhất (Best Practices)](#10-thực-hành-tốt-nhất-best-practices)
    *   [10.1. Tối ưu hóa Hiệu suất](#101-tối-ưu-hóa-hiệu-suất)
    *   [10.2. Viết Mã Dễ bảo trì](#102-viết-mã-dễ-bảo-trì)
    *   [10.3. Xử lý Lỗi Mạnh mẽ](#103-xử-lý-lỗi-mạnh-mẽ)
    *   [10.4. Quản lý Thiết bị Hiệu quả](#104-quản-lý-thiết-bị-hiệu-quả)
*   [11. Đóng góp cho Dự án](#11-đóng-góp-cho-dự-án)
    *   [11.1. Quy trình Đóng góp](#111-quy-trình-đóng-góp)
    *   [11.2. Báo cáo Lỗi (Bug Reports)](#112-báo-cáo-lỗi-bug-reports)
    *   [11.3. Yêu cầu Tính năng (Feature Requests)](#113-yêu-cầu-tính-năng-feature-requests)
    *   [11.4. Gửi Pull Request](#114-gửi-pull-request)
    *   [11.5. Quy tắc Ứng xử (Code of Conduct)](#115-quy-tắc-ứng-xử-code-of-conduct)
*   [12. Tham khảo và Tài nguyên](#12-tham-khảo-và-tài-nguyên)
    *   [12.1. Tài liệu ADB Chính thức](#121-tài-liệu-adb-chính-thức)
    *   [12.2. Tài liệu OpenCV](#122-tài-liệu-opencv)
    *   [12.3. Kho GitHub OIADB](#123-kho-github-oiadb)
    *   [12.4. Trang PyPI OIADB](#124-trang-pypi-oiadb)
*   [13. Phụ lục](#13-phụ-lục)
    *   [13.1. Danh sách Mã phím Android (Key Codes)](#131-danh-sách-mã-phím-android-key-codes)
    *   [13.2. Các Tùy chọn Logcat Phổ biến](#132-các-tùy-chọn-logcat-phổ-biến)

---

## 1. Giới thiệu

### 1.1. OIADB là gì?

**OIADB** (viết tắt của **O**penCV **I**mage **A**ndroid **D**ebug **B**ridge) là một thư viện Python mạnh mẽ và linh hoạt, đóng vai trò như một lớp bao (wrapper) cấp cao cho công cụ dòng lệnh **Android Debug Bridge (ADB)**. Nó được thiết kế để đơn giản hóa và tự động hóa các tác vụ tương tác, quản lý và kiểm thử thiết bị Android từ môi trường Python.

Khác với việc gọi trực tiếp các lệnh ADB phức tạp và khó nhớ, OIADB cung cấp một API Pythonic, trực quan và dễ sử dụng. Thư viện không chỉ dừng lại ở việc ánh xạ các lệnh ADB cơ bản mà còn tích hợp các tính năng nâng cao độc đáo, nổi bật nhất là khả năng **nhận diện hình ảnh** dựa trên thư viện **OpenCV**. Điều này cho phép tạo ra các kịch bản tự động hóa mạnh mẽ, có khả năng tương tác với giao diện người dùng (UI) của ứng dụng Android ngay cả khi không có ID phần tử hoặc cấu trúc UI ổn định.

Ngoài ra, OIADB còn cung cấp các tiện ích để **phân tích cấu trúc UI (XML Dump)** với hỗ trợ thông tin về khả năng truy cập (accessibility), quản lý phiên bản ADB tự động, thực thi lệnh bất đồng bộ, và hỗ trợ đa nền tảng (Windows, macOS, Linux, và thậm chí cả Termux trên Android).

### 1.2. Tại sao chọn OIADB?

Trong bối cảnh có nhiều công cụ và thư viện hỗ trợ tự động hóa Android, OIADB nổi bật với các ưu điểm sau:

*   **API Pythonic và Dễ sử dụng:** Thay vì phải nhớ cú pháp lệnh ADB, bạn có thể sử dụng các hàm và lớp Python rõ ràng, có tài liệu hướng dẫn đầy đủ.
*   **Tự động hóa Mạnh mẽ với Nhận diện Hình ảnh:** Khả năng tìm và tương tác với các thành phần UI dựa trên hình ảnh mẫu (template matching) mở ra cánh cửa cho việc tự động hóa các ứng dụng phức tạp, game, hoặc các ứng dụng không cung cấp API hoặc ID phần tử ổn định.
*   **Tích hợp Tính năng Nâng cao:** Các tiện ích như XML Dump, quản lý server tự động, thực thi bất đồng bộ, cache kết quả lệnh giúp tăng tốc độ phát triển và hiệu quả thực thi.
*   **Đa nền tảng:** Hoạt động mượt mà trên các hệ điều hành phổ biến, giúp bạn phát triển và chạy kịch bản tự động hóa ở bất cứ đâu.
*   **Mã nguồn Mở và Cộng đồng:** Là một dự án mã nguồn mở, OIADB khuyến khích sự đóng góp và phát triển từ cộng đồng.
*   **Giải pháp Toàn diện:** Cung cấp một bộ công cụ đầy đủ từ quản lý thiết bị, ứng dụng, file, tương tác UI, đến gỡ lỗi và phân tích.

### 1.3. Các tính năng chính

*   **Quản lý Thiết bị:** Kết nối/ngắt kết nối (USB, Wi-Fi), liệt kê thiết bị, lấy thông tin chi tiết (model, phiên bản Android, độ phân giải, pin, CPU, bộ nhớ, IP, IMEI, serial...), khởi động lại, tắt máy, vào chế độ bootloader/recovery.
*   **Quản lý Ứng dụng:** Cài đặt/gỡ cài đặt (APK), khởi động/dừng ứng dụng, xóa dữ liệu/cache, liệt kê ứng dụng đã cài đặt, kiểm tra trạng thái cài đặt, lấy thông tin ứng dụng (phiên bản, đường dẫn).
*   **Thao tác File:** Đẩy (push)/kéo (pull) file và thư mục, liệt kê file, kiểm tra sự tồn tại, tạo/xóa thư mục, xóa file.
*   **Tương tác Giao diện Người dùng (UI):**
    *   **Cơ bản:** Chạm (tap), vuốt (swipe), nhấn giữ (long press), nhập văn bản (text input), gửi sự kiện phím (key event), nhấn các phím cứng (Back, Home, Power, Volume...).
    *   **Nâng cao:** Thu phóng (pinch/zoom), kéo thả (drag), cuộn (scroll), mở khóa màn hình (pattern, PIN).
*   **Nhận diện Hình ảnh (OpenCV):**
    *   Tìm kiếm hình ảnh mẫu trên màn hình (đơn lẻ hoặc tất cả).
    *   Hỗ trợ tìm kiếm theo vùng (region), ngưỡng tương đồng (threshold), tỷ lệ (scale), góc xoay (rotation).
    *   Tối ưu hóa tìm kiếm với ảnh xám (grayscale) và phát hiện cạnh (Canny).
    *   Tương tác trực tiếp: Chạm vào hình ảnh tìm thấy, đợi hình ảnh xuất hiện/biến mất rồi tương tác.
*   **Phân tích Giao diện (XML Dump):**
    *   Lấy cấu trúc UI dưới dạng XML.
    *   Hỗ trợ lấy thông tin về khả năng truy cập (accessibility properties).
    *   Tìm kiếm phần tử dựa trên thuộc tính (text, resource-id, class...). (*Lưu ý: Tính năng tìm kiếm phần tử từ XML dump có thể cần phát triển thêm hoặc sử dụng kết hợp với các thư viện khác*).
*   **Quản lý Log:** Xem logcat thời gian thực, lọc log theo tag/priority/message, xóa log, lưu log vào file, tạo báo cáo lỗi (bugreport).
*   **Quản lý Quyền:** Cấp/thu hồi quyền cho ứng dụng, liệt kê quyền, kiểm tra quyền.
*   **Tiện ích Nâng cao:**
    *   Thực thi lệnh ADB bất đồng bộ.
    *   Cache kết quả lệnh để tăng tốc độ.
    *   Theo dõi sự kiện kết nối/ngắt kết nối thiết bị.
    *   Tự động quản lý (tải xuống, cài đặt) phiên bản ADB phù hợp với hệ điều hành.
    *   Tự động cài đặt và quản lý oiadb-server trên thiết bị (cần thiết cho một số tính năng nâng cao như XML Dump).

### 1.4. Đối tượng sử dụng

OIADB phù hợp với nhiều đối tượng người dùng:

*   **Nhà phát triển Tự động hóa Kiểm thử (QA Automation Engineers):** Xây dựng các kịch bản kiểm thử tự động cho ứng dụng Android một cách hiệu quả và linh hoạt.
*   **Nhà phát triển Ứng dụng Android (Android Developers):** Tự động hóa các tác vụ lặp lại trong quá trình phát triển, gỡ lỗi, hoặc kiểm thử đơn vị.
*   **Kỹ sư DevOps:** Tích hợp các tác vụ quản lý thiết bị Android vào quy trình CI/CD.
*   **Người dùng Python:** Bất kỳ ai muốn tương tác và điều khiển thiết bị Android thông qua mã Python.
*   **Nhà nghiên cứu:** Thu thập dữ liệu hoặc thực hiện các thí nghiệm tự động trên thiết bị Android.

---

## 2. Cài đặt và Thiết lập

Phần này hướng dẫn chi tiết các bước cần thiết để cài đặt OIADB và chuẩn bị môi trường làm việc.

### 2.1. Yêu cầu tiên quyết

Trước khi cài đặt OIADB, hãy đảm bảo hệ thống của bạn đáp ứng các yêu cầu sau:

#### 2.1.1. Python

*   **Phiên bản:** Python 3.6 trở lên. Khuyến nghị sử dụng phiên bản Python 3.7+ để tận dụng các tính năng ngôn ngữ mới nhất.
*   **Kiểm tra phiên bản:** Mở terminal hoặc command prompt và chạy lệnh:
    ```bash
    python --version
    # hoặc
    python3 --version
    ```
*   **Cài đặt Python:** Nếu chưa có Python, hãy tải và cài đặt từ trang chủ [python.org](https://www.python.org/downloads/). Đảm bảo chọn tùy chọn "Add Python to PATH" trong quá trình cài đặt trên Windows.
*   **pip:** Công cụ quản lý gói `pip` thường được cài đặt sẵn cùng Python. Kiểm tra bằng lệnh `pip --version` hoặc `pip3 --version`. Nếu chưa có, hãy tham khảo hướng dẫn cài đặt `pip` tại [pip.pypa.io](https://pip.pypa.io/en/stable/installation/).

#### 2.1.2. ADB (Android Debug Bridge)

*   **Khái niệm:** ADB là một công cụ dòng lệnh đa năng cho phép bạn giao tiếp với thiết bị Android. OIADB sử dụng ADB làm nền tảng để thực thi các lệnh.
*   **Yêu cầu:** ADB cần được cài đặt trên máy tính của bạn và **có thể truy cập được thông qua biến môi trường PATH** (nghĩa là bạn có thể chạy lệnh `adb` từ bất kỳ thư mục nào trong terminal).
*   **Tự động cài đặt (Tùy chọn):** OIADB có khả năng tự động tải xuống và cài đặt ADB nếu không tìm thấy (tính năng này được bật mặc định khi khởi tạo `MyADB`). Tuy nhiên, việc cài đặt thủ công trước sẽ đảm bảo tính ổn định và cho phép bạn kiểm soát phiên bản ADB.
*   **Hướng dẫn cài đặt:** Xem chi tiết tại mục [2.2. Cài đặt ADB](#22-cài-đặt-adb).

#### 2.1.3. OpenCV và NumPy (Tùy chọn, cho Nhận diện Hình ảnh)

*   **Mục đích:** Hai thư viện này là **bắt buộc** nếu bạn muốn sử dụng các tính năng liên quan đến nhận diện hình ảnh (`image_interaction`, `image_recognition`).
*   **OpenCV (cv2):** Thư viện mã nguồn mở hàng đầu về xử lý ảnh và thị giác máy tính.
*   **NumPy:** Thư viện nền tảng cho tính toán khoa học trong Python, cần thiết cho các thao tác mảng của OpenCV.
*   **Cài đặt:** Bạn có thể cài đặt chúng cùng lúc với OIADB bằng cách chỉ định phần phụ thuộc `[image]`:
    ```bash
    pip install oiadb[image]
    ```
    Hoặc cài đặt riêng lẻ:
    ```bash
    pip install opencv-python numpy
    ```
*   **Lưu ý:** Nếu bạn không cần tính năng nhận diện hình ảnh, bạn có thể bỏ qua bước này và cài đặt OIADB cơ bản. Thư viện sẽ hoạt động bình thường cho các tính năng khác, nhưng sẽ báo lỗi nếu bạn cố gắng gọi các hàm liên quan đến hình ảnh.

### 2.2. Cài đặt ADB

Thực hiện các bước sau để cài đặt ADB trên hệ điều hành của bạn:

#### 2.2.1. Windows

1.  **Tải Platform Tools:** Truy cập trang [SDK Platform Tools release notes](https://developer.android.com/studio/releases/platform-tools) và tải xuống tệp ZIP mới nhất cho Windows.
2.  **Giải nén:** Giải nén tệp ZIP vào một vị trí cố định trên máy tính, ví dụ: `C:\platform-tools`.
3.  **Thêm vào PATH:**
    *   Nhấn phím `Windows`, gõ "environment variables" và chọn "Edit the system environment variables".
    *   Trong cửa sổ System Properties, nhấp vào nút "Environment Variables...".
    *   Trong phần "System variables" (hoặc "User variables" nếu bạn chỉ muốn cài đặt cho người dùng hiện tại), tìm biến `Path` và nhấp "Edit...".
    *   Nhấp "New" và dán đường dẫn đến thư mục bạn đã giải nén (ví dụ: `C:\platform-tools`).
    *   Nhấp "OK" trên tất cả các cửa sổ.
4.  **Khởi động lại Terminal:** Mở một cửa sổ Command Prompt hoặc PowerShell mới để thay đổi có hiệu lực.

#### 2.2.2. macOS

Cách đơn giản nhất là sử dụng [Homebrew](https://brew.sh/):

```bash
brew install --cask android-platform-tools
```

Homebrew sẽ tự động cài đặt và cấu hình PATH cho bạn.

#### 2.2.3. Linux (Debian/Ubuntu)

Sử dụng trình quản lý gói `apt`:

```bash
sudo apt update
sudo apt install android-tools-adb android-tools-fastboot
```

Lệnh này sẽ cài đặt cả `adb` và `fastboot`.

#### 2.2.4. Kiểm tra cài đặt ADB

Sau khi cài đặt, mở terminal hoặc command prompt mới và chạy lệnh:

```bash
adb version
```

Nếu bạn thấy thông tin phiên bản ADB hiển thị (ví dụ: `Android Debug Bridge version 1.0.41`), nghĩa là ADB đã được cài đặt thành công và có trong PATH.

### 2.3. Cài đặt OIADB

Chọn một trong các phương pháp sau để cài đặt thư viện OIADB:

#### 2.3.1. Cài đặt từ PyPI (Khuyến nghị)

Đây là cách cài đặt đơn giản và phổ biến nhất, sử dụng `pip`:

```bash
pip install oiadb
```

Lệnh này sẽ tải và cài đặt phiên bản ổn định mới nhất của OIADB từ Python Package Index (PyPI).

#### 2.3.2. Cài đặt với hỗ trợ Nhận diện Hình ảnh

Nếu bạn cần sử dụng các tính năng nhận diện hình ảnh, hãy cài đặt với phần phụ thuộc `[image]`:

```bash
pip install oiadb[image]
```

Lệnh này sẽ cài đặt OIADB cùng với `opencv-python` và `numpy`.

#### 2.3.3. Cài đặt từ Mã nguồn (Cho nhà phát triển)

Nếu bạn muốn cài đặt phiên bản mới nhất đang phát triển hoặc muốn đóng góp cho dự án, bạn có thể cài đặt trực tiếp từ kho GitHub:

1.  **Clone kho lưu trữ:**
    ```bash
    git clone https://github.com/tiendung2k03/oiadb.git
    ```
2.  **Di chuyển vào thư mục dự án:**
    ```bash
    cd oiadb
    ```
3.  **Cài đặt ở chế độ chỉnh sửa (editable mode):**
    ```bash
    pip install -e .
    ```
    Để cài đặt cả các phụ thuộc cho nhận diện hình ảnh:
    ```bash
    pip install -e .[image]
    ```
    Chế độ `-e` (editable) cho phép bạn chỉnh sửa mã nguồn và các thay đổi sẽ có hiệu lực ngay lập tức mà không cần cài đặt lại.

### 2.4. Thiết lập Thiết bị Android

Để OIADB (và ADB nói chung) có thể giao tiếp với thiết bị Android của bạn, bạn cần thực hiện một số cài đặt trên thiết bị:

#### 2.4.1. Bật Tùy chọn Nhà phát triển

1.  Mở **Cài đặt (Settings)** trên thiết bị Android.
2.  Cuộn xuống và chọn **Thông tin điện thoại (About phone)** hoặc **Thông tin máy tính bảng (About tablet)**.
3.  Tìm mục **Số bản dựng (Build number)**.
4.  **Nhấn liên tục 7 lần** vào mục **Số bản dựng**. Bạn sẽ thấy thông báo "Bạn hiện là nhà phát triển!" (You are now a developer!).

#### 2.4.2. Bật Gỡ lỗi USB

1.  Quay lại màn hình **Cài đặt** chính.
2.  Tìm và mở **Tùy chọn nhà phát triển (Developer options)** (thường nằm trong menu Hệ thống hoặc menu chính).
3.  Tìm và **bật** tùy chọn **Gỡ lỗi USB (USB debugging)**.
4.  Xác nhận cảnh báo bảo mật nếu có.

#### 2.4.3. Ủy quyền Kết nối ADB

1.  Kết nối thiết bị Android với máy tính bằng cáp USB.
2.  Trên thiết bị Android, bạn sẽ thấy một hộp thoại hỏi "Cho phép gỡ lỗi USB?" (Allow USB debugging?).
3.  **Đánh dấu** vào ô "Luôn cho phép từ máy tính này" (Always allow from this computer) để không phải xác nhận lại mỗi lần kết nối.
4.  Nhấn **OK** hoặc **Cho phép (Allow)**.

#### 2.4.4. Gỡ lỗi qua Wi-Fi (Tùy chọn)

Bạn cũng có thể kết nối ADB qua Wi-Fi thay vì USB:

1.  **Kết nối USB ban đầu:** Đảm bảo thiết bị và máy tính đang ở cùng một mạng Wi-Fi. Kết nối thiết bị với máy tính qua USB và đảm bảo ADB nhận diện được thiết bị (`adb devices`).
2.  **Tìm địa chỉ IP:**
    *   Trên thiết bị: Vào **Cài đặt > Wi-Fi > [Tên mạng đang kết nối]** hoặc **Cài đặt > Thông tin điện thoại > Trạng thái (Status)** để tìm địa chỉ IP của thiết bị (ví dụ: `192.168.1.100`).
    *   Hoặc chạy lệnh ADB: `adb shell ip addr show wlan0` (thay `wlan0` bằng tên giao diện mạng Wi-Fi nếu khác).
3.  **Bật chế độ TCP/IP:** Chạy lệnh ADB trên máy tính:
    ```bash
    adb tcpip 5555
    ```
    (Bạn có thể sử dụng cổng khác nếu muốn).
4.  **Ngắt kết nối USB.**
5.  **Kết nối qua Wi-Fi:** Chạy lệnh ADB trên máy tính:
    ```bash
    adb connect <địa_chỉ_ip_thiết_bị>:5555
    ```
    Ví dụ: `adb connect 192.168.1.100:5555`
6.  **Xác nhận kết nối:** Chạy lại `adb devices`. Bạn sẽ thấy thiết bị được liệt kê với địa chỉ IP.
7.  **Sử dụng trong OIADB:** Khi khởi tạo `MyADB`, bạn có thể chỉ định `device_id` là địa chỉ IP và cổng (ví dụ: `MyADB(device_id="192.168.1.100:5555")`) hoặc để OIADB tự động phát hiện.

### 2.5. Xác minh Cài đặt OIADB

Sau khi hoàn tất các bước trên, hãy chạy đoạn mã Python sau để kiểm tra xem OIADB có thể kết nối và tương tác với thiết bị của bạn hay không:

```python
from oiadb import MyADB
from oiadb.exceptions import DeviceNotFoundError, ADBError

try:
    # Khởi tạo OIADB (sẽ tự động tìm thiết bị nếu không chỉ định)
    print("Đang khởi tạo OIADB...")
    adb = MyADB()
    print(f"Đã kết nối với thiết bị: {adb.device_id}")

    # Lấy model thiết bị
    print("Đang lấy model thiết bị...")
    model = adb.run("shell getprop ro.product.model")
    print(f"Model thiết bị: {model.strip()}")

    print("\nCài đặt OIADB thành công!")

except DeviceNotFoundError:
    print("Lỗi: Không tìm thấy thiết bị Android nào được kết nối hoặc ủy quyền.")
    print("Vui lòng kiểm tra kết nối USB, bật Gỡ lỗi USB và ủy quyền máy tính.")
except ADBError as e:
    print(f"Lỗi ADB: {e}")
    print("Đảm bảo ADB đã được cài đặt đúng cách và có trong PATH.")
except Exception as e:
    print(f"Đã xảy ra lỗi không mong muốn: {e}")
```

Nếu mã chạy mà không có lỗi và in ra ID cùng model thiết bị của bạn, xin chúc mừng! Bạn đã cài đặt và thiết lập thành công OIADB.



---

## 3. Kiến trúc Thư viện

Phần này mô tả kiến trúc tổng thể của thư viện OIADB, giúp bạn hiểu rõ hơn về cách các thành phần khác nhau tương tác với nhau.

### 3.1. Tổng quan

OIADB được xây dựng theo kiến trúc module hóa, với các lớp và module đảm nhiệm các chức năng cụ thể. Trung tâm của thư viện là lớp `MyADB`, đóng vai trò là giao diện chính để người dùng tương tác. Lớp này sử dụng các module con trong `commands` và `utils` để thực hiện các tác vụ cụ thể.

Sơ đồ kiến trúc tổng quan:

```mermaid
graph TD
    A[Người dùng (Mã Python)] --> B(MyADB Class);
    B --> C{Commands Modules};
    B --> D{Utils Modules};
    C --> E[ADB Runner];
    D --> E;
    E --> F[ADB Executable];
    F <--> G[Thiết bị Android];
    D -- Optional --> H[OpenCV/NumPy];
    B -- Optional --> I[oiadb-server (trên thiết bị)];
    I <--> G;

    subgraph Core
        B
    end

    subgraph Functionality Modules
        C
        D
    end

    subgraph Execution Layer
        E
    end

    subgraph External Dependencies
        F
        H
        I
    end
```

*   **Người dùng (Mã Python):** Tương tác với thư viện thông qua việc khởi tạo và gọi các phương thức của lớp `MyADB`.
*   **Lớp MyADB:** Lớp chính, điều phối các yêu cầu, quản lý kết nối thiết bị, và gọi các module chức năng.
*   **Commands Modules:** Chứa các hàm được nhóm theo chức năng (ví dụ: `apps`, `file_ops`, `interaction`) để thực hiện các lệnh ADB cụ thể.
*   **Utils Modules:** Cung cấp các tiện ích hỗ trợ như chạy lệnh (`runner`), nhận diện hình ảnh (`image_recognition`), quản lý nền tảng (`platform_utils`), và các tính năng nâng cao (`advanced`).
*   **ADB Runner:** Thành phần nội bộ (thường là trong `utils.runner` hoặc trực tiếp trong `MyADB`) chịu trách nhiệm thực thi các lệnh `adb` thực tế thông qua `subprocess`.
*   **ADB Executable:** Công cụ dòng lệnh `adb` được cài đặt trên máy tính.
*   **Thiết bị Android:** Thiết bị vật lý hoặc giả lập mà ADB kết nối tới.
*   **OpenCV/NumPy:** Các thư viện bên ngoài, cần thiết cho tính năng nhận diện hình ảnh.
*   **oiadb-server:** Một ứng dụng Android nhỏ (APK) được OIADB tự động cài đặt lên thiết bị để hỗ trợ các tính năng nâng cao như XML Dump nhanh hơn hoặc các tương tác phức tạp (dựa trên kiến trúc của uiautomator2).

### 3.2. Cấu trúc Module

Cấu trúc thư mục chi tiết của thư viện (đã được liệt kê trong phần cài đặt) phản ánh rõ ràng kiến trúc module này:

*   **`adb.py`:** Chứa lớp `MyADB` chính.
*   **`exceptions.py`:** Định nghĩa các lớp ngoại lệ tùy chỉnh (ví dụ: `DeviceNotFoundError`, `ADBCommandError`).
*   **`commands/`:** Mỗi tệp `.py` trong thư mục này tương ứng với một nhóm lệnh logic:
    *   `apps.py`: Quản lý ứng dụng.
    *   `file_ops.py`: Thao tác file.
    *   `interaction.py`: Tương tác cơ bản (tap, swipe, keyevent).
    *   `image_interaction.py`: Tương tác dựa trên hình ảnh.
    *   `xml_dump.py`: Lấy và phân tích XML UI.
    *   ... (các module khác như `basic`, `connect`, `device_info`, etc.)
*   **`utils/`:** Chứa các module tiện ích:
    *   `runner.py`: Logic thực thi lệnh `adb`.
    *   `image_recognition.py`: Thuật toán nhận diện hình ảnh cốt lõi.
    *   `platform_utils.py`: Phát hiện hệ điều hành, tìm đường dẫn ADB.
    *   `advanced.py`: Cache, thực thi bất đồng bộ, theo dõi thiết bị.
    *   `adb_manager.py`: Tự động tải và quản lý ADB.
*   **`server/`:** Chứa mã nguồn hoặc tệp APK của `oiadb-server` (nếu có).

### 3.3. Luồng hoạt động chính

Một luồng hoạt động điển hình khi sử dụng OIADB diễn ra như sau:

1.  **Khởi tạo `MyADB`:** Người dùng tạo một instance của lớp `MyADB`, có thể chỉ định `device_id` hoặc để thư viện tự động chọn.
    *   Trong quá trình khởi tạo, `MyADB` sẽ:
        *   Xác định đường dẫn ADB (sử dụng `platform_utils`, có thể tự tải nếu cần với `adb_manager`).
        *   Kiểm tra kết nối ADB (`adb version`).
        *   Kiểm tra sự tồn tại của thiết bị (`adb devices`).
        *   (Tùy chọn) Tự động cài đặt/cập nhật và khởi động `oiadb-server` trên thiết bị, thiết lập port forwarding.
2.  **Gọi Phương thức/Lệnh:** Người dùng gọi một phương thức trên đối tượng `adb` (ví dụ: `adb.install_app(...)`) hoặc truy cập một module lệnh và gọi hàm của nó (ví dụ: `from oiadb.commands import apps; apps.install(...)` - cách này ít phổ biến hơn vì `MyADB` thường cung cấp các phương thức tiện lợi hơn).
3.  **Thực thi Lệnh:**
    *   Phương thức trong `MyADB` hoặc module `commands` sẽ xây dựng (các) lệnh `adb` tương ứng.
    *   Lệnh được chuyển đến `utils.runner` (hoặc logic thực thi nội bộ).
    *   `runner` sử dụng `subprocess` để thực thi lệnh `adb` với các tham số phù hợp (như `-s <device_id>`).
4.  **Xử lý Kết quả:**
    *   `runner` thu thập `stdout`, `stderr`, và `return_code` từ tiến trình `adb`.
    *   Kết quả được trả về cho lớp/module gọi.
    *   Kết quả có thể được xử lý thêm (ví dụ: phân tích chuỗi output để lấy thông tin cụ thể) trước khi trả về cho người dùng.
    *   Kết quả có thể được lưu vào cache (`utils.advanced.ResultCache`) nếu được bật.
5.  **Xử lý Lỗi:** Nếu lệnh `adb` thất bại (ví dụ: `return_code != 0`) hoặc xảy ra lỗi trong quá trình xử lý, một ngoại lệ OIADB cụ thể (từ `exceptions.py`) sẽ được ném ra (ví dụ: `ADBCommandError`, `PackageNotFoundError`).

### 3.4. Xử lý Lỗi và Ngoại lệ

OIADB định nghĩa một hệ thống các lớp ngoại lệ tùy chỉnh trong `exceptions.py` để cung cấp thông tin chi tiết hơn về các lỗi có thể xảy ra. Các ngoại lệ chính bao gồm:

*   **`ADBError`:** Lỗi chung liên quan đến ADB (ví dụ: không tìm thấy ADB, server không phản hồi).
*   **`ADBCommandError`:** Lỗi xảy ra khi thực thi một lệnh ADB cụ thể (thường là do `return_code != 0`). Chứa thông tin về lệnh, `stdout`, `stderr`.
*   **`DeviceNotFoundError`:** Không tìm thấy thiết bị được chỉ định hoặc không có thiết bị nào kết nối.
*   **`DeviceConnectionError`:** Lỗi trong quá trình kết nối với thiết bị (ví dụ: ủy quyền thất bại).
*   **`PackageNotFoundError`:** Không tìm thấy gói ứng dụng được chỉ định trên thiết bị.
*   **`InstallationError`:** Lỗi trong quá trình cài đặt ứng dụng.
*   **`UninstallationError`:** Lỗi trong quá trình gỡ cài đặt ứng dụng.
*   **`FileOperationError`:** Lỗi khi thực hiện thao tác file (push, pull, rm...).
*   **`ImageNotFoundError`:** (Có thể có) Lỗi khi không tìm thấy hình ảnh mẫu (trong `image_interaction`).

Việc sử dụng các ngoại lệ cụ thể này giúp người dùng viết mã xử lý lỗi (`try...except`) một cách chính xác và hiệu quả hơn.



---

## 4. Lớp MyADB - Cốt lõi Tương tác

Lớp `MyADB` là trái tim của thư viện OIADB. Nó đóng vai trò là điểm truy cập chính cho hầu hết các chức năng, quản lý kết nối đến thiết bị Android và điều phối việc thực thi các lệnh ADB.

### 4.1. Khởi tạo và Cấu hình

Việc đầu tiên khi sử dụng OIADB là tạo một instance của lớp `MyADB`.

```python
from oiadb import MyADB
from oiadb.exceptions import DeviceNotFoundError, ADBError

try:
    # Khởi tạo đơn giản, tự động tìm thiết bị đầu tiên
    adb_instance_1 = MyADB()
    print(f"Kết nối thành công với thiết bị: {adb_instance_1.device_id}")

    # Khởi tạo với ID thiết bị cụ thể (ví dụ: từ output của 'adb devices')
    # device_serial = "emulator-5554" # Hoặc "192.168.1.100:5555" nếu kết nối qua Wi-Fi
    # adb_instance_2 = MyADB(device_id=device_serial)
    # print(f"Kết nối thành công với thiết bị: {adb_instance_2.device_id}")

    # Khởi tạo với các tùy chọn cấu hình khác
    adb_instance_3 = MyADB(
        cache_enabled=False,      # Tắt cache kết quả lệnh
        timeout=60,               # Tăng thời gian chờ lệnh lên 60 giây
        adb_path="/usr/local/bin/adb", # Chỉ định đường dẫn ADB tùy chỉnh
        auto_start_server=False,  # Không tự động cài đặt/khởi động oiadb-server
        auto_install_adb=False    # Không tự động tải ADB nếu không tìm thấy
    )
    print(f"Kết nối thành công với thiết bị: {adb_instance_3.device_id}")

except DeviceNotFoundError:
    print("Lỗi: Không tìm thấy thiết bị nào.")
except ADBError as e:
    print(f"Lỗi ADB: {e}")
except Exception as e:
    print(f"Lỗi không mong muốn: {e}")
```

**Các tham số khởi tạo (`__init__`) quan trọng:**

*   `device_id` (Optional[str], default=None): ID (serial number hoặc `ip:port`) của thiết bị mục tiêu. Nếu là `None`, OIADB sẽ cố gắng kết nối với thiết bị đầu tiên tìm thấy trong danh sách `adb devices`.
*   `cache_enabled` (bool, default=True): Bật hoặc tắt cơ chế cache kết quả lệnh. Khi bật, các lệnh giống hệt nhau được thực thi trong một khoảng thời gian ngắn (mặc định 60 giây) sẽ trả về kết quả đã lưu thay vì thực thi lại, giúp tăng tốc độ đáng kể cho các lệnh lấy thông tin.
*   `timeout` (int, default=30): Thời gian chờ tối đa (tính bằng giây) cho một lệnh ADB hoàn thành trước khi bị coi là thất bại (timeout).
*   `adb_path` (Optional[str], default=None): Cho phép chỉ định đường dẫn tuyệt đối đến tệp thực thi `adb`. Nếu là `None`, OIADB sẽ cố gắng tự động tìm ADB trong PATH hệ thống hoặc tự động tải xuống (nếu `auto_install_adb=True`).
*   `auto_start_server` (bool, default=True): Nếu `True`, OIADB sẽ tự động kiểm tra, cài đặt (nếu cần) và khởi động `oiadb-server.apk` trên thiết bị khi khởi tạo `MyADB`. Server này cần thiết cho một số tính năng nâng cao như XML Dump.
*   `auto_install_adb` (bool, default=True): Nếu `True` và không tìm thấy ADB trong PATH hoặc `adb_path` không hợp lệ, OIADB sẽ cố gắng tự động tải xuống và cài đặt phiên bản ADB phù hợp cho hệ điều hành hiện tại.

**Các thuộc tính (Attributes) quan trọng của instance `MyADB`:**

*   `device_id` (str): ID của thiết bị đang được kết nối.
*   `adb_path` (str): Đường dẫn đến tệp thực thi ADB đang được sử dụng.
*   `platform_info` (PlatformInfo): Đối tượng chứa thông tin về hệ điều hành hiện tại.
*   `timeout` (int): Giá trị timeout đang được sử dụng.
*   `cache_enabled` (bool): Trạng thái của cache.
*   `_cache` (ResultCache | None): Instance của lớp cache (nếu được bật).
*   `_async_executor` (AsyncCommandExecutor): Instance để thực thi lệnh bất đồng bộ.
*   `local_server_port` (int | None): Cổng cục bộ được sử dụng để chuyển tiếp (forward) đến `oiadb-server` trên thiết bị (nếu server được khởi động).

### 4.2. Các Phương thức Chính

Lớp `MyADB` cung cấp một số phương thức cốt lõi để thực thi lệnh và quản lý thiết bị. Nhiều chức năng chi tiết hơn được ủy quyền cho các module trong `commands` và `utils`, nhưng các phương thức sau đây thường được sử dụng trực tiếp:

*   **`run(command: str, use_cache: bool = True) -> str`:**
    *   **Mô tả:** Thực thi một lệnh ADB tùy chỉnh và trả về kết quả `stdout` dưới dạng chuỗi. Đây là phương thức nền tảng cho hầu hết các tương tác ADB.
    *   **Tham số:**
        *   `command`: Chuỗi lệnh ADB cần thực thi (phần sau `adb -s <device_id>`). Ví dụ: `"shell getprop ro.product.model"`, `"logcat -d"`.
        *   `use_cache`: Có sử dụng cache cho lệnh này hay không (chỉ có hiệu lực nếu `cache_enabled=True` khi khởi tạo).
    *   **Trả về:** Chuỗi `stdout` của lệnh nếu thành công.
    *   **Ngoại lệ:** Ném ra `ADBCommandError` nếu lệnh thất bại (return code != 0) hoặc các ngoại lệ khác như `DeviceNotFoundError`.
    *   **Ví dụ:**
        ```python
        try:
            model = adb.run("shell getprop ro.product.model")
            print(f"Model: {model.strip()}")
            # Lấy log gần đây, không dùng cache
            logs = adb.run("logcat -d -t 50", use_cache=False)
            print(f"Logs:\n{logs}")
        except ADBCommandError as e:
            print(f"Lỗi khi chạy lệnh '{e.command}': {e.stderr}")
        ```

*   **`run_async(command: str, command_id: Optional[str] = None, callback: Optional[Callable] = None) -> str`:**
    *   **Mô tả:** Thực thi một lệnh ADB bất đồng bộ (không chặn luồng chính). Hữu ích cho các lệnh chạy dài như `logcat` liên tục hoặc theo dõi sự kiện.
    *   **Tham số:**
        *   `command`: Chuỗi lệnh ADB cần thực thi.
        *   `command_id` (Optional): ID duy nhất để quản lý tiến trình bất đồng bộ. Nếu `None`, một ID ngẫu nhiên sẽ được tạo.
        *   `callback` (Optional): Một hàm sẽ được gọi khi lệnh hoàn thành. Hàm callback nhận một tham số là đối tượng `CommandResult`.
    *   **Trả về:** `command_id` được sử dụng cho lệnh.
    *   **Ví dụ:**
        ```python
        def log_handler(result: CommandResult):
            if result.success:
                print(f"Logcat output:\n{result.stdout}")
            else:
                print(f"Logcat error: {result.stderr}")

        cmd_id = adb.run_async("logcat -d", callback=log_handler)
        print(f"Đã bắt đầu logcat với ID: {cmd_id}")
        # ... (làm việc khác trong khi logcat chạy)
        # Có thể kiểm tra trạng thái: adb._async_executor.is_running(cmd_id)
        # Hoặc lấy kết quả sau: result = adb._async_executor.get_result(cmd_id)
        ```

*   **`get_devices_list() -> List[str]`:**
    *   **Mô tả:** Trả về danh sách các ID của tất cả thiết bị đang được kết nối và nhận diện bởi ADB trên máy tính.
    *   **Trả về:** List các chuỗi device ID.
    *   **Ví dụ:**
        ```python
        connected_devices = adb.get_devices_list()
        print(f"Các thiết bị đang kết nối: {connected_devices}")
        ```

*   **`push_file(local_path: str, remote_path: str) -> bool`:**
    *   **Mô tả:** Đẩy (sao chép) một file hoặc thư mục từ máy tính cục bộ lên thiết bị Android.
    *   **Tham số:**
        *   `local_path`: Đường dẫn đến file/thư mục trên máy tính.
        *   `remote_path`: Đường dẫn đích trên thiết bị Android.
    *   **Trả về:** `True` nếu thành công, `False` nếu thất bại.
    *   **Ngoại lệ:** `FileOperationError` nếu có lỗi.
    *   **Ví dụ:**
        ```python
        if adb.push_file("./my_script.sh", "/data/local/tmp/script.sh"):
            print("Đẩy file thành công!")
        ```

*   **`pull_file(remote_path: str, local_path: str) -> bool`:**
    *   **Mô tả:** Kéo (sao chép) một file hoặc thư mục từ thiết bị Android về máy tính cục bộ.
    *   **Tham số:**
        *   `remote_path`: Đường dẫn đến file/thư mục trên thiết bị Android.
        *   `local_path`: Đường dẫn đích trên máy tính.
    *   **Trả về:** `True` nếu thành công, `False` nếu thất bại.
    *   **Ngoại lệ:** `FileOperationError` nếu có lỗi.
    *   **Ví dụ:**
        ```python
        if adb.pull_file("/sdcard/DCIM/Camera/image.jpg", "./downloaded_image.jpg"):
            print("Kéo file thành công!")
        ```

*   **`take_screenshot(output_path: Optional[str] = None, as_bytes: bool = False) -> Union[str, bytes]`:**
    *   **Mô tả:** Chụp ảnh màn hình thiết bị.
    *   **Tham số:**
        *   `output_path` (Optional): Đường dẫn để lưu file ảnh PNG trên máy tính. Nếu `None` và `as_bytes=False`, ảnh sẽ được lưu vào một đường dẫn tạm thời.
        *   `as_bytes` (bool): Nếu `True`, trả về dữ liệu ảnh dưới dạng bytes thay vì lưu vào file. `output_path` sẽ bị bỏ qua.
    *   **Trả về:** Đường dẫn đến file ảnh đã lưu (nếu `as_bytes=False`) hoặc đối tượng `bytes` chứa dữ liệu ảnh PNG (nếu `as_bytes=True`).
    *   **Ngoại lệ:** `ADBCommandError` nếu chụp ảnh thất bại.
    *   **Ví dụ:**
        ```python
        # Lưu vào file
        saved_path = adb.take_screenshot("./screenshot.png")
        print(f"Ảnh màn hình đã lưu tại: {saved_path}")

        # Lấy dữ liệu bytes
        image_bytes = adb.take_screenshot(as_bytes=True)
        # (Có thể dùng PIL hoặc thư viện khác để xử lý image_bytes)
        # from PIL import Image
        # import io
        # img = Image.open(io.BytesIO(image_bytes))
        # img.show()
        ```

*   **`get_screen_size() -> Dict[str, int]`:**
    *   **Mô tả:** Lấy kích thước màn hình (chiều rộng và chiều cao) của thiết bị.
    *   **Trả về:** Dictionary dạng `{"width": <int>, "height": <int>}`.
    *   **Ví dụ:**
        ```python
        size = adb.get_screen_size()
        print(f"Kích thước màn hình: {size['width']}x{size['height']}")
        ```

### 4.3. Tự động Cài đặt và Quản lý Server

Một trong những tính năng tiện lợi của OIADB là khả năng tự động quản lý `oiadb-server` trên thiết bị. Server này là một ứng dụng Android nhỏ (dựa trên instrumentation test runner) cần thiết cho một số tính năng nâng cao, đặc biệt là `xml_dump` để lấy cấu trúc UI một cách hiệu quả.

Khi bạn khởi tạo `MyADB` với `auto_start_server=True` (mặc định), các bước sau sẽ tự động diễn ra:

1.  **Kiểm tra Server:** OIADB kiểm tra xem `oiadb-server` (cả gói chính và gói test) đã được cài đặt trên thiết bị chưa.
2.  **Cài đặt/Cập nhật:** Nếu server chưa được cài đặt hoặc có phiên bản cũ hơn (logic kiểm tra phiên bản có thể được cải thiện trong tương lai), OIADB sẽ:
    *   Tìm tệp `oiadb-server.apk` được đóng gói sẵn trong thư viện OIADB.
    *   Đẩy tệp APK lên thư mục tạm trên thiết bị.
    *   Thực thi lệnh `pm install` để cài đặt hoặc cập nhật server.
    *   Xóa tệp APK tạm trên thiết bị.
3.  **Khởi động Server:** OIADB thực thi lệnh `am instrument` để khởi động instrumentation test runner của `oiadb-server` ở chế độ nền.
4.  **Thiết lập Port Forwarding:** OIADB tìm một cổng cục bộ trống trên máy tính và thiết lập chuyển tiếp cổng ADB (`adb forward`) từ cổng cục bộ đó đến cổng mà `oiadb-server` đang lắng nghe trên thiết bị (mặc định là 9008).
5.  **Kiểm tra Kết nối Server:** OIADB gửi một yêu cầu `ping` đến server thông qua cổng đã chuyển tiếp để đảm bảo server đang chạy và sẵn sàng nhận lệnh.

Toàn bộ quá trình này giúp đơn giản hóa việc sử dụng các tính năng phụ thuộc vào server. Nếu có lỗi xảy ra trong quá trình này (ví dụ: cài đặt thất bại, server không khởi động), một ngoại lệ `ADBError` sẽ được ném ra.

Bạn có thể tắt tính năng này bằng cách đặt `auto_start_server=False` khi khởi tạo `MyADB` nếu bạn muốn quản lý server thủ công hoặc không cần các tính năng phụ thuộc vào nó.

### 4.4. Ví dụ Sử dụng Cơ bản

```python
from oiadb import MyADB
from oiadb.exceptions import ADBError, DeviceNotFoundError

try:
    # Kết nối với thiết bị đầu tiên tìm thấy
    adb = MyADB()
    print(f"Đã kết nối: {adb.device_id}")

    # Lấy một số thông tin cơ bản
    model = adb.run("shell getprop ro.product.model").strip()
    version = adb.run("shell getprop ro.build.version.release").strip()
    size = adb.get_screen_size()
    print(f"Thiết bị: {model}, Android {version}, Màn hình: {size['width']}x{size['height']}")

    # Chụp ảnh màn hình
    screenshot_file = adb.take_screenshot("current_screen.png")
    print(f"Đã chụp màn hình: {screenshot_file}")

    # Đẩy một file text lên thiết bị
    with open("hello.txt", "w") as f:
        f.write("Xin chào từ OIADB!")
    if adb.push_file("hello.txt", "/sdcard/hello_oiadb.txt"):
        print("Đã đẩy file 'hello.txt' lên /sdcard/")
        # Kiểm tra nội dung file trên thiết bị
        content = adb.run("shell cat /sdcard/hello_oiadb.txt")
        print(f"Nội dung file trên thiết bị: {content.strip()}")
        # Xóa file trên thiết bị
        adb.run("shell rm /sdcard/hello_oiadb.txt")
        print("Đã xóa file trên thiết bị.")

except DeviceNotFoundError:
    print("Lỗi: Không tìm thấy thiết bị.")
except ADBError as e:
    print(f"Lỗi ADB: {e}")
except Exception as e:
    print(f"Lỗi không mong muốn: {e}")
```



---

## 5. Module Commands - Bộ lệnh Chi tiết

Module `commands` là nơi tập hợp các chức năng chính của OIADB, được tổ chức thành các tệp Python riêng biệt tương ứng với từng nhóm tác vụ cụ thể. Điều này giúp mã nguồn trở nên rõ ràng, dễ bảo trì và mở rộng.

Để sử dụng các lệnh này, bạn thường sẽ gọi các phương thức tương ứng trên instance `MyADB` đã khởi tạo. Lớp `MyADB` đóng vai trò là facade, ủy quyền các lệnh đến các hàm/lớp phù hợp trong module `commands`.

```python
from oiadb import MyADB

adb = MyADB()

# Ví dụ: Gọi lệnh cài đặt ứng dụng (sử dụng logic trong commands/apps.py)
# adb.install_app("path/to/app.apk") 

# Ví dụ: Gọi lệnh lấy thông tin model (sử dụng logic trong commands/device_info.py)
# model = adb.get_device_model() 
```

Trong phần này, chúng ta sẽ đi sâu vào từng module lệnh con, giải thích chức năng và cách sử dụng của chúng.

### 5.1. `app_info`: Lấy Thông tin Ứng dụng

Module này cung cấp các hàm cơ bản để truy vấn thông tin về các gói (packages) ứng dụng đã cài đặt trên thiết bị.

**Vị trí:** `oiadb/commands/app_info.py`

**Các hàm chính:**

*   **`list_packages() -> str`:**
    *   **Mô tả:** Liệt kê tất cả các gói ứng dụng (cả hệ thống và bên thứ ba) đã cài đặt trên thiết bị.
    *   **Tương đương ADB:** `adb shell pm list packages`
    *   **Trả về:** Chuỗi chứa danh sách các tên gói, mỗi gói trên một dòng (ví dụ: `package:com.example.app`).

*   **`list_packages_r() -> str`:**
    *   **Mô tả:** Liệt kê tất cả các gói và đường dẫn đến tệp APK của chúng.
    *   **Tương đương ADB:** `adb shell pm list packages -r` (Lưu ý: Lệnh gốc là `pm list packages -f`, `-r` không phải là tùy chọn chuẩn cho `list packages` nhưng có thể thư viện đã tùy chỉnh hoặc có sự nhầm lẫn trong mã gốc).
    *   **Trả về:** Chuỗi chứa danh sách các gói và đường dẫn APK.

*   **`list_packages_3rd() -> str`:**
    *   **Mô tả:** Chỉ liệt kê các gói ứng dụng của bên thứ ba (đã được người dùng cài đặt).
    *   **Tương đương ADB:** `adb shell pm list packages -3`
    *   **Trả về:** Chuỗi chứa danh sách tên gói của bên thứ ba.

*   **`list_packages_sys() -> str`:**
    *   **Mô tả:** Chỉ liệt kê các gói ứng dụng hệ thống.
    *   **Tương đương ADB:** `adb shell pm list packages -s`
    *   **Trả về:** Chuỗi chứa danh sách tên gói hệ thống.

*   **`list_packages_uninstalled() -> str`:**
    *   **Mô tả:** Liệt kê các gói đã được gỡ cài đặt nhưng vẫn còn giữ lại dữ liệu (thường ít gặp).
    *   **Tương đương ADB:** `adb shell pm list packages -u`
    *   **Trả về:** Chuỗi chứa danh sách tên gói đã gỡ cài đặt còn dữ liệu.

*   **`dumpsys_package() -> str`:**
    *   **Mô tả:** Lấy thông tin chi tiết về tất cả các gói trên hệ thống bằng cách sử dụng `dumpsys`. Kết quả trả về rất lớn và chi tiết.
    *   **Tương đương ADB:** `adb shell dumpsys package packages`
    *   **Trả về:** Chuỗi lớn chứa thông tin chi tiết của tất cả các gói.

*   **`dump(name: str) -> str`:**
    *   **Mô tả:** Lấy thông tin chi tiết về một gói ứng dụng cụ thể bằng `dumpsys`.
    *   **Tham số:**
        *   `name`: Tên gói ứng dụng cần lấy thông tin (ví dụ: `"com.android.settings"`).
    *   **Tương đương ADB:** `adb shell dumpsys package <name>`
    *   **Trả về:** Chuỗi chứa thông tin chi tiết của gói được chỉ định.
    *   **Ngoại lệ:** `ADBCommandError` nếu gói không tồn tại hoặc có lỗi khác.

*   **`apk_path(package: str) -> str`:**
    *   **Mô tả:** Lấy đường dẫn đầy đủ đến tệp APK gốc của một gói ứng dụng đã cài đặt.
    *   **Tham số:**
        *   `package`: Tên gói ứng dụng (ví dụ: `"com.google.android.youtube"`).
    *   **Tương đương ADB:** `adb shell pm path <package>`
    *   **Trả về:** Chuỗi chứa đường dẫn đến tệp APK (ví dụ: `package:/data/app/com.google.android.youtube-1/base.apk`).
    *   **Ngoại lệ:** `ADBCommandError` nếu gói không tồn tại.

**Ví dụ sử dụng:**

```python
from oiadb import MyADB
from oiadb.commands import app_info # Có thể truy cập trực tiếp nếu muốn

try:
    adb = MyADB()

    # Lấy danh sách tất cả các gói
    all_packages_str = adb.run("shell pm list packages") # Hoặc dùng app_info.list_packages()
    # print("Tất cả các gói:\n", all_packages_str)

    # Lấy danh sách gói bên thứ ba
    third_party_packages = app_info.list_packages_3rd()
    print("Các gói bên thứ ba:")
    for pkg in third_party_packages.splitlines():
        if pkg.startswith("package:"):
            print(f"- {pkg.replace('package:', '')}")

    # Lấy đường dẫn APK của ứng dụng Cài đặt
    settings_pkg = "com.android.settings"
    settings_path = app_info.apk_path(settings_pkg)
    print(f"\nĐường dẫn APK của {settings_pkg}: {settings_path.replace('package:', '').strip()}")

    # Lấy thông tin chi tiết của ứng dụng Cài đặt
    # settings_dump = app_info.dump(settings_pkg)
    # print(f"\nThông tin chi tiết {settings_pkg}:\n{settings_dump[:500]}...") # In 500 ký tự đầu

except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")

```

**Lưu ý:** Các hàm trong module này chủ yếu trả về chuỗi output thô từ lệnh ADB. Bạn có thể cần phải xử lý (parse) chuỗi này để trích xuất thông tin cụ thể mà bạn cần (ví dụ: tách tên gói từ chuỗi `package:com.example.app`). Lớp `MyADB` hoặc các module khác có thể cung cấp các phương thức tiện lợi hơn đã xử lý sẵn output này (ví dụ: `adb.is_app_installed(package_name)` thay vì tự parse output của `list_packages`).




### 5.2. `apps`: Quản lý Vòng đời Ứng dụng

Module này tập trung vào các hành động liên quan đến việc quản lý trạng thái và vòng đời của các ứng dụng trên thiết bị, bao gồm cài đặt, gỡ bỏ, khởi chạy, dừng, và quản lý dữ liệu.

**Vị trí:** `oiadb/commands/apps.py` (Thường được đóng gói trong lớp `AppCommands`)

**Các hàm/phương thức chính (trong lớp `AppCommands`):**

*   **`install(apk_path: str, replace: bool = False, grant_permissions: bool = False, downgrade: bool = False, allow_test_packages: bool = False) -> str`:**
    *   **Mô tả:** Cài đặt một ứng dụng từ tệp APK cục bộ.
    *   **Tham số:**
        *   `apk_path`: Đường dẫn đến tệp APK trên máy tính.
        *   `replace` (bool): Cho phép thay thế ứng dụng nếu đã tồn tại (`-r`).
        *   `grant_permissions` (bool): Tự động cấp tất cả các quyền được yêu cầu trong manifest (`-g`).
        *   `downgrade` (bool): Cho phép cài đặt phiên bản cũ hơn phiên bản hiện tại (`-d`).
        *   `allow_test_packages` (bool): Cho phép cài đặt các gói được đánh dấu là test (`-t`).
    *   **Tương đương ADB:** `adb install [-r] [-g] [-d] [-t] <apk_path>`
    *   **Trả về:** Chuỗi output từ lệnh `adb install`.
    *   **Ngoại lệ:** `InstallationError` nếu tệp APK không tồn tại hoặc quá trình cài đặt thất bại.

*   **`install_multiple(apk_paths: List[str], replace: bool = False, grant_permissions: bool = False) -> str`:**
    *   **Mô tả:** Cài đặt ứng dụng từ nhiều tệp APK (split APKs).
    *   **Tham số:**
        *   `apk_paths`: Danh sách các đường dẫn đến tệp APK thành phần.
        *   `replace` (bool): Tương tự `install` (`-r`).
        *   `grant_permissions` (bool): Tương tự `install` (`-g`).
    *   **Tương đương ADB:** `adb install-multiple [-r] [-g] <apk_path1> <apk_path2> ...`
    *   **Trả về:** Chuỗi output từ lệnh `adb install-multiple`.
    *   **Ngoại lệ:** `InstallationError` nếu có lỗi.

*   **`uninstall(package_name: str, keep_data: bool = False) -> str`:**
    *   **Mô tả:** Gỡ cài đặt một ứng dụng khỏi thiết bị.
    *   **Tham số:**
        *   `package_name`: Tên gói của ứng dụng cần gỡ.
        *   `keep_data` (bool): Giữ lại dữ liệu và thư mục cache của ứng dụng sau khi gỡ (`-k`).
    *   **Tương đương ADB:** `adb uninstall [-k] <package_name>`
    *   **Trả về:** Chuỗi output từ lệnh `adb uninstall`.
    *   **Ngoại lệ:** `UninstallationError` nếu gỡ cài đặt thất bại.

*   **`list_packages(filter_type: Optional[str] = None) -> List[str]`:**
    *   **Mô tả:** Liệt kê các gói ứng dụng đã cài đặt, có thể lọc theo loại.
    *   **Tham số:**
        *   `filter_type`: Loại bộ lọc:
            *   `None`: Liệt kê tất cả các gói.
            *   `"system"`: Chỉ gói hệ thống (`-s`).
            *   `"third-party"`: Chỉ gói bên thứ ba (`-3`).
            *   `"disabled"`: Chỉ gói bị vô hiệu hóa (`-d`).
            *   `"enabled"`: Chỉ gói đang được kích hoạt (`-e`).
    *   **Tương đương ADB:** `adb shell pm list packages [-s | -3 | -d | -e]`
    *   **Trả về:** Danh sách (List) các chuỗi tên gói (đã loại bỏ tiền tố `package:`).

*   **`clear_app_data(package_name: str) -> str`:**
    *   **Mô tả:** Xóa toàn bộ dữ liệu người dùng và cache của một ứng dụng. Tương tự như việc vào Cài đặt > Ứng dụng > [Tên ứng dụng] > Lưu trữ > Xóa dữ liệu.
    *   **Tham số:** `package_name`: Tên gói của ứng dụng.
    *   **Tương đương ADB:** `adb shell pm clear <package_name>`
    *   **Trả về:** Chuỗi output từ lệnh `pm clear`.

*   **`force_stop(package_name: str) -> str`:**
    *   **Mô tả:** Buộc dừng tất cả các tiến trình liên quan đến một ứng dụng.
    *   **Tham số:** `package_name`: Tên gói của ứng dụng.
    *   **Tương đương ADB:** `adb shell am force-stop <package_name>`
    *   **Trả về:** Chuỗi output từ lệnh `am force-stop`.

*   **`start_app(package_name: str, activity: Optional[str] = None) -> str`:**
    *   **Mô tả:** Khởi chạy một ứng dụng. Có thể chỉ định một Activity cụ thể để khởi chạy, hoặc nếu không, sẽ cố gắng khởi chạy Activity mặc định (LAUNCHER).
    *   **Tham số:**
        *   `package_name`: Tên gói của ứng dụng.
        *   `activity` (Optional): Tên đầy đủ của Activity cần khởi chạy (ví dụ: `.MainActivity`, `com.example.app.SpecificActivity`). Nếu `None`, sử dụng lệnh `monkey` để tìm và chạy LAUNCHER activity.
    *   **Tương đương ADB:**
        *   Với activity: `adb shell am start -n <package_name>/<activity>`
        *   Không có activity: `adb shell monkey -p <package_name> -c android.intent.category.LAUNCHER 1`
    *   **Trả về:** Chuỗi output từ lệnh `am start` hoặc `monkey`.

*   **`get_app_version(package_name: str) -> str`:**
    *   **Mô tả:** Lấy chuỗi phiên bản (versionName) của ứng dụng.
    *   **Tham số:** `package_name`: Tên gói của ứng dụng.
    *   **Trả về:** Chuỗi versionName (ví dụ: "1.2.3").
    *   **Ngoại lệ:** `PackageNotFoundError` nếu gói không tồn tại hoặc không tìm thấy versionName.

*   **`is_app_installed(package_name: str) -> bool`:**
    *   **Mô tả:** Kiểm tra xem một ứng dụng có được cài đặt trên thiết bị hay không.
    *   **Tham số:** `package_name`: Tên gói của ứng dụng.
    *   **Trả về:** `True` nếu ứng dụng đã cài đặt, `False` nếu không.

*   **`get_app_path(package_name: str) -> str`:**
    *   **Mô tả:** Lấy đường dẫn đầy đủ đến tệp APK gốc của ứng dụng trên thiết bị.
    *   **Tham số:** `package_name`: Tên gói của ứng dụng.
    *   **Trả về:** Chuỗi đường dẫn đến tệp APK (đã loại bỏ tiền tố `package:`).
    *   **Ngoại lệ:** `PackageNotFoundError` nếu gói không tồn tại.

*   **`get_app_info(package_name: str) -> Dict[str, Any]`:**
    *   **Mô tả:** Lấy thông tin chi tiết về một ứng dụng bằng cách phân tích output của `dumpsys package`.
    *   **Tham số:** `package_name`: Tên gói của ứng dụng.
    *   **Trả về:** Một dictionary chứa các thông tin như `version_name`, `version_code`, `first_install_time`, `last_update_time`, `installer`, `uid`, `target_sdk`, và danh sách các quyền đã cấp (`permissions`).
    *   **Ngoại lệ:** `PackageNotFoundError` nếu gói không tồn tại.

*   **`get_running_apps() -> List[str]`:**
    *   **Mô tả:** Cố gắng lấy danh sách các gói ứng dụng đang chạy bằng cách phân tích output của `ps`.
    *   **Trả về:** Danh sách (List) các chuỗi tên gói có vẻ đang chạy. Lưu ý: Phương pháp này có thể không hoàn toàn chính xác.

*   **`get_app_activities(package_name: str) -> List[str]`:**
    *   **Mô tả:** Lấy danh sách các Activity được đăng ký bởi một ứng dụng từ output của `dumpsys package`.
    *   **Tham số:** `package_name`: Tên gói của ứng dụng.
    *   **Trả về:** Danh sách (List) các chuỗi tên Activity (thường có dạng `com.package.name/.ActivityName`).
    *   **Ngoại lệ:** `PackageNotFoundError` nếu gói không tồn tại.

*   **`grant_permission(package_name: str, permission: str) -> str`:**
    *   **Mô tả:** Cấp một quyền cụ thể cho ứng dụng (chỉ hoạt động trên các phiên bản Android và quyền nhất định).
    *   **Tham số:**
        *   `package_name`: Tên gói của ứng dụng.
        *   `permission`: Tên quyền cần cấp (ví dụ: `android.permission.CAMERA`).
    *   **Tương đương ADB:** `adb shell pm grant <package_name> <permission>`
    *   **Trả về:** Chuỗi output từ lệnh `pm grant`.

*   **`revoke_permission(package_name: str, permission: str) -> str`:**
    *   **Mô tả:** Thu hồi một quyền cụ thể của ứng dụng.
    *   **Tham số:**
        *   `package_name`: Tên gói của ứng dụng.
        *   `permission`: Tên quyền cần thu hồi.
    *   **Tương đương ADB:** `adb shell pm revoke <package_name> <permission>`
    *   **Trả về:** Chuỗi output từ lệnh `pm revoke`.

*   **`disable_app(package_name: str) -> str`:**
    *   **Mô tả:** Vô hiệu hóa một ứng dụng (ngăn không cho chạy, ẩn khỏi launcher). Thường dùng cho ứng dụng hệ thống.
    *   **Tham số:** `package_name`: Tên gói của ứng dụng.
    *   **Tương đương ADB:** `adb shell pm disable-user <package_name>` (hoặc `pm disable` trên các phiên bản cũ).
    *   **Trả về:** Chuỗi output từ lệnh.

*   **`enable_app(package_name: str) -> str`:**
    *   **Mô tả:** Kích hoạt lại một ứng dụng đã bị vô hiệu hóa.
    *   **Tham số:** `package_name`: Tên gói của ứng dụng.
    *   **Tương đương ADB:** `adb shell pm enable <package_name>`
    *   **Trả về:** Chuỗi output từ lệnh.

**Ví dụ sử dụng:**

```python
from oiadb import MyADB
from oiadb.exceptions import InstallationError, PackageNotFoundError

try:
    adb = MyADB()
    package = "com.android.calculator2" # Gói máy tính mặc định

    # Kiểm tra xem đã cài đặt chưa
    if adb.is_app_installed(package):
        print(f"Ứng dụng {package} đã được cài đặt.")
        
        # Lấy thông tin
        info = adb.get_app_info(package)
        print(f"  Version: {info.get("version_name")}")
        print(f"  Path: {adb.get_app_path(package)}")

        # Dừng ứng dụng
        print("Đang dừng ứng dụng...")
        adb.force_stop(package)

        # Xóa dữ liệu (Cẩn thận khi chạy lệnh này!)
        # print("Đang xóa dữ liệu...")
        # adb.clear_app_data(package)

        # Khởi chạy lại
        print("Đang khởi chạy ứng dụng...")
        adb.start_app(package)
        
    else:
        print(f"Ứng dụng {package} chưa được cài đặt.")
        # Thử cài đặt nếu có file APK
        # try:
        #     adb.install("path/to/calculator.apk", grant_permissions=True)
        #     print("Cài đặt thành công!")
        # except InstallationError as e:
        #     print(f"Cài đặt thất bại: {e}")
        # except FileNotFoundError:
        #     print("Không tìm thấy file APK để cài đặt.")

except PackageNotFoundError as e:
    print(f"Lỗi: Không tìm thấy gói {e.package_name}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
```




### 5.3. `basic`: Các Lệnh ADB Cơ bản

Module này chứa các hàm tương ứng với những lệnh ADB cơ bản nhất, thường dùng để quản lý server ADB, kết nối thiết bị và thực hiện các hành động chung.

**Vị trí:** `oiadb/commands/basic.py`

**Các hàm chính:**

*   **`devices() -> str`:**
    *   **Mô tả:** Liệt kê các thiết bị đang được kết nối và trạng thái của chúng (ví dụ: `device`, `offline`, `unauthorized`).
    *   **Tương đương ADB:** `adb devices`
    *   **Trả về:** Chuỗi output từ lệnh `adb devices`.

*   **`devices_long() -> str`:**
    *   **Mô tả:** Liệt kê các thiết bị đang kết nối cùng với thông tin chi tiết hơn (thường bao gồm product, model, device identifiers).
    *   **Tương đương ADB:** `adb devices -l`
    *   **Trả về:** Chuỗi output từ lệnh `adb devices -l`.

*   **`root() -> str`:**
    *   **Mô tả:** Khởi động lại `adbd` (daemon ADB trên thiết bị) với quyền root. Chỉ hoạt động trên các thiết bị đã root hoặc các bản build eng/userdebug.
    *   **Tương đương ADB:** `adb root`
    *   **Trả về:** Chuỗi output từ lệnh `adb root` (thường là "restarting adbd as root" hoặc thông báo lỗi).

*   **`start_server() -> str`:**
    *   **Mô tả:** Khởi động tiến trình server ADB trên máy tính nếu nó chưa chạy.
    *   **Tương đương ADB:** `adb start-server`
    *   **Trả về:** Chuỗi output từ lệnh.

*   **`kill_server() -> str`:**
    *   **Mô tả:** Dừng tiến trình server ADB trên máy tính.
    *   **Tương đương ADB:** `adb kill-server`
    *   **Trả về:** Chuỗi output từ lệnh.

*   **`reboot() -> str`:**
    *   **Mô tả:** Khởi động lại thiết bị Android.
    *   **Tương đương ADB:** `adb reboot`
    *   **Trả về:** Chuỗi output (thường là trống nếu thành công).

*   **`shell() -> str`:**
    *   **Mô tả:** Mở một shell tương tác trên thiết bị. Hàm này trong OIADB có thể chỉ thực thi `adb shell` mà không thực sự mở shell tương tác, hoặc trả về output của một lệnh shell mặc định nào đó. Cần kiểm tra lại cách triển khai cụ thể.
    *   **Tương đương ADB:** `adb shell`
    *   **Trả về:** Output từ lệnh shell (nếu có).

*   **`help() -> str`:**
    *   **Mô tả:** Hiển thị thông tin trợ giúp chung của ADB.
    *   **Tương đương ADB:** `adb help`
    *   **Trả về:** Chuỗi chứa nội dung trợ giúp.

*   **`custom_command(device_id: str, command: str) -> str`:**
    *   **Mô tả:** Thực thi một lệnh ADB tùy chỉnh nhắm vào một thiết bị cụ thể. Hữu ích khi bạn muốn chạy lệnh không được OIADB hỗ trợ trực tiếp hoặc cần chỉ định rõ thiết bị.
    *   **Tham số:**
        *   `device_id`: ID của thiết bị mục tiêu.
        *   `command`: Chuỗi lệnh cần thực thi (phần sau `adb -s <device_id>`).
    *   **Tương đương ADB:** `adb -s <device_id> <command>`
    *   **Trả về:** Chuỗi output từ lệnh.

*   **`usb_only(command: str) -> str`:**
    *   **Mô tả:** Thực thi một lệnh ADB chỉ nhắm vào thiết bị kết nối qua USB (nếu có nhiều thiết bị, bao gồm cả emulator/Wi-Fi).
    *   **Tham số:** `command`: Chuỗi lệnh cần thực thi (phần sau `adb -d`).
    *   **Tương đương ADB:** `adb -d <command>`
    *   **Trả về:** Chuỗi output từ lệnh.

*   **`emulator_only(command: str) -> str`:**
    *   **Mô tả:** Thực thi một lệnh ADB chỉ nhắm vào trình giả lập (emulator) đang chạy (nếu có nhiều thiết bị, bao gồm cả USB/Wi-Fi).
    *   **Tham số:** `command`: Chuỗi lệnh cần thực thi (phần sau `adb -e`).
    *   **Tương đương ADB:** `adb -e <command>`
    *   **Trả về:** Chuỗi output từ lệnh.

**Ví dụ sử dụng:**

```python
from oiadb import MyADB
from oiadb.commands import basic # Có thể truy cập trực tiếp nếu muốn

try:
    adb = MyADB() # Kết nối thiết bị đầu tiên

    # Liệt kê thiết bị chi tiết
    devices_info = basic.devices_long()
    print("Thông tin thiết bị chi tiết:\n", devices_info)

    # Thử lấy quyền root (chỉ thành công trên thiết bị hỗ trợ)
    # try:
    #     root_result = basic.root()
    #     print("Kết quả adb root:", root_result)
    # except Exception as root_err:
    #     print("Không thể lấy quyền root:", root_err)

    # Chạy lệnh shell tùy chỉnh
    wifi_status = basic.custom_command(adb.device_id, "shell dumpsys wifi | grep Wi-Fi")
    print("Trạng thái Wi-Fi:", wifi_status.strip())

    # Khởi động lại thiết bị (Cẩn thận!)
    # print("Đang khởi động lại thiết bị...")
    # basic.reboot()

except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
```




### 5.4. `connect`: Quản lý Kết nối Thiết bị

Module này xử lý việc thiết lập kết nối ADB đến các thiết bị, đặc biệt là qua mạng (Wi-Fi).

**Vị trí:** `oiadb/commands/connect.py`

**Các hàm chính:**

*   **`connect_default(ip: str, port: int) -> str`:**
    *   **Mô tả:** Thực hiện kết nối ADB tiêu chuẩn đến một thiết bị qua địa chỉ IP và cổng.
    *   **Tham số:**
        *   `ip`: Địa chỉ IP của thiết bị Android.
        *   `port`: Cổng ADB đang lắng nghe trên thiết bị (thường là 5555 sau khi chạy `adb tcpip 5555`).
    *   **Tương đương ADB:** `adb connect <ip>:<port>`
    *   **Trả về:** Chuỗi output từ lệnh `adb connect` (ví dụ: `connected to 192.168.1.100:5555` hoặc `failed to connect to ...`).

*   **`connect_pair(ip: str, port: int, pairing_code: str) -> str`:**
    *   **Mô tả:** Thực hiện kết nối ADB sử dụng cơ chế ghép nối (pairing) qua Wi-Fi, thường được yêu cầu trên Android 11 trở lên khi bật "Gỡ lỗi không dây" (Wireless debugging).
    *   **Tham số:**
        *   `ip`: Địa chỉ IP của thiết bị.
        *   `port`: Cổng ghép nối hiển thị trên màn hình "Gỡ lỗi không dây" của thiết bị.
        *   `pairing_code`: Mã ghép nối gồm 6 chữ số hiển thị trên màn hình "Gỡ lỗi không dây".
    *   **Tương đương ADB:** `adb pair <ip>:<port> <pairing_code>`
    *   **Trả về:** Chuỗi output từ lệnh `adb pair` (ví dụ: `Successfully paired to ...`). Lưu ý: Lệnh này chỉ thực hiện ghép nối, bạn vẫn cần chạy `adb connect` (sử dụng cổng kết nối riêng, khác cổng pairing) sau đó để thực sự kết nối shell.

**Ví dụ sử dụng:**

```python
from oiadb import MyADB
from oiadb.commands import connect # Có thể truy cập trực tiếp nếu muốn

# --- Kết nối thông thường (sau khi đã chạy adb tcpip 5555 trên thiết bị qua USB) ---
try:
    device_ip = "192.168.1.105" # Thay bằng IP thực tế
    connect_port = 5555
    print(f"Đang kết nối đến {device_ip}:{connect_port}...")
    result = connect.connect_default(device_ip, connect_port)
    print(f"Kết quả kết nối: {result}")

    # Sau khi kết nối, có thể khởi tạo MyADB với device_id là IP:PORT
    # adb = MyADB(device_id=f"{device_ip}:{connect_port}")
    # print(f"Đã khởi tạo MyADB cho {adb.device_id}")
    # model = adb.run("shell getprop ro.product.model")
    # print(f"Model: {model.strip()}")

except Exception as e:
    print(f"Lỗi kết nối: {e}")

# --- Kết nối bằng mã ghép nối (Android 11+) ---
# try:
#     pair_ip = "192.168.1.108" # IP hiển thị trên màn hình Gỡ lỗi không dây
#     pair_port = 41234        # Cổng PAIRING hiển thị
#     pair_code = "123456"     # Mã PAIRING hiển thị
#     connect_port_after_pair = 37890 # Cổng CONNECT hiển thị (khác cổng pairing)

#     print(f"Đang ghép nối với {pair_ip}:{pair_port} bằng mã {pair_code}...")
#     pair_result = connect.connect_pair(pair_ip, pair_port, pair_code)
#     print(f"Kết quả ghép nối: {pair_result}")

#     if "Successfully paired" in pair_result:
#         print(f"Đang kết nối đến {pair_ip}:{connect_port_after_pair}...")
#         connect_result = connect.connect_default(pair_ip, connect_port_after_pair)
#         print(f"Kết quả kết nối: {connect_result}")
#         # Khởi tạo MyADB
#         # adb_paired = MyADB(device_id=f"{pair_ip}:{connect_port_after_pair}")
#         # print(f"Đã khởi tạo MyADB cho {adb_paired.device_id}")
#     else:
#         print("Ghép nối thất bại.")

# except Exception as e:
#     print(f"Lỗi ghép nối: {e}")
```

**Lưu ý quan trọng về Ghép nối (Pairing):**

*   Cơ chế ghép nối (`adb pair`) chỉ thiết lập sự tin tưởng giữa máy tính và thiết bị.
*   Sau khi ghép nối thành công, bạn **vẫn phải** sử dụng lệnh `adb connect` với địa chỉ IP và **cổng kết nối** (connection port) được hiển thị trên màn hình "Gỡ lỗi không dây" (cổng này khác với cổng ghép nối - pairing port) để thực sự thiết lập phiên ADB.
*   OIADB hiện tại dường như chỉ cung cấp hàm `connect_pair` để thực hiện bước ghép nối. Bạn cần tự gọi `connect_default` với cổng kết nối đúng sau khi ghép nối thành công.




### 5.5. `device_actions`: Hành động trên Thiết bị

Module này bao gồm các lệnh thực hiện các hành động cấp thiết bị như khởi động lại vào các chế độ khác nhau, chụp/quay màn hình, và sao lưu/phục hồi.

**Vị trí:** `oiadb/commands/device_actions.py`

**Các hàm chính:**

*   **`reboot_recovery() -> str`:**
    *   **Mô tả:** Khởi động lại thiết bị vào chế độ Recovery.
    *   **Tương đương ADB:** `adb reboot recovery`
    *   **Trả về:** Chuỗi output từ lệnh.

*   **`reboot_fastboot() -> str`:**
    *   **Mô tả:** Khởi động lại thiết bị vào chế độ Bootloader (thường được gọi là Fastboot).
    *   **Tương đương ADB:** `adb reboot bootloader` (Lưu ý: Lệnh ADB chuẩn là `bootloader`, không phải `fastboot`. Cần kiểm tra lại mã nguồn OIADB hoặc đây có thể là một alias tùy chỉnh).
    *   **Trả về:** Chuỗi output từ lệnh.

*   **`screencap(path: str) -> str`:**
    *   **Mô tả:** Chụp ảnh màn hình và lưu trực tiếp vào một đường dẫn **trên thiết bị**.
    *   **Tham số:** `path`: Đường dẫn đầy đủ trên thiết bị để lưu file ảnh PNG (ví dụ: `/sdcard/screenshot.png`).
    *   **Tương đương ADB:** `adb shell screencap -p <path>`
    *   **Trả về:** Chuỗi output từ lệnh `screencap` (thường là trống nếu thành công).
    *   **Lưu ý:** Hàm này khác với `adb.take_screenshot()` (trong lớp `MyADB`), vốn kéo ảnh về máy tính.

*   **`screenrecord(path: str) -> str`:**
    *   **Mô tả:** Bắt đầu quay video màn hình và lưu vào một đường dẫn **trên thiết bị**. Quá trình quay sẽ tiếp tục cho đến khi bị dừng (Ctrl+C trong shell) hoặc đạt giới hạn thời gian mặc định (thường là 3 phút).
    *   **Tham số:** `path`: Đường dẫn đầy đủ trên thiết bị để lưu file video MP4 (ví dụ: `/sdcard/video.mp4`).
    *   **Tương đương ADB:** `adb shell screenrecord <path>` (Có thể thêm các tùy chọn như `--time-limit`, `--size`, `--bit-rate`).
    *   **Trả về:** Chuỗi output từ lệnh. Lệnh này thường chạy nền, nên việc quản lý tiến trình quay cần được xử lý riêng (ví dụ: dùng `run_async` và `kill`).

*   **`backup_all(filename: str) -> str`:**
    *   **Mô tả:** Tạo một bản sao lưu đầy đủ của thiết bị (bao gồm ứng dụng và dữ liệu của chúng) vào một tệp trên máy tính cục bộ. Yêu cầu xác nhận trên màn hình thiết bị.
    *   **Tham số:** `filename`: Đường dẫn và tên tệp trên máy tính để lưu bản sao lưu (ví dụ: `./my_backup.ab`).
    *   **Tương đương ADB:** `adb backup -apk -all -f <filename>` (Tùy chọn `-apk` bao gồm cả tệp APK, `-all` bao gồm tất cả ứng dụng).
    *   **Trả về:** Chuỗi output từ lệnh `adb backup`.

*   **`restore_backup(filename: str) -> str`:**
    *   **Mô tả:** Phục hồi thiết bị từ một tệp sao lưu đã tạo trước đó. Yêu cầu xác nhận trên màn hình thiết bị.
    *   **Tham số:** `filename`: Đường dẫn đến tệp sao lưu (`.ab`) trên máy tính.
    *   **Tương đương ADB:** `adb restore <filename>`
    *   **Trả về:** Chuỗi output từ lệnh `adb restore`.

*   **`start_activity(intent: str) -> str`:**
    *   **Mô tả:** Khởi chạy một Activity bằng cách sử dụng Intent. Cung cấp cách linh hoạt hơn để khởi chạy các thành phần ứng dụng so với `apps.start_app`.
    *   **Tham số:** `intent`: Chuỗi mô tả Intent, bao gồm action, data, component, extras... (ví dụ: `-a android.intent.action.VIEW -d http://example.com`, `-n com.example.app/.MainActivity`).
    *   **Tương đương ADB:** `adb shell am start <intent_arguments>`
    *   **Trả về:** Chuỗi output từ lệnh `am start`.

**Ví dụ sử dụng:**

```python
from oiadb import MyADB
from oiadb.commands import device_actions
import time

try:
    adb = MyADB()

    # Chụp ảnh màn hình và lưu trên thiết bị
    device_path = "/sdcard/temp_screenshot.png"
    print(f"Đang chụp màn hình lưu vào {device_path}...")
    device_actions.screencap(device_path)
    # Kiểm tra xem file có tồn tại không (ví dụ)
    ls_output = adb.run(f"shell ls {device_path}")
    if device_path in ls_output:
        print("Chụp màn hình thành công!")
        # Kéo về máy tính nếu muốn
        # adb.pull_file(device_path, "./device_screenshot.png")
        # Xóa file trên thiết bị
        adb.run(f"shell rm {device_path}")
    else:
        print("Chụp màn hình thất bại.")

    # Khởi chạy trình duyệt với một URL
    print("Đang mở trình duyệt...")
    device_actions.start_activity("-a android.intent.action.VIEW -d https://www.google.com")

    # Sao lưu (Yêu cầu xác nhận trên thiết bị!)
    # print("Bắt đầu sao lưu, vui lòng xác nhận trên thiết bị...")
    # backup_file = "full_backup.ab"
    # backup_result = device_actions.backup_all(backup_file)
    # print(f"Kết quả sao lưu: {backup_result}")

    # Khởi động lại vào recovery (Cẩn thận!)
    # print("Đang khởi động lại vào Recovery...")
    # device_actions.reboot_recovery()

except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
```




### 5.6. `device_info`: Thu thập Thông tin Thiết bị

Module này (thường được triển khai trong lớp `DeviceCommands`) cung cấp các phương thức để lấy thông tin chi tiết về phần cứng, phần mềm và trạng thái hiện tại của thiết bị Android.

**Vị trí:** `oiadb/commands/device_info.py` (Thường được đóng gói trong lớp `DeviceCommands`)

**Các hàm/phương thức chính (trong lớp `DeviceCommands`):**

*   **`get_state() -> str`:**
    *   **Mô tả:** Lấy trạng thái kết nối hiện tại của thiết bị đối với ADB.
    *   **Tương đương ADB:** `adb get-state`
    *   **Trả về:** Chuỗi trạng thái (`"device"`, `"offline"`, `"unknown"`, `"bootloader"`, `"recovery"`).

*   **`get_serialno() -> str`:**
    *   **Mô tả:** Lấy số serial (serial number) duy nhất của thiết bị.
    *   **Tương đương ADB:** `adb get-serialno`
    *   **Trả về:** Chuỗi số serial.

*   **`get_imei() -> str`:**
    *   **Mô tả:** Cố gắng lấy số IMEI của thiết bị. Lưu ý: Lệnh `dumpsys iphonesybinfo` (được sử dụng trong mã nguồn) có thể không tồn tại trên tất cả các thiết bị hoặc phiên bản Android, hoặc có thể yêu cầu quyền đặc biệt. Việc lấy IMEI thường bị hạn chế vì lý do bảo mật.
    *   **Tương đương ADB:** `adb shell dumpsys iphonesybinfo` (Không phải lệnh chuẩn, độ tin cậy thấp).
    *   **Trả về:** Chuỗi IMEI nếu thành công, hoặc output lỗi.

*   **`battery() -> Dict[str, Any]`:**
    *   **Mô tả:** Lấy thông tin chi tiết về pin bằng cách phân tích output của `dumpsys battery`.
    *   **Tương đương ADB:** `adb shell dumpsys battery`
    *   **Trả về:** Dictionary chứa các thông tin như `level` (mức pin), `status` (trạng thái sạc), `health` (sức khỏe pin), `temperature`, `voltage`, `technology`...

*   **`current_dir() -> str`:**
    *   **Mô tả:** Lấy đường dẫn thư mục làm việc hiện tại trong shell ADB.
    *   **Tương đương ADB:** `adb shell pwd`
    *   **Trả về:** Chuỗi đường dẫn thư mục hiện tại.

*   **`list_features() -> List[str]`:**
    *   **Mô tả:** Liệt kê các tính năng phần cứng và phần mềm mà thiết bị hỗ trợ (ví dụ: `android.hardware.camera`, `android.software.live_wallpaper`).
    *   **Tương đương ADB:** `adb shell pm list features`
    *   **Trả về:** Danh sách (List) các chuỗi tên tính năng (đã loại bỏ tiền tố `feature:`).

*   **`service_list() -> List[str]`:**
    *   **Mô tả:** Liệt kê các dịch vụ hệ thống đang chạy và được đăng ký với `servicemanager`.
    *   **Tương đương ADB:** `adb shell service list`
    *   **Trả về:** Danh sách (List) các chuỗi tên dịch vụ.

*   **`screen_size() -> Tuple[int, int]`:**
    *   **Mô tả:** Lấy kích thước vật lý của màn hình (chiều rộng và chiều cao) tính bằng pixel.
    *   **Tương đương ADB:** `adb shell wm size`
    *   **Trả về:** Tuple `(width, height)`.

*   **`screen_density() -> int`:**
    *   **Mô tả:** Lấy mật độ điểm ảnh vật lý của màn hình (dots per inch - DPI).
    *   **Tương đương ADB:** `adb shell wm density`
    *   **Trả về:** Số nguyên là giá trị DPI.

*   **`get_android_version() -> str`:**
    *   **Mô tả:** Lấy phiên bản hệ điều hành Android (ví dụ: "11", "12").
    *   **Tương đương ADB:** `adb shell getprop ro.build.version.release`
    *   **Trả về:** Chuỗi phiên bản Android.

*   **`get_sdk_version() -> int`:**
    *   **Mô tả:** Lấy cấp độ API (SDK version) của hệ điều hành Android (ví dụ: 30 cho Android 11, 31 cho Android 12).
    *   **Tương đương ADB:** `adb shell getprop ro.build.version.sdk`
    *   **Trả về:** Số nguyên là cấp độ API.

*   **`get_device_model() -> str`:**
    *   **Mô tả:** Lấy tên model của thiết bị.
    *   **Tương đương ADB:** `adb shell getprop ro.product.model`
    *   **Trả về:** Chuỗi tên model.

*   **`get_device_manufacturer() -> str`:**
    *   **Mô tả:** Lấy tên nhà sản xuất thiết bị.
    *   **Tương đương ADB:** `adb shell getprop ro.product.manufacturer`
    *   **Trả về:** Chuỗi tên nhà sản xuất.

*   **`get_device_info() -> Dict[str, Any]`:**
    *   **Mô tả:** Tổng hợp thông tin chi tiết về thiết bị bằng cách gọi nhiều hàm lấy thông tin khác (`get_android_version`, `get_sdk_version`, `get_device_model`, `battery`, `screen_size`...) và bổ sung thêm các thuộc tính hệ thống (`getprop`).
    *   **Trả về:** Dictionary chứa nhiều thông tin tổng hợp về thiết bị.

*   **`reboot(mode: Optional[str] = None) -> str`:**
    *   **Mô tả:** Khởi động lại thiết bị. Có thể chỉ định chế độ khởi động lại.
    *   **Tham số:** `mode`: `None` (khởi động lại bình thường), `"recovery"`, `"bootloader"`, `"fastboot"`.
    *   **Tương đương ADB:** `adb reboot [mode]`
    *   **Trả về:** Chuỗi output từ lệnh.

*   **(Các hàm reboot khác như `reboot_recovery`, `reboot_bootloader`, `reboot_fastboot` là các alias tiện lợi cho `reboot(mode=...)`)**

*   **(Các hàm `screencap`, `take_screenshot`, `screenrecord`, `record_screen`, `backup`, `restore`, `start_activity`, `start_service`, `broadcast`, `set_prop`, `get_prop` cũng được liệt kê trong mã nguồn `device_info.py`, nhưng chúng có vẻ thuộc về các module khác như `device_actions` hoặc `basic`. Có thể có sự trùng lặp hoặc cấu trúc lại trong mã nguồn. Tài liệu này sẽ mô tả chúng dựa trên chức năng logic thay vì vị trí file tuyệt đối.)**

**Ví dụ sử dụng:**

```python
from oiadb import MyADB
from oiadb.commands import device_info # Hoặc truy cập qua adb instance
import json

try:
    adb = MyADB()

    # Lấy trạng thái
    state = adb.run("get-state") # Hoặc device_info.get_state()
    print(f"Trạng thái thiết bị: {state.strip()}")

    # Lấy thông tin cơ bản
    android_version = device_info.get_android_version()
    sdk_version = device_info.get_sdk_version()
    model = device_info.get_device_model()
    manufacturer = device_info.get_device_manufacturer()
    print(f"Thiết bị: {manufacturer} {model}")
    print(f"Android: {android_version} (SDK {sdk_version})")

    # Lấy thông tin màn hình
    width, height = device_info.screen_size()
    density = device_info.screen_density()
    print(f"Màn hình: {width}x{height} @ {density}dpi")

    # Lấy thông tin pin
    battery_stats = device_info.battery()
    print("Thông tin pin:")
    print(json.dumps(battery_stats, indent=2))

    # Lấy thông tin tổng hợp
    # all_info = device_info.get_device_info()
    # print("\nThông tin tổng hợp:")
    # print(json.dumps(all_info, indent=2))

except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
```




### 5.7. `file_ops`: Thao tác với Hệ thống Tệp

Module này (thường được triển khai trong lớp `FileOperationsCommands`) cung cấp các phương thức để tương tác với hệ thống tệp trên thiết bị Android, bao gồm sao chép, di chuyển, xóa, liệt kê, đọc, ghi file và thư mục.

**Vị trí:** `oiadb/commands/file_ops.py` (Thường được đóng gói trong lớp `FileOperationsCommands`)

**Các hàm/phương thức chính (trong lớp `FileOperationsCommands`):**

*   **`push(local_path: str, remote_path: str) -> str`:**
    *   **Mô tả:** Đẩy (sao chép) một file hoặc thư mục từ máy tính cục bộ lên thiết bị Android.
    *   **Tham số:**
        *   `local_path`: Đường dẫn đến file/thư mục trên máy tính.
        *   `remote_path`: Đường dẫn đích trên thiết bị Android.
    *   **Tương đương ADB:** `adb push <local_path> <remote_path>`
    *   **Trả về:** Chuỗi output từ lệnh `adb push`.
    *   **Ngoại lệ:** `FileOperationError` nếu file nguồn không tồn tại hoặc có lỗi trong quá trình đẩy.

*   **`pull(remote_path: str, local_path: str) -> str`:**
    *   **Mô tả:** Kéo (sao chép) một file hoặc thư mục từ thiết bị Android về máy tính cục bộ.
    *   **Tham số:**
        *   `remote_path`: Đường dẫn đến file/thư mục trên thiết bị Android.
        *   `local_path`: Đường dẫn đích trên máy tính (thư mục cha sẽ được tạo nếu chưa tồn tại).
    *   **Tương đương ADB:** `adb pull <remote_path> <local_path>`
    *   **Trả về:** Chuỗi output từ lệnh `adb pull`.
    *   **Ngoại lệ:** `FileOperationError` nếu có lỗi trong quá trình kéo.

*   **`list_files(remote_path: str) -> List[str]`:**
    *   **Mô tả:** Liệt kê nội dung của một thư mục trên thiết bị (bao gồm cả file và thư mục con). Sử dụng `ls -la` để lấy thông tin chi tiết, nhưng chỉ trả về tên.
    *   **Tham số:** `remote_path`: Đường dẫn đến thư mục trên thiết bị.
    *   **Tương đương ADB:** `adb shell ls -la <remote_path>`
    *   **Trả về:** Danh sách (List) các chuỗi tên file/thư mục trong thư mục đó.
    *   **Ngoại lệ:** `FileOperationError` nếu đường dẫn không hợp lệ hoặc có lỗi.

*   **`exists(remote_path: str) -> bool`:**
    *   **Mô tả:** Kiểm tra sự tồn tại của một file hoặc thư mục tại đường dẫn chỉ định trên thiết bị.
    *   **Tham số:** `remote_path`: Đường dẫn cần kiểm tra.
    *   **Tương đương ADB:** `adb shell [ -e <remote_path> ] && echo "exists" || echo "not exists"`
    *   **Trả về:** `True` nếu tồn tại, `False` nếu không.

*   **`is_file(remote_path: str) -> bool`:**
    *   **Mô tả:** Kiểm tra xem đường dẫn chỉ định trên thiết bị có phải là một file thông thường hay không.
    *   **Tham số:** `remote_path`: Đường dẫn cần kiểm tra.
    *   **Tương đương ADB:** `adb shell [ -f <remote_path> ] && echo "is file" || echo "not file"`
    *   **Trả về:** `True` nếu là file, `False` nếu không (có thể là thư mục hoặc không tồn tại).

*   **`is_dir(remote_path: str) -> bool`:**
    *   **Mô tả:** Kiểm tra xem đường dẫn chỉ định trên thiết bị có phải là một thư mục hay không.
    *   **Tham số:** `remote_path`: Đường dẫn cần kiểm tra.
    *   **Tương đương ADB:** `adb shell [ -d <remote_path> ] && echo "is dir" || echo "not dir"`
    *   **Trả về:** `True` nếu là thư mục, `False` nếu không.

*   **`mkdir(remote_path: str, parents: bool = False) -> str`:**
    *   **Mô tả:** Tạo một thư mục mới trên thiết bị.
    *   **Tham số:**
        *   `remote_path`: Đường dẫn thư mục cần tạo.
        *   `parents` (bool): Nếu `True`, tạo cả các thư mục cha nếu chúng chưa tồn tại (tương đương `mkdir -p`).
    *   **Tương đương ADB:** `adb shell mkdir [-p] <remote_path>`
    *   **Trả về:** Chuỗi output từ lệnh `mkdir`.
    *   **Ngoại lệ:** `FileOperationError` nếu tạo thư mục thất bại.

*   **`remove(remote_path: str, recursive: bool = False, force: bool = False) -> str`:**
    *   **Mô tả:** Xóa một file hoặc thư mục trên thiết bị.
    *   **Tham số:**
        *   `remote_path`: Đường dẫn đến file/thư mục cần xóa.
        *   `recursive` (bool): Nếu `True`, xóa thư mục và toàn bộ nội dung bên trong nó (`-r`).
        *   `force` (bool): Nếu `True`, bỏ qua các lỗi file không tồn tại và không bao giờ hỏi xác nhận (`-f`).
    *   **Tương đương ADB:** `adb shell rm [-r] [-f] <remote_path>`
    *   **Trả về:** Chuỗi output từ lệnh `rm`.
    *   **Ngoại lệ:** `FileOperationError` nếu xóa thất bại.

*   **`copy(source_path: str, dest_path: str) -> str`:**
    *   **Mô tả:** Sao chép file hoặc thư mục từ vị trí này sang vị trí khác **trên cùng thiết bị**.
    *   **Tham số:**
        *   `source_path`: Đường dẫn nguồn trên thiết bị.
        *   `dest_path`: Đường dẫn đích trên thiết bị.
    *   **Tương đương ADB:** `adb shell cp -r <source_path> <dest_path>` (Luôn sử dụng `-r` để hỗ trợ cả thư mục).
    *   **Trả về:** Chuỗi output từ lệnh `cp`.
    *   **Ngoại lệ:** `FileOperationError` nếu sao chép thất bại.

*   **`move(source_path: str, dest_path: str) -> str`:**
    *   **Mô tả:** Di chuyển (hoặc đổi tên) file hoặc thư mục từ vị trí này sang vị trí khác **trên cùng thiết bị**.
    *   **Tham số:**
        *   `source_path`: Đường dẫn nguồn trên thiết bị.
        *   `dest_path`: Đường dẫn đích trên thiết bị.
    *   **Tương đương ADB:** `adb shell mv <source_path> <dest_path>`
    *   **Trả về:** Chuỗi output từ lệnh `mv`.
    *   **Ngoại lệ:** `FileOperationError` nếu di chuyển thất bại.

*   **`cat(remote_path: str) -> str`:**
    *   **Mô tả:** Đọc và trả về toàn bộ nội dung của một file text trên thiết bị.
    *   **Tham số:** `remote_path`: Đường dẫn đến file trên thiết bị.
    *   **Tương đương ADB:** `adb shell cat <remote_path>`
    *   **Trả về:** Chuỗi chứa nội dung của file.
    *   **Ngoại lệ:** `FileOperationError` nếu đọc file thất bại.

*   **`write(remote_path: str, content: str) -> str`:**
    *   **Mô tả:** Ghi đè nội dung vào một file trên thiết bị. Phương thức này hoạt động bằng cách tạo một file tạm trên máy tính, đẩy lên thiết bị, sau đó dùng `cat` và chuyển hướng (`>`) để ghi nội dung vào file đích.
    *   **Tham số:**
        *   `remote_path`: Đường dẫn đến file đích trên thiết bị.
        *   `content`: Chuỗi nội dung cần ghi.
    *   **Trả về:** Chuỗi output từ lệnh `cat ... > ...`.
    *   **Ngoại lệ:** `FileOperationError` nếu ghi file thất bại.

*   **`append(remote_path: str, content: str) -> str`:**
    *   **Mô tả:** Nối thêm nội dung vào cuối một file trên thiết bị. Hoạt động tương tự `write` nhưng sử dụng chuyển hướng nối thêm (`>>`).
    *   **Tham số:**
        *   `remote_path`: Đường dẫn đến file đích trên thiết bị.
        *   `content`: Chuỗi nội dung cần nối thêm.
    *   **Trả về:** Chuỗi output từ lệnh `cat ... >> ...`.
    *   **Ngoại lệ:** `FileOperationError` nếu nối file thất bại.

*   **`chmod(remote_path: str, mode: str) -> str`:**
    *   **Mô tả:** Thay đổi quyền truy cập (permissions) của file hoặc thư mục trên thiết bị.
    *   **Tham số:**
        *   `remote_path`: Đường dẫn đến file/thư mục.
        *   `mode`: Chuỗi biểu diễn quyền truy cập dạng số (ví dụ: `"755"`, `"644"`) hoặc dạng ký hiệu (ví dụ: `"u+x"`).
    *   **Tương đương ADB:** `adb shell chmod <mode> <remote_path>`
    *   **Trả về:** Chuỗi output từ lệnh `chmod`.
    *   **Ngoại lệ:** `FileOperationError` nếu thay đổi quyền thất bại.

*   **`get_size(remote_path: str) -> int`:**
    *   **Mô tả:** Lấy kích thước của một file trên thiết bị tính bằng byte.
    *   **Tham số:** `remote_path`: Đường dẫn đến file.
    *   **Tương đương ADB:** `adb shell stat -c %s <remote_path>`
    *   **Trả về:** Số nguyên là kích thước file (bytes).
    *   **Ngoại lệ:** `FileOperationError` nếu không lấy được kích thước (ví dụ: file không tồn tại, không phải file).

*   **`get_free_space(mount_point: str = "/data") -> int`:**
    *   **Mô tả:** Lấy dung lượng trống trên một phân vùng (mount point) cụ thể của thiết bị.
    *   **Tham số:** `mount_point`: Đường dẫn đến điểm gắn kết (mặc định là `/data`). Các điểm phổ biến khác: `/sdcard`, `/system`.
    *   **Tương đương ADB:** `adb shell df <mount_point>`
    *   **Trả về:** Số nguyên là dung lượng trống tính bằng byte.
    *   **Ngoại lệ:** `FileOperationError` nếu không lấy được thông tin dung lượng.

**Ví dụ sử dụng:**

```python
from oiadb import MyADB
from oiadb.commands import file_ops
from oiadb.exceptions import FileOperationError

try:
    adb = MyADB()
    remote_dir = "/sdcard/oiadb_test_dir"
    remote_file = f"{remote_dir}/test_file.txt"
    local_file = "./local_copy.txt"

    # Tạo thư mục
    print(f"Đang tạo thư mục {remote_dir}...")
    file_ops.mkdir(remote_dir, parents=True)

    # Kiểm tra sự tồn tại
    if file_ops.exists(remote_dir) and file_ops.is_dir(remote_dir):
        print("Tạo thư mục thành công.")
    else:
        print("Tạo thư mục thất bại.")
        exit()

    # Ghi file
    content_to_write = "Dòng đầu tiên.\n"
    print(f"Đang ghi vào {remote_file}...")
    file_ops.write(remote_file, content_to_write)

    # Nối thêm vào file
    content_to_append = "Dòng thứ hai.\n"
    print(f"Đang nối thêm vào {remote_file}...")
    file_ops.append(remote_file, content_to_append)

    # Đọc nội dung file
    print(f"Đang đọc nội dung {remote_file}...")
    read_content = file_ops.cat(remote_file)
    print(f"Nội dung:\n{read_content}")

    # Lấy kích thước file
    size = file_ops.get_size(remote_file)
    print(f"Kích thước file: {size} bytes")

    # Kéo file về máy tính
    print(f"Đang kéo {remote_file} về {local_file}...")
    file_ops.pull(remote_file, local_file)
    if os.path.exists(local_file):
        print("Kéo file thành công.")
        with open(local_file, "r") as f:
            print(f"Nội dung file cục bộ:\n{f.read()}")
        os.remove(local_file) # Xóa file cục bộ sau khi kiểm tra
    else:
        print("Kéo file thất bại.")

    # Liệt kê thư mục
    print(f"Nội dung thư mục {remote_dir}:")
    files_list = file_ops.list_files(remote_dir)
    for item in files_list:
        print(f"- {item}")

    # Xóa file và thư mục
    print(f"Đang xóa {remote_file}...")
    file_ops.remove(remote_file)
    print(f"Đang xóa {remote_dir}...")
    file_ops.remove(remote_dir, recursive=True)

    # Kiểm tra lại sự tồn tại
    if not file_ops.exists(remote_dir):
        print("Xóa thành công.")
    else:
        print("Xóa thất bại.")

except FileOperationError as e:
    print(f"Lỗi thao tác file: {e}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
```




### 5.8. `interaction`: Mô phỏng Tương tác Người dùng

Module này (thường được triển khai trong lớp `InteractionCommands`) tập trung vào việc mô phỏng các hành động tương tác của người dùng trên màn hình thiết bị, như chạm, vuốt, nhập liệu và nhấn phím.

**Vị trí:** `oiadb/commands/interaction.py` (Thường được đóng gói trong lớp `InteractionCommands`)

**Các hàm/phương thức chính (trong lớp `InteractionCommands`):**

*   **`tap(x: int, y: int) -> str`:**
    *   **Mô tả:** Mô phỏng một cú chạm (tap) tại tọa độ (x, y) trên màn hình.
    *   **Tham số:**
        *   `x`: Tọa độ X.
        *   `y`: Tọa độ Y.
    *   **Tương đương ADB:** `adb shell input tap <x> <y>`
    *   **Trả về:** Chuỗi output từ lệnh.

*   **`swipe(x1: int, y1: int, x2: int, y2: int, duration: int = 300) -> str`:**
    *   **Mô tả:** Mô phỏng thao tác vuốt (swipe) từ điểm (x1, y1) đến điểm (x2, y2) trong một khoảng thời gian nhất định.
    *   **Tham số:**
        *   `x1`, `y1`: Tọa độ điểm bắt đầu.
        *   `x2`, `y2`: Tọa độ điểm kết thúc.
        *   `duration`: Thời gian thực hiện thao tác vuốt (tính bằng mili giây, mặc định 300ms).
    *   **Tương đương ADB:** `adb shell input swipe <x1> <y1> <x2> <y2> [duration]`
    *   **Trả về:** Chuỗi output từ lệnh.

*   **`text_input(text: str) -> str`:**
    *   **Mô tả:** Nhập một chuỗi văn bản vào trường nhập liệu đang có focus trên thiết bị. Lưu ý: Lệnh này có thể không hoạt động với mọi loại bàn phím hoặc trường nhập liệu, và các ký tự đặc biệt (như khoảng trắng, dấu nháy) cần được escape đúng cách (mã nguồn OIADB đã xử lý việc này).
    *   **Tham số:** `text`: Chuỗi văn bản cần nhập.
    *   **Tương đương ADB:** `adb shell input text '<escaped_text>'`
    *   **Trả về:** Chuỗi output từ lệnh.

*   **`key_event(key_code: int) -> str`:**
    *   **Mô tả:** Gửi một sự kiện nhấn phím (key event) đến thiết bị bằng mã phím (keycode). Danh sách các keycode có thể tìm thấy trong tài liệu Android (KeyEvent).
    *   **Tham số:** `key_code`: Mã số nguyên của phím (ví dụ: 4 cho BACK, 3 cho HOME, 66 cho ENTER).
    *   **Tương đương ADB:** `adb shell input keyevent <key_code>`
    *   **Trả về:** Chuỗi output từ lệnh.

*   **Các hàm tiện ích cho `key_event`:**
    *   `back() -> str`: Gửi keycode 4 (Nút Back).
    *   `home() -> str`: Gửi keycode 3 (Nút Home).
    *   `menu() -> str`: Gửi keycode 82 (Nút Menu - có thể không hoạt động trên các thiết bị mới).
    *   `power() -> str`: Gửi keycode 26 (Nút Nguồn).
    *   `volume_up() -> str`: Gửi keycode 24 (Tăng âm lượng).
    *   `volume_down() -> str`: Gửi keycode 25 (Giảm âm lượng).
    *   `enter() -> str`: Gửi keycode 66 (Phím Enter).
    *   `tab() -> str`: Gửi keycode 61 (Phím Tab).
    *   `delete() -> str`: Gửi keycode 67 (Phím Delete/Backspace).
    *   `recent_apps() -> str`: Gửi keycode 187 (Hiển thị ứng dụng gần đây).

*   **`long_press(x: int, y: int, duration: int = 1000) -> str`:**
    *   **Mô tả:** Mô phỏng thao tác nhấn giữ (long press) tại tọa độ (x, y) trong một khoảng thời gian. Được thực hiện bằng cách gọi `swipe` với điểm bắt đầu và kết thúc trùng nhau.
    *   **Tham số:**
        *   `x`, `y`: Tọa độ nhấn giữ.
        *   `duration`: Thời gian nhấn giữ (mili giây, mặc định 1000ms).
    *   **Trả về:** Chuỗi output từ lệnh swipe tương ứng.

*   **`pinch(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, x4: int, y4: int, duration: int = 500) -> Tuple[str, str]`:**
    *   **Mô tả:** Mô phỏng thao tác chụm/mở hai ngón tay (pinch gesture). Yêu cầu tọa độ bắt đầu và kết thúc cho cả hai "ngón tay". Được thực hiện bằng cách chạy hai lệnh `swipe` song song (hoặc gần như song song).
    *   **Tham số:**
        *   `(x1, y1)`: Điểm bắt đầu ngón 1.
        *   `(x2, y2)`: Điểm kết thúc ngón 1.
        *   `(x3, y3)`: Điểm bắt đầu ngón 2.
        *   `(x4, y4)`: Điểm kết thúc ngón 2.
        *   `duration`: Thời gian thực hiện (mili giây).
    *   **Trả về:** Tuple chứa kết quả output của hai lệnh swipe.

*   **`zoom_in(center_x: int, center_y: int, distance: int = 200, duration: int = 500) -> Tuple[str, str]`:**
    *   **Mô tả:** Hàm tiện ích để mô phỏng thao tác phóng to (zoom in) quanh một điểm trung tâm. Thực hiện bằng cách gọi `pinch` với các tọa độ được tính toán để hai ngón tay di chuyển ra xa nhau từ gần tâm.
    *   **Tham số:**
        *   `center_x`, `center_y`: Tọa độ tâm phóng to.
        *   `distance`: Khoảng cách mỗi ngón tay di chuyển (tổng khoảng cách tăng gấp đôi).
        *   `duration`: Thời gian thực hiện.
    *   **Trả về:** Tuple chứa kết quả output của hai lệnh swipe.

*   **`zoom_out(center_x: int, center_y: int, distance: int = 200, duration: int = 500) -> Tuple[str, str]`:**
    *   **Mô tả:** Hàm tiện ích để mô phỏng thao tác thu nhỏ (zoom out) quanh một điểm trung tâm. Thực hiện bằng cách gọi `pinch` với các tọa độ được tính toán để hai ngón tay di chuyển lại gần nhau về phía tâm.
    *   **Tham số:** Tương tự `zoom_in`.
    *   **Trả về:** Tuple chứa kết quả output của hai lệnh swipe.

*   **`drag(x1: int, y1: int, x2: int, y2: int, duration: int = 1000) -> str`:**
    *   **Mô tả:** Mô phỏng thao tác kéo (drag) một đối tượng từ điểm (x1, y1) đến (x2, y2). Về cơ bản giống `swipe` nhưng thường với `duration` dài hơn.
    *   **Tham số:** Tương tự `swipe`, mặc định `duration` là 1000ms.
    *   **Trả về:** Chuỗi output từ lệnh swipe tương ứng.

*   **Các hàm tiện ích cho `swipe` (cuộn):**
    *   `scroll_up(distance: int = 500, duration: int = 500) -> str`: Cuộn lên trên một khoảng `distance` pixel.
    *   `scroll_down(distance: int = 500, duration: int = 500) -> str`: Cuộn xuống dưới một khoảng `distance` pixel.
    *   `scroll_left(distance: int = 500, duration: int = 500) -> str`: Cuộn sang trái một khoảng `distance` pixel.
    *   `scroll_right(distance: int = 500, duration: int = 500) -> str`: Cuộn sang phải một khoảng `distance` pixel.
    *   **Lưu ý:** Các hàm cuộn này cố gắng lấy kích thước màn hình để tính toán tọa độ vuốt ở giữa màn hình. Nếu không lấy được kích thước, chúng sử dụng giá trị mặc định.

*   **`type_keycode_sequence(keycodes: List[int]) -> List[str]`:**
    *   **Mô tả:** Gửi một chuỗi các sự kiện nhấn phím theo thứ tự.
    *   **Tham số:** `keycodes`: Danh sách các mã phím cần gửi.
    *   **Trả về:** Danh sách các chuỗi output từ mỗi lệnh `key_event`.

*   **`wake_up() -> str`:**
    *   **Mô tả:** Đánh thức thiết bị nếu đang ở chế độ ngủ.
    *   **Tương đương ADB:** `adb shell input keyevent KEYCODE_WAKEUP` (hoặc 224).
    *   **Trả về:** Chuỗi output từ lệnh.

*   **`sleep() -> str`:**
    *   **Mô tả:** Đưa thiết bị vào chế độ ngủ (tắt màn hình).
    *   **Tương đương ADB:** `adb shell input keyevent KEYCODE_SLEEP` (hoặc 223).
    *   **Trả về:** Chuỗi output từ lệnh.

*   **`unlock(pattern: Optional[List[int]] = None, pin: Optional[str] = None) -> str`:**
    *   **Mô tả:** Cố gắng mở khóa màn hình thiết bị. Đầu tiên, nó sẽ đánh thức thiết bị và vuốt lên để bỏ qua màn hình khóa cơ bản. Sau đó, nếu cung cấp `pattern` (mẫu hình) hoặc `pin` (mã PIN), nó sẽ cố gắng nhập chúng.
    *   **Tham số:**
        *   `pattern`: Danh sách các số nguyên từ 1-9 đại diện cho các điểm trong mẫu hình vẽ.
        *   `pin`: Chuỗi mã PIN.
    *   **Trả về:** Kết quả của lệnh nhập PIN hoặc lệnh vuốt mẫu hình cuối cùng.
    *   **Lưu ý:** Việc tính toán tọa độ cho mẫu hình dựa trên kích thước màn hình và có thể không chính xác tuyệt đối trên mọi thiết bị. Mở khóa bằng PIN/mật khẩu phức tạp hơn có thể cần các lệnh `text_input` và `enter`.

**Ví dụ sử dụng:**

```python
from oiadb import MyADB
from oiadb.commands import interaction
import time

try:
    adb = MyADB()

    # Đánh thức và mở khóa (giả sử không có khóa phức tạp)
    print("Đang đánh thức và mở khóa cơ bản...")
    interaction.unlock()
    time.sleep(1)

    # Mở ứng dụng Cài đặt (ví dụ)
    print("Mở ứng dụng Cài đặt...")
    adb.run("shell am start -n com.android.settings/.Settings")
    time.sleep(2)

    # Lấy kích thước màn hình để tính tọa độ
    size = adb.get_screen_size()
    width, height = size.get("width", 1080), size.get("height", 1920)

    # Cuộn xuống
    print("Cuộn xuống...")
    interaction.scroll_down(distance=height // 2, duration=500)
    time.sleep(1)

    # Chạm vào một vị trí gần giữa màn hình (ví dụ)
    tap_x, tap_y = width // 2, height // 2
    print(f"Chạm vào ({tap_x}, {tap_y})...")
    interaction.tap(tap_x, tap_y)
    time.sleep(1)

    # Nhập văn bản (ví dụ: vào ô tìm kiếm nếu có)
    # print("Nhập 'Wi-Fi'...")
    # interaction.text_input("Wi-Fi")
    # time.sleep(0.5)
    # interaction.enter()
    # time.sleep(2)

    # Nhấn nút Back
    print("Nhấn Back...")
    interaction.back()
    time.sleep(1)

    # Nhấn nút Home
    print("Nhấn Home...")
    interaction.home()

except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
```




### 5.9. `image_interaction`: Tương tác Dựa trên Nhận diện Hình ảnh

Module này (thường được triển khai trong lớp `ImageInteractionCommands`) mở rộng khả năng tương tác bằng cách cho phép tìm kiếm và thao tác với các yếu tố trên màn hình dựa vào hình ảnh mẫu, thay vì tọa độ cố định. Điều này rất hữu ích cho việc tự động hóa các giao diện người dùng (GUI) phức tạp hoặc thay đổi.

**Vị trí:** `oiadb/commands/image_interaction.py` (Thường được đóng gói trong lớp `ImageInteractionCommands`, sử dụng `oiadb.utils.image_recognition.ImageRecognition`)

**Các hàm/phương thức chính (trong lớp `ImageInteractionCommands`):**

*   **`find_image(template_path: str, threshold: float = 0.8, region: Optional[Tuple[int, int, int, int]] = None, scale_range: Tuple[float, float] = (0.8, 1.2), scale_steps: int = 5, rotation_range: Tuple[float, float] = (0, 0), rotation_steps: int = 1, use_gray: bool = True, use_canny: bool = False) -> Optional[Tuple[int, int, float]]`:**
    *   **Mô tả:** Tìm kiếm sự xuất hiện **đầu tiên** (với độ tin cậy cao nhất) của một hình ảnh mẫu (`template_path`) trên màn hình hiện tại của thiết bị.
    *   **Tham số:**
        *   `template_path`: Đường dẫn đến file ảnh mẫu trên máy tính.
        *   `threshold`: Ngưỡng độ tương đồng (0.0 đến 1.0). Giá trị càng cao, yêu cầu hình ảnh trên màn hình phải càng giống hệt mẫu. Mặc định là 0.8.
        *   `region`: Tuple `(x, y, width, height)` xác định vùng màn hình cần tìm kiếm. Nếu `None`, tìm kiếm trên toàn màn hình.
        *   `scale_range`: Tuple `(min_scale, max_scale)` xác định phạm vi tỷ lệ của ảnh mẫu sẽ được thử nghiệm khi tìm kiếm (ví dụ: `(0.8, 1.2)` sẽ tìm cả ảnh nhỏ hơn 20% và lớn hơn 20% so với mẫu). Mặc định `(0.8, 1.2)`.
        *   `scale_steps`: Số lượng bước tỷ lệ khác nhau sẽ được thử trong `scale_range`. Mặc định 5.
        *   `rotation_range`: Tuple `(min_angle, max_angle)` xác định phạm vi góc xoay (độ) của ảnh mẫu sẽ được thử nghiệm. Mặc định `(0, 0)` (không xoay).
        *   `rotation_steps`: Số lượng bước góc xoay khác nhau sẽ được thử trong `rotation_range`. Mặc định 1.
        *   `use_gray`: Nếu `True` (mặc định), chuyển cả ảnh màn hình và ảnh mẫu sang thang độ xám trước khi so sánh để tăng tốc độ và giảm ảnh hưởng của màu sắc.
        *   `use_canny`: Nếu `True`, áp dụng thuật toán phát hiện cạnh Canny trước khi so sánh. Hữu ích khi tìm các đối tượng có đường viền rõ ràng hoặc khi hình ảnh bị mờ/nhiễu. Mặc định `False`.
    *   **Trả về:** Tuple `(x, y, confidence)` nếu tìm thấy, trong đó `(x, y)` là tọa độ tâm của hình ảnh tìm được và `confidence` là độ tương đồng (từ `threshold` đến 1.0). Trả về `None` nếu không tìm thấy.

*   **`find_all_images(template_path: str, threshold: float = 0.8, region: Optional[Tuple[int, int, int, int]] = None, scale_range: Tuple[float, float] = (0.8, 1.2), scale_steps: int = 5, use_gray: bool = True, use_canny: bool = False) -> List[Tuple[int, int, float]]`:**
    *   **Mô tả:** Tìm kiếm **tất cả** các vị trí xuất hiện của hình ảnh mẫu trên màn hình thiết bị (đáp ứng ngưỡng `threshold`).
    *   **Tham số:** Tương tự `find_image`, nhưng không có `rotation_range` và `rotation_steps` (có thể là giới hạn của phiên bản hiện tại).
    *   **Trả về:** Danh sách (List) các tuple `(x, y, confidence)`. Trả về danh sách rỗng nếu không tìm thấy.

*   **`tap_image(template_path: str, threshold: float = 0.8, region: Optional[Tuple[int, int, int, int]] = None, scale_range: Tuple[float, float] = (0.8, 1.2), scale_steps: int = 5, use_gray: bool = True, use_canny: bool = False, tap_offset: Tuple[int, int] = (0, 0)) -> bool`:**
    *   **Mô tả:** Tìm kiếm hình ảnh mẫu đầu tiên và nếu tìm thấy, thực hiện thao tác chạm (`tap`) vào tâm của nó (có thể điều chỉnh bằng `tap_offset`).
    *   **Tham số:**
        *   Các tham số tìm kiếm tương tự `find_image`.
        *   `tap_offset`: Tuple `(dx, dy)` là độ lệch so với tâm hình ảnh khi thực hiện chạm. Mặc định `(0, 0)` (chạm đúng tâm).
    *   **Trả về:** `True` nếu tìm thấy và chạm thành công, `False` nếu không tìm thấy.

*   **`wait_and_tap_image(template_path: str, timeout: int = 10, interval: float = 0.5, threshold: float = 0.8, region: Optional[Tuple[int, int, int, int]] = None, scale_range: Tuple[float, float] = (0.8, 1.2), scale_steps: int = 5, use_gray: bool = True, use_canny: bool = False, tap_offset: Tuple[int, int] = (0, 0)) -> bool`:**
    *   **Mô tả:** Liên tục tìm kiếm hình ảnh mẫu trên màn hình trong một khoảng thời gian (`timeout`). Nếu tìm thấy, thực hiện chạm và trả về `True`. Nếu hết `timeout` mà không tìm thấy, trả về `False`.
    *   **Tham số:**
        *   Các tham số tìm kiếm và chạm tương tự `tap_image`.
        *   `timeout`: Thời gian tối đa chờ đợi (tính bằng giây). Mặc định 10 giây.
        *   `interval`: Khoảng thời gian nghỉ giữa mỗi lần chụp màn hình và tìm kiếm (tính bằng giây). Mặc định 0.5 giây.
    *   **Trả về:** `True` nếu tìm thấy và chạm thành công trong thời gian chờ, `False` nếu hết thời gian.

*   **`save_screenshot(output_path: str) -> str`:**
    *   **Mô tả:** Chụp ảnh màn hình hiện tại của thiết bị và lưu vào một file trên máy tính cục bộ.
    *   **Tham số:** `output_path`: Đường dẫn đầy đủ (bao gồm tên file và phần mở rộng, ví dụ: `./screenshots/screen1.png`) để lưu ảnh.
    *   **Trả về:** Đường dẫn đến file ảnh đã lưu.
    *   **Ngoại lệ:** `ADBCommandError` nếu chụp hoặc lưu ảnh thất bại.

*   **`get_screenshot_as_bytes() -> bytes`:**
    *   **Mô tả:** Chụp ảnh màn hình hiện tại và trả về dữ liệu ảnh dưới dạng đối tượng `bytes` (thường là định dạng PNG).
    *   **Trả về:** Đối tượng `bytes` chứa dữ liệu ảnh.
    *   **Ngoại lệ:** `ADBCommandError` nếu chụp ảnh thất bại.

**Lưu ý quan trọng:**

*   **Hiệu năng:** Nhận diện hình ảnh là một tác vụ tốn tài nguyên. Việc chụp màn hình, xử lý và so sánh ảnh mất thời gian. Sử dụng `region` để giới hạn vùng tìm kiếm và `use_gray=True` có thể cải thiện hiệu năng đáng kể.
*   **Độ chính xác:** Chất lượng của ảnh mẫu, sự thay đổi về ánh sáng, tỷ lệ, góc xoay trên màn hình thực tế đều ảnh hưởng đến độ chính xác. Cần thử nghiệm với các giá trị `threshold`, `scale_range`, `rotation_range` khác nhau.
*   **Thư viện phụ thuộc:** Chức năng này thường yêu cầu cài đặt các thư viện xử lý ảnh Python như `OpenCV (cv2)` và `NumPy`. Đảm bảo chúng đã được cài đặt trong môi trường của bạn (`pip install opencv-python numpy`).

**Ví dụ sử dụng:**

```python
from oiadb import MyADB
from oiadb.commands import image_interaction
import time
import os

# Giả sử bạn có ảnh mẫu 'calculator_icon.png' trong thư mục hiện tại
template_file = "calculator_icon.png"

# Tạo ảnh mẫu giả (chỉ để ví dụ chạy được)
if not os.path.exists(template_file):
    try:
        from PIL import Image, ImageDraw
        img = Image.new('RGB', (60, 60), color = (73, 109, 137))
        d = ImageDraw.Draw(img)
        d.text((10,10), "CALC", fill=(255,255,0))
        img.save(template_file)
        print(f"Đã tạo file mẫu tạm: {template_file}")
    except ImportError:
        print(f"Vui lòng tạo file ảnh mẫu '{template_file}' hoặc cài đặt Pillow (pip install Pillow) để chạy ví dụ này.")
        exit()

try:
    adb = MyADB()

    # Mở màn hình chính
    adb.run("shell input keyevent HOME")
    time.sleep(1)

    # Tìm icon máy tính
    print(f"Đang tìm hình ảnh '{template_file}'...")
    location = image_interaction.find_image(template_file, threshold=0.7, scale_range=(0.7, 1.3))

    if location:
        x, y, conf = location
        print(f"Tìm thấy tại ({x}, {y}) với độ tin cậy {conf:.2f}")

        # Chạm vào icon
        print("Đang chạm vào hình ảnh...")
        tapped = image_interaction.tap_image(template_file, threshold=0.7, scale_range=(0.7, 1.3))
        if tapped:
            print("Chạm thành công!")
            time.sleep(3) # Chờ ứng dụng mở
            # ... có thể thực hiện các thao tác khác trong ứng dụng ...
            adb.run("shell input keyevent BACK") # Quay lại
        else:
            print("Chạm thất bại (không tìm thấy lại?).")
    else:
        print("Không tìm thấy hình ảnh trên màn hình.")

    # Ví dụ đợi nút "OK" xuất hiện và chạm (giả sử có ảnh 'ok_button.png')
    # ok_button_file = "ok_button.png"
    # if os.path.exists(ok_button_file):
    #     print(f"Đang đợi nút '{ok_button_file}' xuất hiện (tối đa 5s)...")
    #     ok_tapped = image_interaction.wait_and_tap_image(ok_button_file, timeout=5, threshold=0.8)
    #     if ok_tapped:
    #         print("Đã chạm vào nút OK.")
    #     else:
    #         print("Không tìm thấy nút OK trong thời gian chờ.")

except FileNotFoundError:
    print(f"Lỗi: Không tìm thấy file ảnh mẫu '{template_file}'.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")

# Xóa file mẫu tạm nếu đã tạo
# if os.path.exists(template_file) and "Đã tạo file mẫu tạm" in locals().get("creation_message", ""):
#     os.remove(template_file)
#     print(f"Đã xóa file mẫu tạm: {template_file}")
```




---

## 6. Module Utilities (`oiadb.utils`) - Các Tiện ích Nâng cao

Ngoài các lệnh ADB trực tiếp, OIADB còn cung cấp một số module tiện ích để hỗ trợ các tác vụ phức tạp hơn hoặc quản lý thư viện hiệu quả hơn.

### 6.1. `advanced`: Thực thi Bất đồng bộ, Theo dõi Thiết bị và Cache

Module này chứa các lớp hỗ trợ các chức năng nâng cao như chạy lệnh ADB không đồng bộ, theo dõi sự kiện kết nối/ngắt kết nối thiết bị và lưu trữ kết quả lệnh vào bộ nhớ đệm (cache).

**Vị trí:** `oiadb/utils/advanced.py`

**Các lớp chính:**

*   **`CommandResult`:**
    *   **Mô tả:** Một lớp đơn giản để đóng gói kết quả trả về từ một lệnh ADB, bao gồm lệnh gốc, stdout, stderr, mã trả về (return code) và một thuộc tính boolean `success`.
    *   **Thuộc tính:**
        *   `command` (str): Chuỗi lệnh đã thực thi.
        *   `stdout` (str): Output chuẩn (standard output).
        *   `stderr` (str): Output lỗi (standard error).
        *   `return_code` (int): Mã trả về của tiến trình.
        *   `success` (bool): `True` nếu `return_code` là 0, ngược lại là `False`.
    *   **Phương thức:**
        *   `__str__()`: Trả về `stdout` nếu thành công, `stderr` nếu thất bại.
        *   `__bool__()`: Trả về giá trị của `success`.

*   **`AsyncCommandExecutor`:**
    *   **Mô tả:** Cho phép thực thi các lệnh ADB trong một luồng (thread) riêng biệt, không làm chặn luồng chính. Hữu ích cho các lệnh chạy dài như `screenrecord` hoặc `logcat`.
    *   **Phương thức chính:**
        *   `execute(command_id: str, command: List[str], callback: Optional[Callable] = None, timeout: Optional[int] = None)`: Bắt đầu thực thi lệnh trong một luồng mới.
            *   `command_id`: Một ID chuỗi duy nhất để định danh lệnh này.
            *   `command`: Danh sách các thành phần của lệnh (ví dụ: `["adb", "shell", "ls"]`).
            *   `callback`: Một hàm tùy chọn sẽ được gọi khi lệnh hoàn thành. Hàm này nhận một đối tượng `CommandResult` làm tham số.
            *   `timeout`: Thời gian chờ tối đa (giây). Nếu lệnh chạy quá thời gian này, nó sẽ bị hủy.
        *   `get_result(command_id: str) -> Optional[CommandResult]`: Lấy kết quả của lệnh đã hoàn thành. Trả về `None` nếu lệnh chưa xong hoặc không tồn tại.
        *   `is_running(command_id: str) -> bool`: Kiểm tra xem lệnh có đang chạy hay không.
        *   `kill(command_id: str) -> bool`: Cố gắng hủy (kill) một lệnh đang chạy.

*   **`DeviceMonitor`:**
    *   **Mô tả:** Chạy một luồng nền để liên tục kiểm tra danh sách thiết bị kết nối (`adb devices`) và thông báo khi có thiết bị mới kết nối hoặc ngắt kết nối.
    *   **Phương thức chính:**
        *   `start()`: Bắt đầu luồng theo dõi.
        *   `stop()`: Dừng luồng theo dõi.
        *   `add_callback(callback)`: Đăng ký một hàm callback sẽ được gọi khi có sự kiện thay đổi thiết bị. Hàm callback nhận hai tham số: `device_id` (str) và `event_type` (str, là `'connected'` hoặc `'disconnected'`).

*   **`ResultCache`:**
    *   **Mô tả:** Một cơ chế cache đơn giản để lưu trữ kết quả của các lệnh ADB thường dùng (ví dụ: `getprop`). Giúp giảm số lần thực thi lệnh thực tế và tăng tốc độ.
    *   **Phương thức chính:**
        *   `__init__(max_size=100, ttl=60)`: Khởi tạo cache với kích thước tối đa (`max_size`) và thời gian sống (time-to-live - `ttl`, tính bằng giây) cho mỗi mục.
        *   `get(key)`: Lấy giá trị từ cache dựa trên `key`. Trả về `None` nếu không có hoặc đã hết hạn.
        *   `set(key, value)`: Lưu một cặp `key-value` vào cache.
        *   `clear()`: Xóa toàn bộ cache.
        *   `remove(key)`: Xóa một mục cụ thể khỏi cache.

**Ví dụ sử dụng (AsyncCommandExecutor):**

```python
from oiadb import MyADB
from oiadb.utils.advanced import AsyncCommandExecutor
import time
import uuid

def my_callback(result):
    print(f"\n--- Lệnh {result.command} đã hoàn thành ---")
    if result.success:
        print(f"Output:\n{result.stdout[:200]}...") # In 200 ký tự đầu
    else:
        print(f"Lỗi:\n{result.stderr}")

executor = AsyncCommandExecutor()
adb = MyADB() # Giả sử đã kết nối thiết bị

# Chạy lệnh ls bất đồng bộ
cmd_id_ls = str(uuid.uuid4())
print(f"Đang chạy ls (ID: {cmd_id_ls})...")
executor.execute(cmd_id_ls, ["adb", "-s", adb.device_id, "shell", "ls", "-l", "/sdcard/"], callback=my_callback)

# Chạy lệnh screenrecord bất đồng bộ trong 5 giây
cmd_id_rec = str(uuid.uuid4())
remote_video_path = "/sdcard/async_record.mp4"
print(f"Đang chạy screenrecord 5s (ID: {cmd_id_rec})...")
executor.execute(cmd_id_rec, 
                 ["adb", "-s", adb.device_id, "shell", "screenrecord", "--time-limit", "5", remote_video_path],
                 callback=my_callback)

# Làm gì đó khác trong khi lệnh chạy...
print("Đang chờ các lệnh hoàn thành...")
running_count = 2
while running_count > 0:
    running_count = 0
    if executor.is_running(cmd_id_ls):
        running_count += 1
        print(".", end="", flush=True)
    if executor.is_running(cmd_id_rec):
        running_count += 1
        print("+", end="", flush=True)
    time.sleep(0.5)

print("\nTất cả các lệnh bất đồng bộ đã kết thúc (hoặc bị hủy).")

# Lấy kết quả (nếu cần)
ls_result = executor.get_result(cmd_id_ls)
rec_result = executor.get_result(cmd_id_rec)

# Dọn dẹp file video trên thiết bị
if rec_result and rec_result.success:
    try:
        adb.run(f"shell rm {remote_video_path}")
        print(f"Đã xóa {remote_video_path}")
    except Exception as e:
        print(f"Lỗi khi xóa video: {e}")

```

**Ví dụ sử dụng (DeviceMonitor):**

```python
from oiadb.utils.advanced import DeviceMonitor
import time

def device_event_handler(device_id, event_type):
    print(f"Sự kiện: Thiết bị {device_id} vừa {event_type}.")

monitor = DeviceMonitor()
monitor.add_callback(device_event_handler)

print("Bắt đầu theo dõi thiết bị (Nhấn Ctrl+C để dừng)...")
monitor.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nDừng theo dõi...")
    monitor.stop()
    print("Đã dừng.")
```




---

## 7. Hướng dẫn Đóng góp (Contribution Guidelines)

Chúng tôi hoan nghênh và khuyến khích mọi đóng góp để cải thiện OIADB! Dù là báo lỗi, đề xuất tính năng mới, cải thiện tài liệu hay viết mã, sự tham gia của bạn đều rất quan trọng.

### 7.1. Báo cáo Lỗi (Reporting Bugs)

Nếu bạn gặp lỗi khi sử dụng OIADB, vui lòng kiểm tra các vấn đề (Issues) đã tồn tại trên kho GitHub [https://github.com/tiendung2k03/oiadb/issues](https://github.com/tiendung2k03/oiadb/issues) để xem lỗi đã được báo cáo chưa.

Nếu chưa, hãy tạo một Issue mới với các thông tin sau:

*   **Tiêu đề rõ ràng:** Mô tả ngắn gọn về lỗi.
*   **Phiên bản OIADB:** Phiên bản bạn đang sử dụng (`pip show oiadb`).
*   **Phiên bản Python:** Phiên bản Python bạn đang dùng (`python --version`).
*   **Hệ điều hành:** Hệ điều hành máy tính của bạn (Windows, macOS, Linux).
*   **Thông tin thiết bị Android:** Model thiết bị, phiên bản Android.
*   **Các bước tái hiện lỗi (Steps to Reproduce):** Mô tả chi tiết từng bước để chúng tôi có thể tái hiện lỗi.
*   **Hành vi mong đợi (Expected Behavior):** Điều gì đáng lẽ phải xảy ra.
*   **Hành vi thực tế (Actual Behavior):** Điều gì đã thực sự xảy ra.
*   **Thông báo lỗi đầy đủ (Error Messages/Traceback):** Sao chép và dán toàn bộ thông báo lỗi hoặc traceback.
*   **Ảnh chụp màn hình/Video (nếu có):** Hình ảnh hoặc video minh họa lỗi sẽ rất hữu ích.

### 7.2. Đề xuất Tính năng (Suggesting Enhancements)

Nếu bạn có ý tưởng về tính năng mới hoặc cải tiến cho OIADB, hãy:

1.  Kiểm tra danh sách Issues và Pull Requests đang mở để xem ý tưởng đã được đề xuất hoặc đang được thực hiện chưa.
2.  Nếu chưa, hãy tạo một Issue mới với nhãn (label) là `enhancement`.
3.  Mô tả chi tiết về tính năng bạn đề xuất:
    *   Vấn đề mà tính năng này giải quyết.
    *   Cách hoạt động của tính năng (hành vi mong muốn).
    *   Ví dụ về cách sử dụng (nếu có thể).
    *   Tại sao bạn nghĩ tính năng này hữu ích cho cộng đồng.

### 7.3. Đóng góp Mã nguồn (Contributing Code)

Nếu bạn muốn đóng góp mã nguồn, vui lòng tuân theo quy trình sau:

1.  **Fork Kho lưu trữ:** Tạo một bản sao (fork) của kho lưu trữ `tiendung2k03/oiadb` về tài khoản GitHub của bạn.
2.  **Clone Fork:** Sao chép (clone) fork về máy tính của bạn:
    ```bash
    git clone https://github.com/YOUR_USERNAME/oiadb.git
    cd oiadb
    ```
3.  **Tạo Nhánh Mới (New Branch):** Tạo một nhánh mới cho thay đổi của bạn. Đặt tên nhánh rõ ràng, ví dụ: `feature/add-new-command` hoặc `fix/resolve-issue-123`.
    ```bash
    git checkout -b feature/your-feature-name
    ```
4.  **Phát triển và Kiểm thử:**
    *   Viết mã nguồn cho tính năng mới hoặc sửa lỗi.
    *   Tuân thủ phong cách mã (coding style) hiện có của dự án (ví dụ: PEP 8 cho Python).
    *   Thêm các bài kiểm thử (tests) mới cho thay đổi của bạn nếu có thể.
    *   Đảm bảo tất cả các bài kiểm thử hiện có đều vượt qua.
    *   Cập nhật tài liệu (README, docstrings) nếu cần thiết.
5.  **Commit Thay đổi:** Thực hiện commit các thay đổi của bạn với thông điệp commit rõ ràng.
    ```bash
    git add .
    git commit -m "feat: Add feature X that does Y" 
    # Hoặc "fix: Resolve issue Z by doing W"
    ```
6.  **Đẩy Nhánh lên Fork:** Đẩy nhánh mới của bạn lên fork trên GitHub.
    ```bash
    git push origin feature/your-feature-name
    ```
7.  **Tạo Pull Request (PR):**
    *   Truy cập kho lưu trữ fork của bạn trên GitHub.
    *   Nhấn nút "Compare & pull request".
    *   Chọn nhánh cơ sở (base branch) là `main` (hoặc nhánh phát triển chính) của kho `tiendung2k03/oiadb`.
    *   Chọn nhánh so sánh (compare branch) là nhánh bạn vừa đẩy lên (`feature/your-feature-name`).
    *   Viết tiêu đề và mô tả rõ ràng cho PR, giải thích những thay đổi bạn đã thực hiện và tại sao.
    *   Nếu PR của bạn giải quyết một Issue cụ thể, hãy liên kết đến Issue đó (ví dụ: `Closes #123`).
    *   Gửi Pull Request.

8.  **Review và Hợp nhất:** Người quản lý dự án sẽ xem xét PR của bạn, có thể yêu cầu thay đổi hoặc thảo luận thêm. Sau khi được chấp thuận, PR sẽ được hợp nhất vào kho lưu trữ chính.

### 7.4. Phong cách Mã (Coding Style)

*   **Python:** Tuân thủ theo [PEP 8 Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/). Sử dụng công cụ định dạng như `black` và kiểm tra lỗi như `flake8` được khuyến khích.
*   **Docstrings:** Sử dụng docstrings theo định dạng Google Style hoặc reStructuredText để mô tả các lớp, phương thức và hàm.
*   **Commit Messages:** Viết thông điệp commit rõ ràng, súc tích, theo quy ước [Conventional Commits](https://www.conventionalcommits.org/) nếu có thể.

Cảm ơn bạn đã quan tâm và đóng góp cho sự phát triển của OIADB!



---

## 8. Xử lý sự cố và Câu hỏi thường gặp (Troubleshooting & FAQ)

Phần này cung cấp giải pháp cho các vấn đề phổ biến và trả lời một số câu hỏi thường gặp khi sử dụng ADB và thư viện OIADB.

### 8.1. Lỗi Kết nối Thiết bị

*   **Vấn đề:** `adb devices` hiển thị thiết bị là `offline` hoặc `unauthorized`.
    *   **Giải pháp (`offline`):**
        *   Kiểm tra cáp USB và cổng kết nối. Thử cáp/cổng khác.
        *   Khởi động lại thiết bị và máy tính.
        *   Chạy `adb kill-server` và sau đó `adb start-server`.
        *   Trên thiết bị, vào Tùy chọn nhà phát triển, tắt và bật lại Gỡ lỗi USB.
    *   **Giải pháp (`unauthorized`):**
        *   Đảm bảo bạn đã cho phép gỡ lỗi USB từ máy tính này trên màn hình thiết bị (sẽ có hộp thoại yêu cầu xác nhận dấu vân tay RSA).
        *   Nếu không thấy hộp thoại, vào Tùy chọn nhà phát triển, chọn "Thu hồi ủy quyền gỡ lỗi USB" (Revoke USB debugging authorizations), sau đó kết nối lại thiết bị.
        *   Kiểm tra lại cáp và cổng USB.

*   **Vấn đề:** Không thể kết nối qua Wi-Fi (`adb connect <ip>:<port>`).
    *   **Giải pháp:**
        *   Đảm bảo thiết bị và máy tính đang ở cùng một mạng Wi-Fi.
        *   Kiểm tra xem bạn đã bật Gỡ lỗi USB và Gỡ lỗi qua Wi-Fi (hoặc chạy `adb tcpip 5555` qua USB trước) trên thiết bị chưa.
        *   Kiểm tra địa chỉ IP và cổng của thiết bị có chính xác không.
        *   Tường lửa trên máy tính hoặc router có thể chặn kết nối. Thử tạm thời tắt tường lửa để kiểm tra.
        *   Đối với Android 11+, hãy sử dụng cơ chế ghép nối (pairing) nếu kết nối trực tiếp không thành công (xem phần `connect.connect_pair`).

### 8.2. Lỗi Thực thi Lệnh OIADB

*   **Vấn đề:** Nhận được ngoại lệ `ADBCommandError` hoặc `FileOperationError`.
    *   **Giải pháp:**
        *   Đọc kỹ thông báo lỗi (`e.error_message`) để hiểu nguyên nhân.
        *   Kiểm tra xem lệnh ADB tương đương có chạy được trực tiếp trên terminal không. Ví dụ, nếu `file_ops.pull("/sdcard/file.txt", "./file.txt")` lỗi, hãy thử `adb pull /sdcard/file.txt ./file.txt`.
        *   Đảm bảo đường dẫn file/thư mục trên thiết bị và máy tính là chính xác.
        *   Kiểm tra quyền truy cập. Một số lệnh (`setprop`, `rm /system/...`) yêu cầu quyền root (`adb root`). Một số thao tác file có thể bị chặn bởi quyền của ứng dụng hoặc SELinux.
        *   Đối với `FileOperationError` khi `push` hoặc `pull`, kiểm tra dung lượng trống trên thiết bị và máy tính.

*   **Vấn đề:** Lệnh tương tác (`tap`, `swipe`, `text_input`) không hoạt động như mong đợi.
    *   **Giải pháp:**
        *   Tọa độ (x, y) có thể không chính xác. Sử dụng Tùy chọn nhà phát triển > Hiển thị vị trí con trỏ (Show pointer location) để xác định tọa độ đúng.
        *   `text_input` có thể không hoạt động với một số bàn phím hoặc ứng dụng. Thử sử dụng `key_event` để mô phỏng gõ từng ký tự (phức tạp hơn).
        *   Đảm bảo màn hình thiết bị đang bật và không bị khóa khi thực hiện lệnh tương tác.

*   **Vấn đề:** Nhận diện hình ảnh (`find_image`, `tap_image`) không tìm thấy ảnh mẫu.
    *   **Giải pháp:**
        *   **Chất lượng ảnh mẫu:** Đảm bảo ảnh mẫu rõ ràng, không bị nhiễu, và khớp với yếu tố trên màn hình.
        *   **Ngưỡng (`threshold`):** Thử giảm giá trị `threshold` (ví dụ: 0.7 hoặc 0.65) nếu ảnh trên màn hình có thể hơi khác mẫu. Tuy nhiên, giảm quá thấp có thể dẫn đến kết quả sai.
        *   **Vùng tìm kiếm (`region`):** Nếu biết ảnh chỉ xuất hiện ở một khu vực cụ thể, hãy chỉ định `region` để tăng tốc độ và độ chính xác.
        *   **Tỷ lệ (`scale_range`):** Nếu kích thước ảnh trên màn hình có thể thay đổi, hãy điều chỉnh `scale_range` và `scale_steps`.
        *   **Xoay (`rotation_range`):** Nếu ảnh có thể bị xoay, hãy thử nghiệm với `rotation_range`.
        *   **Ảnh xám (`use_gray`) và Canny (`use_canny`):** Thử bật/tắt các tùy chọn này để xem có cải thiện không. `use_canny=True` có thể hữu ích với ảnh mờ hoặc icon có viền rõ.
        *   **Chụp màn hình kiểm tra:** Sử dụng `save_screenshot` để chụp lại màn hình thiết bị tại thời điểm tìm kiếm và so sánh thủ công với ảnh mẫu.

### 8.3. Câu hỏi thường gặp (FAQ)

*   **Hỏi:** Làm cách nào để chạy lệnh ADB cho một thiết bị cụ thể nếu có nhiều thiết bị đang kết nối?
    *   **Đáp:** Khởi tạo đối tượng `MyADB` với `device_id` cụ thể: `adb = MyADB(device_id="YOUR_DEVICE_SERIAL_OR_IP")`. Tất cả các lệnh sau đó sẽ nhắm vào thiết bị đó. Hoặc sử dụng `basic.custom_command(device_id, command)`.

*   **Hỏi:** OIADB có hỗ trợ Fastboot không?
    *   **Đáp:** Dựa trên tài liệu hiện tại, OIADB chủ yếu tập trung vào các lệnh ADB. Mặc dù có lệnh `reboot_bootloader` (hoặc `reboot_fastboot`), thư viện không cung cấp các lệnh Fastboot chuyên dụng (như `fastboot devices`, `fastboot flash`, `fastboot boot`). Bạn cần sử dụng công cụ `fastboot` riêng.

*   **Hỏi:** Làm thế nào để xử lý các lệnh ADB yêu cầu tương tác người dùng (ví dụ: xác nhận sao lưu trên màn hình)?
    *   **Đáp:** OIADB (và ADB nói chung) không thể tự động hóa các tương tác yêu cầu xác nhận vật lý trên màn hình thiết bị. Bạn cần phải tự xác nhận trên thiết bị khi lệnh như `backup` hoặc `restore` chạy.

*   **Hỏi:** Thư viện có tương thích với tất cả các phiên bản Android không?
    *   **Đáp:** Hầu hết các lệnh ADB cơ bản hoạt động trên nhiều phiên bản Android. Tuy nhiên, một số lệnh (`dumpsys`, `wm`, `pm grant/revoke`, Gỡ lỗi không dây) có thể có cú pháp hoặc hành vi khác nhau giữa các phiên bản. Luôn kiểm tra trên thiết bị mục tiêu của bạn.

*   **Hỏi:** Làm cách nào để cài đặt OIADB?
    *   **Đáp:** Sử dụng pip: `pip install oiadb`.

---

