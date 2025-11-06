# Công Trình Công Cộng - Embeddable Image Links

This file contains HTTP URLs for **Công Trình Công Cộng (Public Buildings)** images that can be embedded directly into your applications.

## 🔗 Usage

All images are hosted on GitHub and can be accessed via raw URLs. These links can be used in:
- HTML `<img>` tags
- CSS `background-image`
- Markdown image syntax
- JavaScript/TypeScript fetch/axios requests
- Mobile app image loaders (React Native, Flutter, iOS, Android)
- Any HTTP client

## 📋 Base URL

```
https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/
```

---

## 🏢 Công Trình Công Cộng (Public Buildings) - 11 Images

| # | Filename | Embeddable URL |
|---|----------|----------------|
| 1 | 9b1fa2681a1a9644cf0b.jpg | `https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/9b1fa2681a1a9644cf0b.jpg` |
| 2 | 9cbf90c822baaee4f7ab.jpg | `https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/9cbf90c822baaee4f7ab.jpg` |
| 3 | 9f6f24198b6b07355e7a.jpg | `https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/9f6f24198b6b07355e7a.jpg` |
| 4 | 9f94759702ea8eb4d7fb.jpg | `https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/9f94759702ea8eb4d7fb.jpg` |
| 5 | a05915e293901fce4681.jpg | `https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/a05915e293901fce4681.jpg` |
| 6 | a14aec384c4ac014995b.jpg | `https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/a14aec384c4ac014995b.jpg` |
| 7 | a36cdd9275e0f9bea0f1.jpg | `https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/a36cdd9275e0f9bea0f1.jpg` |
| 8 | b1908fb035c2b99ce0d3.jpg | `https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/b1908fb035c2b99ce0d3.jpg` |
| 9 | c8e0a3d70fa583fbdab4.jpg | `https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/c8e0a3d70fa583fbdab4.jpg` |
| 10 | e3e513c474b9f8e7a1a8.jpg | `https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/e3e513c474b9f8e7a1a8.jpg` |
| 11 | ee96199ba9e925b77cf8.jpg | `https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/ee96199ba9e925b77cf8.jpg` |

---

## 💡 Usage Examples

### HTML
```html
<img src="https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/9b1fa2681a1a9644cf0b.jpg" 
     alt="Public Building Architecture">
```

### Markdown
```markdown
![Public Building](https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/9b1fa2681a1a9644cf0b.jpg)
```

### CSS
```css
.public-building-hero {
    background-image: url('https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/9b1fa2681a1a9644cf0b.jpg');
    background-size: cover;
    background-position: center;
}
```

### JavaScript/TypeScript
```javascript
const publicBuildingImages = [
    'https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/9b1fa2681a1a9644cf0b.jpg',
    'https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/9cbf90c822baaee4f7ab.jpg',
    // ... more images
];

// Fetch image
fetch(publicBuildingImages[0])
    .then(response => response.blob())
    .then(blob => {
        const imageUrl = URL.createObjectURL(blob);
        document.getElementById('myImage').src = imageUrl;
    });
```

### React
```jsx
import React from 'react';

const PublicBuildingGallery = () => {
    const images = [
        'https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/9b1fa2681a1a9644cf0b.jpg',
        'https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/9cbf90c822baaee4f7ab.jpg',
    ];

    return (
        <div className="gallery">
            {images.map((img, idx) => (
                <img 
                    key={idx} 
                    src={img} 
                    alt={`Public Building ${idx + 1}`} 
                    loading="lazy"
                />
            ))}
        </div>
    );
};

export default PublicBuildingGallery;
```

### React Native
```jsx
import { Image, ScrollView } from 'react-native';

const PublicBuildingScreen = () => {
    const imageUrl = 'https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/9b1fa2681a1a9644cf0b.jpg';
    
    return (
        <ScrollView>
            <Image 
                source={{ uri: imageUrl }}
                style={{ width: '100%', height: 300 }}
                resizeMode="cover"
            />
        </ScrollView>
    );
};
```

### Flutter/Dart
```dart
import 'package:flutter/material.dart';

class PublicBuildingImage extends StatelessWidget {
  final String imageUrl = 'https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/9b1fa2681a1a9644cf0b.jpg';
  
  @override
  Widget build(BuildContext context) {
    return Image.network(
      imageUrl,
      fit: BoxFit.cover,
      loadingBuilder: (context, child, loadingProgress) {
        if (loadingProgress == null) return child;
        return CircularProgressIndicator();
      },
    );
  }
}
```

### Swift/iOS
```swift
import UIKit

class PublicBuildingViewController: UIViewController {
    let imageView = UIImageView()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let urlString = "https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/9b1fa2681a1a9644cf0b.jpg"
        if let url = URL(string: urlString) {
            URLSession.shared.dataTask(with: url) { data, response, error in
                guard let data = data, error == nil else { return }
                DispatchQueue.main.async {
                    self.imageView.image = UIImage(data: data)
                }
            }.resume()
        }
    }
}
```

### Android/Kotlin with Glide
```kotlin
import com.bumptech.glide.Glide
import android.widget.ImageView

class PublicBuildingActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        
        val imageView: ImageView = findViewById(R.id.publicBuildingImage)
        val imageUrl = "https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/9b1fa2681a1a9644cf0b.jpg"
        
        Glide.with(this)
            .load(imageUrl)
            .placeholder(R.drawable.placeholder)
            .error(R.drawable.error)
            .into(imageView)
    }
}
```

### Python
```python
import requests
from PIL import Image
from io import BytesIO

# Download and display image
url = 'https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/9b1fa2681a1a9644cf0b.jpg'
response = requests.get(url)
img = Image.open(BytesIO(response.content))
img.show()
```

### Vue.js
```vue
<template>
  <div class="public-building-gallery">
    <img 
      v-for="(image, index) in images" 
      :key="index"
      :src="image"
      :alt="`Public Building ${index + 1}`"
      loading="lazy"
    />
  </div>
</template>

<script>
export default {
  data() {
    return {
      images: [
        'https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/9b1fa2681a1a9644cf0b.jpg',
        'https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/9cbf90c822baaee4f7ab.jpg',
      ]
    };
  }
};
</script>
```

---

## 📊 Summary

- **Category:** Công Trình Công Cộng (Public Buildings)
- **Total Images:** 11
- **Format:** JPG
- **Access:** Direct HTTP URLs via GitHub raw content

All URLs are direct links to raw image files hosted on GitHub and can be used in any application that supports HTTP image loading.

## 🌐 Folder Structure

Images are organized in the repository as:
```
ArchX/
├── Công Trình Công Cộng/
│   ├── 9b1fa2681a1a9644cf0b.jpg -> ../9b1fa2681a1a9644cf0b.jpg
│   ├── 9cbf90c822baaee4f7ab.jpg -> ../9cbf90c822baaee4f7ab.jpg
│   └── ... (11 total symlinks)
└── [original images in root]
```

---

## 📝 Notes

- These are symlinked images pointing to the original files in the repository root
- URLs remain stable and do not change unless images are renamed
- Suitable for production use in web and mobile applications
- No authentication required for public repository access
- CORS-enabled for cross-origin requests
