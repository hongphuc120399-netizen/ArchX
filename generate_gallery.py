#!/usr/bin/env python3
"""
Script to generate a markdown gallery from images in specific folders.
Ignores images outside the specified folders.
"""

import os
from pathlib import Path

# Define the folders to scan
FOLDERS = [
    "1. BIỆT THỰ",
    "2. NHÀ PHỐ", 
    "3. Công Trình Công cộng"
]

# Supported image extensions
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp', '.svg'}

def get_images_in_folder(folder_path):
    """Get all image files in a folder."""
    images = []
    folder = Path(folder_path)
    
    if not folder.exists():
        return images
    
    for file in sorted(folder.iterdir()):
        if file.is_file() and file.suffix.lower() in IMAGE_EXTENSIONS:
            images.append(file)
    
    return images

def generate_markdown():
    """Generate markdown content with embedded image links."""
    markdown_lines = ["# Thư viện Dự án Kiến trúc\n"]
    markdown_lines.append("Bộ sưu tập các dự án kiến trúc được phân loại theo từng loại công trình.\n")
    markdown_lines.append("\n---\n")
    markdown_lines.append("\n### Hướng dẫn sử dụng\n")
    markdown_lines.append("\n1. **Thêm hình ảnh**: Đặt hình ảnh vào các thư mục tương ứng:")
    markdown_lines.append("\n   - `1. BIỆT THỰ/` - Dự án biệt thự")
    markdown_lines.append("\n   - `2. NHÀ PHỐ/` - Dự án nhà phố")
    markdown_lines.append("\n   - `3. Công Trình Công cộng/` - Các công trình công cộng\n")
    markdown_lines.append("\n2. **Cập nhật thư viện**: Chạy lệnh sau để tự động tạo lại thư viện:")
    markdown_lines.append("\n   ```bash")
    markdown_lines.append("\n   python3 generate_gallery.py")
    markdown_lines.append("\n   ```\n")
    markdown_lines.append("\n3. **Lưu ý**: Chỉ hình ảnh trong 3 thư mục trên mới được hiển thị. Hình ảnh ngoài các thư mục này sẽ bị bỏ qua.\n")
    markdown_lines.append("\n---\n")
    
    repo_root = Path(__file__).parent
    
    for folder_name in FOLDERS:
        folder_path = repo_root / folder_name
        images = get_images_in_folder(folder_path)
        
        if images:
            # Add folder heading
            markdown_lines.append(f"\n## {folder_name}\n")
            
            # Add each image as an embedded link
            for image in images:
                # Use relative path from repo root
                relative_path = image.relative_to(repo_root)
                # URL encode the path for markdown
                image_url = str(relative_path).replace(" ", "%20")
                image_name = image.stem.replace("_", " ").replace("-", " ")
                
                markdown_lines.append(f"![{image_name}]({image_url})\n")
        else:
            # Add folder heading even if empty
            markdown_lines.append(f"\n## {folder_name}\n")
            markdown_lines.append("*Chưa có hình ảnh*\n")
    
    return "\n".join(markdown_lines)

def main():
    """Main function to generate README.md."""
    markdown_content = generate_markdown()
    
    # Write to README.md
    readme_path = Path(__file__).parent / "README.md"
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"✓ Generated {readme_path}")
    print(f"✓ Processed {len(FOLDERS)} folders")

if __name__ == "__main__":
    main()
