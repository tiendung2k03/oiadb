import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, FancyArrowPatch, Ellipse

# Tạo hình ảnh sơ đồ quy trình XML dump
fig, ax = plt.subplots(figsize=(14, 8))
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.axis('off')

# Định nghĩa các thành phần trong quy trình
components = [
    ('Local Server', 2, 6.5, '#4285F4'),  # HTTP Server
    ('XML Parser', 2, 4.5, '#EA4335'),  # XML Parser
    ('Parameter Handler', 2, 2.5, '#FBBC05'),  # Parameter Handler
    ('UI Hierarchy', 5, 6.5, '#34A853'),  # UI Hierarchy
    ('Accessibility API', 5, 2.5, '#DB4437'),  # Accessibility API
    ('Client Application', 9, 4.5, '#4285F4'),  # Client Application
]

# Định nghĩa các API endpoints
endpoints = [
    ('/get_xml', 5, 5.5, '#EA4335'),
    ('/find_elements', 5, 4.5, '#FBBC05'),
    ('/accessibility_actions', 5, 3.5, '#34A853'),
]

# Vẽ các thành phần
for name, x, y, color in components:
    ellipse = Ellipse((x, y), 2.5, 1.2, linewidth=1, edgecolor='black', facecolor=color, alpha=0.7)
    ax.add_patch(ellipse)
    ax.text(x, y, name, ha='center', va='center', fontsize=12, fontweight='bold', color='white')

# Vẽ các API endpoints
for name, x, y, color in endpoints:
    rect = Rectangle((x-1.5, y-0.4), 3, 0.8, linewidth=1, edgecolor='black', facecolor=color, alpha=0.7)
    ax.add_patch(rect)
    ax.text(x, y, name, ha='center', va='center', fontsize=11, fontweight='bold', color='white')

# Vẽ các mũi tên kết nối
arrows = [
    # Local Server đến API endpoints
    (3, 6.5, 3.5, 5.5),
    (3, 6.5, 3.5, 4.5),
    (3, 6.5, 3.5, 3.5),
    
    # XML Parser đến API endpoints
    (3, 4.5, 3.5, 5.5),
    (3, 4.5, 3.5, 4.5),
    
    # Parameter Handler đến API endpoints
    (3, 2.5, 3.5, 4.5),
    (3, 2.5, 3.5, 3.5),
    
    # API endpoints đến UI Hierarchy
    (6.5, 5.5, 6, 6.5),
    
    # API endpoints đến Accessibility API
    (6.5, 3.5, 6, 2.5),
    
    # API endpoints đến Client Application
    (6.5, 5.5, 7.5, 4.5),
    (6.5, 4.5, 7.5, 4.5),
    (6.5, 3.5, 7.5, 4.5),
]

for x1, y1, x2, y2 in arrows:
    arrow = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='->', linewidth=1.5, color='black', connectionstyle='arc3,rad=0.1')
    ax.add_patch(arrow)

# Thêm mô tả cho các thành phần
descriptions = [
    (2, 7.5, "HTTP Server cung cấp\ncác API endpoints"),
    (2, 3.5, "Xử lý và lọc XML\ndựa trên tham số"),
    (5, 7.5, "Cấu trúc UI của\nứng dụng Android"),
    (5, 1.5, "Tương tác với các\nphần tử UI"),
    (9, 5.5, "Ứng dụng sử dụng\nXML dump API"),
]

for x, y, text in descriptions:
    ax.text(x, y, text, ha='center', va='center', fontsize=9, color='black', 
            bbox=dict(facecolor='white', alpha=0.7, boxstyle='round,pad=0.5'))

# Thêm tiêu đề
ax.text(6, 7.8, 'OIADB XML Dump Architecture', ha='center', va='center', fontsize=16, fontweight='bold')

# Lưu hình ảnh
plt.savefig('/home/ubuntu/doc_update/oiadb/docs/images/xml_dump_architecture.png', dpi=300, bbox_inches='tight')
plt.close()

# Tạo hình ảnh sơ đồ luồng xử lý XML dump
fig, ax = plt.subplots(figsize=(14, 8))
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.axis('off')

# Định nghĩa các bước trong quy trình
steps = [
    ('HTTP Request', 1, 6, '#4285F4'),
    ('Parameter Parsing', 3, 6, '#EA4335'),
    ('UI Dump Command', 5, 6, '#FBBC05'),
    ('XML Generation', 7, 6, '#34A853'),
    ('XML Filtering', 9, 6, '#DB4437'),
    ('HTTP Response', 11, 6, '#4285F4'),
    
    ('Find Elements', 3, 4, '#EA4335'),
    ('Fuzzy Matching', 5, 4, '#FBBC05'),
    ('Element Selection', 7, 4, '#34A853'),
    ('JSON Response', 9, 4, '#DB4437'),
    
    ('Accessibility Query', 3, 2, '#EA4335'),
    ('Action Detection', 5, 2, '#FBBC05'),
    ('Action Execution', 7, 2, '#34A853'),
    ('Result Response', 9, 2, '#DB4437'),
]

# Vẽ các bước
for name, x, y, color in steps:
    rect = Rectangle((x-1, y-0.4), 2, 0.8, linewidth=1, edgecolor='black', facecolor=color, alpha=0.7)
    ax.add_patch(rect)
    ax.text(x, y, name, ha='center', va='center', fontsize=10, fontweight='bold', color='white')

# Vẽ các mũi tên kết nối
# Luồng XML dump
for i in range(5):
    arrow = FancyArrowPatch((2*i+2, 6), (2*i+3, 6), arrowstyle='->', linewidth=1.5, color='black')
    ax.add_patch(arrow)

# Luồng Find Elements
for i in range(3):
    arrow = FancyArrowPatch((2*i+4, 4), (2*i+5, 4), arrowstyle='->', linewidth=1.5, color='black')
    ax.add_patch(arrow)

# Luồng Accessibility
for i in range(3):
    arrow = FancyArrowPatch((2*i+4, 2), (2*i+5, 2), arrowstyle='->', linewidth=1.5, color='black')
    ax.add_patch(arrow)

# Kết nối giữa các luồng
arrow1 = FancyArrowPatch((1, 5.6), (1, 4.4), arrowstyle='->', linewidth=1.5, color='black', connectionstyle='arc3,rad=-0.3')
ax.add_patch(arrow1)
arrow2 = FancyArrowPatch((1, 3.6), (1, 2.4), arrowstyle='->', linewidth=1.5, color='black', connectionstyle='arc3,rad=-0.3')
ax.add_patch(arrow2)

# Thêm nhãn cho các luồng
ax.text(6, 6.8, 'XML Dump Flow', ha='center', va='center', fontsize=12, fontweight='bold')
ax.text(6, 4.8, 'Find Elements Flow', ha='center', va='center', fontsize=12, fontweight='bold')
ax.text(6, 2.8, 'Accessibility Flow', ha='center', va='center', fontsize=12, fontweight='bold')

# Thêm tiêu đề
ax.text(6, 7.5, 'OIADB XML Dump Workflow', ha='center', va='center', fontsize=16, fontweight='bold')

# Lưu hình ảnh
plt.savefig('/home/ubuntu/doc_update/oiadb/docs/images/xml_dump_workflow.png', dpi=300, bbox_inches='tight')
plt.close()
