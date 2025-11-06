#!/usr/bin/env python3
"""
Script to generate a markdown gallery from images in specific folders.
Ignores images outside the specified folders.
"""

from pathlib import Path
from urllib.parse import quote

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
    lines = []
    
    # Header
    lines.append("# Thư viện Dự án Kiến trúc")
    lines.append("")
    lines.append("Bộ sưu tập các dự án kiến trúc được phân loại theo từng loại công trình.")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Instructions
    lines.append("### Hướng dẫn sử dụng")
    lines.append("")
    lines.append("1. **Thêm hình ảnh**: Đặt hình ảnh vào các thư mục tương ứng:")
    lines.append("   - `1. BIỆT THỰ/` - Dự án biệt thự")
    lines.append("   - `2. NHÀ PHỐ/` - Dự án nhà phố")
    lines.append("   - `3. Công Trình Công cộng/` - Các công trình công cộng")
    lines.append("")
    lines.append("2. **Cập nhật thư viện**: Chạy lệnh sau để tự động tạo lại thư viện:")
    lines.append("   ```bash")
    lines.append("   python3 generate_gallery.py")
    lines.append("   ```")
    lines.append("")
    lines.append("3. **Lưu ý**: Chỉ hình ảnh trong 3 thư mục trên mới được hiển thị. Hình ảnh ngoài các thư mục này sẽ bị bỏ qua.")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    repo_root = Path(__file__).parent
    
    for folder_name in FOLDERS:
        folder_path = repo_root / folder_name
        images = get_images_in_folder(folder_path)
        
        # Add folder heading
        lines.append(f"## {folder_name}")
        lines.append("")
        
        if images:
            # Add each image as an embedded link
            for image in images:
                # Use relative path from repo root
                relative_path = image.relative_to(repo_root)
                # Properly URL encode the path for markdown
                image_url = quote(str(relative_path))
                image_name = image.stem.replace("_", " ").replace("-", " ")
                
                lines.append(f"![{image_name}]({image_url})")
                lines.append("")
        else:
            lines.append("*Chưa có hình ảnh*")
            lines.append("")
    
    return "\n".join(lines)

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
