import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, FancyArrowPatch

# Tạo hình ảnh sơ đồ cấu trúc gói
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')

# Vẽ các hộp module
modules = {
    'MyADB': (5, 7, 2, 0.8),  # x, y, width, height
    'commands': (5, 5, 2, 0.8),
    'utils': (5, 3, 2, 0.8),
    'exceptions': (5, 1, 2, 0.8),
}

# Vẽ các module con của commands
command_modules = {
    'interaction': (2, 5.5, 1.5, 0.6),
    'image_interaction': (2, 4.5, 1.5, 0.6),
    'app_info': (8, 5.5, 1.5, 0.6),
    'file_ops': (8, 4.5, 1.5, 0.6),
}

# Màu sắc
colors = {
    'main': '#4285F4',  # Google Blue
    'commands': '#EA4335',  # Google Red
    'utils': '#FBBC05',  # Google Yellow
    'exceptions': '#34A853',  # Google Green
    'command_modules': '#DB4437',  # Lighter Red
}

# Vẽ các hộp module chính
for name, (x, y, w, h) in modules.items():
    color = colors['main'] if name == 'MyADB' else colors[name.lower()]
    rect = Rectangle((x-w/2, y-h/2), w, h, linewidth=1, edgecolor='black', facecolor=color, alpha=0.7)
    ax.add_patch(rect)
    ax.text(x, y, name, ha='center', va='center', fontsize=12, fontweight='bold', color='white')

# Vẽ các module con
for name, (x, y, w, h) in command_modules.items():
    rect = Rectangle((x-w/2, y-h/2), w, h, linewidth=1, edgecolor='black', facecolor=colors['command_modules'], alpha=0.6)
    ax.add_patch(rect)
    ax.text(x, y, name, ha='center', va='center', fontsize=10, color='white')

# Vẽ các mũi tên kết nối
arrows = [
    # Từ MyADB đến commands
    (5, 6.6, 5, 5.4),
    # Từ commands đến các module con
    (4, 5, 2.75, 5.5),
    (4, 5, 2.75, 4.5),
    (6, 5, 7.25, 5.5),
    (6, 5, 7.25, 4.5),
    # Từ MyADB đến utils
    (5, 6.2, 5, 3.4),
    # Từ MyADB đến exceptions
    (5, 6.2, 5, 1.4),
]

for x1, y1, x2, y2 in arrows:
    arrow = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='->', linewidth=1, color='black', connectionstyle='arc3,rad=0.1')
    ax.add_patch(arrow)

# Thêm tiêu đề
ax.text(5, 7.8, 'OIADB Package Structure', ha='center', va='center', fontsize=16, fontweight='bold')

# Lưu hình ảnh
plt.savefig('/home/ubuntu/workspace/oiadb/docs/images/package_structure.png', dpi=300, bbox_inches='tight')
plt.close()
