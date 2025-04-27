import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, FancyArrowPatch, Ellipse

# Tạo hình ảnh sơ đồ quy trình nhận diện hình ảnh
fig, ax = plt.subplots(figsize=(14, 8))
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.axis('off')

# Định nghĩa các bước trong quy trình
steps = [
    ('Input Image', 1.5, 6, '#4285F4'),  # Hình ảnh mẫu
    ('Screen Capture', 1.5, 4, '#4285F4'),  # Chụp màn hình thiết bị
    ('Image Processing', 4, 5, '#EA4335'),  # Xử lý hình ảnh
    ('Template Matching', 6.5, 5, '#FBBC05'),  # So khớp mẫu
    ('Match Detection', 9, 5, '#34A853'),  # Phát hiện vị trí khớp
    ('Device Interaction', 9, 3, '#DB4437'),  # Tương tác với thiết bị
]

# Vẽ các hộp bước
for name, x, y, color in steps:
    if name in ['Input Image', 'Screen Capture']:
        # Hình chữ nhật cho hình ảnh
        rect = Rectangle((x-1, y-0.7), 2, 1.4, linewidth=1, edgecolor='black', facecolor=color, alpha=0.7)
        ax.add_patch(rect)
    else:
        # Hình elip cho các bước xử lý
        ellipse = Ellipse((x, y), 2.5, 1.4, linewidth=1, edgecolor='black', facecolor=color, alpha=0.7)
        ax.add_patch(ellipse)
    
    ax.text(x, y, name, ha='center', va='center', fontsize=11, fontweight='bold', color='white')

# Vẽ các mũi tên kết nối
arrows = [
    # Từ Input Image đến Image Processing
    (2.5, 6, 3, 5.3),
    # Từ Screen Capture đến Image Processing
    (2.5, 4, 3, 4.7),
    # Từ Image Processing đến Template Matching
    (5.25, 5, 5.5, 5),
    # Từ Template Matching đến Match Detection
    (7.75, 5, 8, 5),
    # Từ Match Detection đến Device Interaction
    (9, 4.3, 9, 3.7),
]

for x1, y1, x2, y2 in arrows:
    arrow = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='->', linewidth=1.5, color='black', connectionstyle='arc3,rad=0.1')
    ax.add_patch(arrow)

# Thêm mô tả cho các bước
descriptions = [
    (1.5, 5.2, "Template image\nto search for"),
    (1.5, 3.2, "Current device\nscreen state"),
    (4, 4.2, "Preprocessing:\nGrayscale, Resize,\nNormalization"),
    (6.5, 4.2, "OpenCV matching\nalgorithms"),
    (9, 4.2, "Coordinates of\nbest matches"),
    (9, 2.2, "Tap, swipe or\nother actions"),
]

for x, y, text in descriptions:
    ax.text(x, y, text, ha='center', va='center', fontsize=9, color='black', 
            bbox=dict(facecolor='white', alpha=0.7, boxstyle='round,pad=0.5'))

# Thêm tiêu đề
ax.text(6, 7.5, 'OIADB Image Recognition Workflow', ha='center', va='center', fontsize=16, fontweight='bold')

# Lưu hình ảnh
plt.savefig('/home/ubuntu/workspace/oiadb/docs/images/image_recognition_workflow.png', dpi=300, bbox_inches='tight')
plt.close()
