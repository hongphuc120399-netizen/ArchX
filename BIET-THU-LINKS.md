# Biệt Thự (Villas) - Embeddable Image Links

This document contains embeddable HTTP URLs for all villa images in the ArchX collection.

## 🔗 Direct Usage

All images are hosted on GitHub and can be embedded directly into your applications using the raw GitHub URLs below.

## 📋 Base URL

```
https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/
```

---

## 🏰 Biệt Thự (Villas) - 11 Images

| # | Filename | Embeddable URL | Preview |
|---|----------|----------------|---------|
| 1 | 0777b59e06ec8ab2d3fd.jpg | `https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/0777b59e06ec8ab2d3fd.jpg` | ![](https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/0777b59e06ec8ab2d3fd.jpg) |
| 2 | 08df6bcbd7b95be702a8.jpg | `https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/08df6bcbd7b95be702a8.jpg` | ![](https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/08df6bcbd7b95be702a8.jpg) |
| 3 | 1225c120d95d55030c4c.jpg | `https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/1225c120d95d55030c4c.jpg` | ![](https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/1225c120d95d55030c4c.jpg) |
| 4 | 12d8ea644b16c7489e07.jpg | `https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/12d8ea644b16c7489e07.jpg` | ![](https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/12d8ea644b16c7489e07.jpg) |
| 5 | 152eb9530d21817fd830.jpg | `https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/152eb9530d21817fd830.jpg` | ![](https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/152eb9530d21817fd830.jpg) |
| 6 | 1976427df50f7951201e.jpg | `https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/1976427df50f7951201e.jpg` | ![](https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/1976427df50f7951201e.jpg) |
| 7 | 1d9cc2ac7fdef380aacf.jpg | `https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/1d9cc2ac7fdef380aacf.jpg` | ![](https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/1d9cc2ac7fdef380aacf.jpg) |
| 8 | 2332b9b507c78b99d2d6.jpg | `https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/2332b9b507c78b99d2d6.jpg` | ![](https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/2332b9b507c78b99d2d6.jpg) |
| 9 | 3a0c7d6ec81c44421d0d.jpg | `https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/3a0c7d6ec81c44421d0d.jpg` | ![](https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/3a0c7d6ec81c44421d0d.jpg) |
| 10 | 3f82ecb946cbca9593da.jpg | `https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/3f82ecb946cbca9593da.jpg` | ![](https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/3f82ecb946cbca9593da.jpg) |
| 11 | 483a43a5f7d77b8922c6.jpg | `https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/483a43a5f7d77b8922c6.jpg` | ![](https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/483a43a5f7d77b8922c6.jpg) |

---

## 💡 Usage Examples

### HTML
```html
<!-- Simple image tag -->
<img src="https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/0777b59e06ec8ab2d3fd.jpg" 
     alt="Villa Architecture" 
     width="800">

<!-- With responsive sizing -->
<img src="https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/0777b59e06ec8ab2d3fd.jpg" 
     alt="Luxury Villa" 
     style="max-width: 100%; height: auto;">

<!-- As background in div -->
<div style="background-image: url('https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/0777b59e06ec8ab2d3fd.jpg'); 
            background-size: cover; 
            height: 400px;">
</div>
```

### Markdown
```markdown
![Villa Architecture](https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/0777b59e06ec8ab2d3fd.jpg)

<!-- With size control -->
<img src="https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/0777b59e06ec8ab2d3fd.jpg" width="600">
```

### CSS
```css
/* As background image */
.hero-section {
    background-image: url('https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/0777b59e06ec8ab2d3fd.jpg');
    background-size: cover;
    background-position: center;
    height: 500px;
}

/* Multiple backgrounds */
.gallery {
    background-image: 
        url('https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/0777b59e06ec8ab2d3fd.jpg'),
        url('https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/08df6bcbd7b95be702a8.jpg');
}
```

### JavaScript (Vanilla)
```javascript
// Dynamic image loading
const img = document.createElement('img');
img.src = 'https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/0777b59e06ec8ab2d3fd.jpg';
img.alt = 'Villa';
document.body.appendChild(img);

// Fetch as blob
fetch('https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/0777b59e06ec8ab2d3fd.jpg')
    .then(res => res.blob())
    .then(blob => {
        const url = URL.createObjectURL(blob);
        document.getElementById('myImage').src = url;
    });

// Preload images
const villaImages = [
    'https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/0777b59e06ec8ab2d3fd.jpg',
    'https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/08df6bcbd7b95be702a8.jpg',
    // ... more images
];

villaImages.forEach(url => {
    const img = new Image();
    img.src = url;
});
```

### React
```jsx
import React from 'react';

// Simple component
function VillaImage() {
    const imageUrl = 'https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/0777b59e06ec8ab2d3fd.jpg';
    
    return (
        <img 
            src={imageUrl} 
            alt="Villa Architecture"
            style={{ maxWidth: '100%', height: 'auto' }}
        />
    );
}

// Gallery component
function VillaGallery() {
    const villaImages = [
        { id: 1, url: 'https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/0777b59e06ec8ab2d3fd.jpg' },
        { id: 2, url: 'https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/08df6bcbd7b95be702a8.jpg' },
        // ... more images
    ];
    
    return (
        <div className="gallery">
            {villaImages.map(img => (
                <img key={img.id} src={img.url} alt={`Villa ${img.id}`} />
            ))}
        </div>
    );
}

// With useState for dynamic loading
function DynamicVilla() {
    const [currentImage, setCurrentImage] = React.useState(
        'https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/0777b59e06ec8ab2d3fd.jpg'
    );
    
    return <img src={currentImage} alt="Villa" />;
}
```

### Vue.js
```vue
<template>
  <div class="villa-gallery">
    <img 
      v-for="(image, index) in villaImages" 
      :key="index"
      :src="image"
      :alt="`Villa ${index + 1}`"
      class="villa-image"
    />
  </div>
</template>

<script>
export default {
  data() {
    return {
      villaImages: [
        'https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/0777b59e06ec8ab2d3fd.jpg',
        'https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/08df6bcbd7b95be702a8.jpg',
        // ... more images
      ]
    }
  }
}
</script>

<style scoped>
.villa-image {
  max-width: 100%;
  height: auto;
  margin: 10px;
}
</style>
```

### Flutter (Dart)
```dart
import 'package:flutter/material.dart';

class VillaImage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Image.network(
      'https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/0777b59e06ec8ab2d3fd.jpg',
      loadingBuilder: (context, child, loadingProgress) {
        if (loadingProgress == null) return child;
        return Center(
          child: CircularProgressIndicator(
            value: loadingProgress.expectedTotalBytes != null
                ? loadingProgress.cumulativeBytesLoaded / 
                  loadingProgress.expectedTotalBytes!
                : null,
          ),
        );
      },
      errorBuilder: (context, error, stackTrace) {
        return Text('Failed to load image');
      },
    );
  }
}

// Gallery Widget
class VillaGallery extends StatelessWidget {
  final List<String> villaUrls = [
    'https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/0777b59e06ec8ab2d3fd.jpg',
    'https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/08df6bcbd7b95be702a8.jpg',
    // ... more images
  ];

  @override
  Widget build(BuildContext context) {
    return GridView.builder(
      gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
        crossAxisCount: 2,
        crossAxisSpacing: 10,
        mainAxisSpacing: 10,
      ),
      itemCount: villaUrls.length,
      itemBuilder: (context, index) {
        return Image.network(
          villaUrls[index],
          fit: BoxFit.cover,
        );
      },
    );
  }
}

// Cached Network Image (recommended)
import 'package:cached_network_image/cached_network_image.dart';

CachedNetworkImage(
  imageUrl: 'https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/0777b59e06ec8ab2d3fd.jpg',
  placeholder: (context, url) => CircularProgressIndicator(),
  errorWidget: (context, url, error) => Icon(Icons.error),
)
```

### Swift (iOS)
```swift
import UIKit

// Simple UIImageView
if let url = URL(string: "https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/0777b59e06ec8ab2d3fd.jpg") {
    let imageView = UIImageView()
    
    // Using URLSession
    URLSession.shared.dataTask(with: url) { data, response, error in
        guard let data = data, error == nil else { return }
        
        DispatchQueue.main.async {
            imageView.image = UIImage(data: data)
        }
    }.resume()
}

// Using SDWebImage (recommended)
import SDWebImage

let imageView = UIImageView()
if let url = URL(string: "https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/0777b59e06ec8ab2d3fd.jpg") {
    imageView.sd_setImage(with: url, placeholderImage: UIImage(named: "placeholder"))
}

// SwiftUI
import SwiftUI

struct VillaImageView: View {
    let imageUrl = "https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/0777b59e06ec8ab2d3fd.jpg"
    
    var body: some View {
        AsyncImage(url: URL(string: imageUrl)) { phase in
            switch phase {
            case .empty:
                ProgressView()
            case .success(let image):
                image
                    .resizable()
                    .aspectRatio(contentMode: .fit)
            case .failure:
                Image(systemName: "photo")
                    .foregroundColor(.gray)
            @unknown default:
                EmptyView()
            }
        }
    }
}
```

### Kotlin (Android)
```kotlin
import android.widget.ImageView
import com.bumptech.glide.Glide
import com.squareup.picasso.Picasso

// Using Glide (recommended)
val imageUrl = "https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/0777b59e06ec8ab2d3fd.jpg"
val imageView: ImageView = findViewById(R.id.imageView)

Glide.with(this)
    .load(imageUrl)
    .placeholder(R.drawable.placeholder)
    .error(R.drawable.error_image)
    .into(imageView)

// Using Picasso
Picasso.get()
    .load(imageUrl)
    .placeholder(R.drawable.placeholder)
    .error(R.drawable.error_image)
    .into(imageView)

// Using Coil (Kotlin-first)
import coil.load

imageView.load(imageUrl) {
    crossfade(true)
    placeholder(R.drawable.placeholder)
    error(R.drawable.error_image)
}

// Jetpack Compose
import androidx.compose.foundation.Image
import androidx.compose.runtime.Composable
import coil.compose.AsyncImage

@Composable
fun VillaImage() {
    AsyncImage(
        model = "https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/0777b59e06ec8ab2d3fd.jpg",
        contentDescription = "Villa Architecture"
    )
}
```

### Python
```python
# Using requests
import requests
from PIL import Image
from io import BytesIO

url = "https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/0777b59e06ec8ab2d3fd.jpg"
response = requests.get(url)
img = Image.open(BytesIO(response.content))
img.show()

# Download and save
response = requests.get(url)
with open('villa_image.jpg', 'wb') as f:
    f.write(response.content)

# Using urllib
from urllib.request import urlretrieve
urlretrieve(url, 'villa_image.jpg')
```

### PHP
```php
<?php
// Simple img tag
$imageUrl = 'https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/0777b59e06ec8ab2d3fd.jpg';
echo '<img src="' . $imageUrl . '" alt="Villa">';

// Download image
$imageData = file_get_contents($imageUrl);
file_put_contents('villa_image.jpg', $imageData);

// Using cURL
$ch = curl_init($imageUrl);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$imageData = curl_exec($ch);
curl_close($ch);
file_put_contents('villa_image.jpg', $imageData);
?>
```

### Node.js
```javascript
// Using axios
const axios = require('axios');
const fs = require('fs');

const imageUrl = 'https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/0777b59e06ec8ab2d3fd.jpg';

// Download image
axios({
    method: 'get',
    url: imageUrl,
    responseType: 'stream'
})
.then(response => {
    response.data.pipe(fs.createWriteStream('villa_image.jpg'));
})
.catch(error => console.error(error));

// Using fetch (Node 18+)
const response = await fetch(imageUrl);
const buffer = await response.arrayBuffer();
fs.writeFileSync('villa_image.jpg', Buffer.from(buffer));
```

---

## 📊 Summary

- **Total Villa Images:** 11
- **Format:** JPG
- **Hosted on:** GitHub Raw
- **Access:** Public, no authentication required
- **Usage:** Can be embedded in any application supporting HTTP image loading

## 🔒 Important Notes

1. **Rate Limiting:** GitHub has rate limits for raw file access. For production use, consider:
   - Caching images locally
   - Using a CDN
   - Implementing proper image optimization

2. **Performance:** 
   - Images are high-resolution
   - Consider using thumbnails or responsive images for better performance
   - Implement lazy loading for galleries

3. **CORS:** 
   - GitHub raw URLs support CORS
   - Safe to use in web applications

4. **Reliability:**
   - Images are hosted on GitHub's infrastructure
   - No expiration or deletion unless repository is modified
   - Consider backup strategy for mission-critical applications

---

## 🚀 Quick Copy Links

For quick access, here are all URLs in a simple list:

```
https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/0777b59e06ec8ab2d3fd.jpg
https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/08df6bcbd7b95be702a8.jpg
https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/1225c120d95d55030c4c.jpg
https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/12d8ea644b16c7489e07.jpg
https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/152eb9530d21817fd830.jpg
https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/1976427df50f7951201e.jpg
https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/1d9cc2ac7fdef380aacf.jpg
https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/2332b9b507c78b99d2d6.jpg
https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/3a0c7d6ec81c44421d0d.jpg
https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/3f82ecb946cbca9593da.jpg
https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/483a43a5f7d77b8922c6.jpg
```

## 📝 JSON Format

For programmatic access:

```json
{
  "category": "Biệt thự",
  "category_english": "Villas",
  "total_images": 11,
  "base_url": "https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/",
  "images": [
    {
      "id": 1,
      "filename": "0777b59e06ec8ab2d3fd.jpg",
      "url": "https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/0777b59e06ec8ab2d3fd.jpg"
    },
    {
      "id": 2,
      "filename": "08df6bcbd7b95be702a8.jpg",
      "url": "https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/08df6bcbd7b95be702a8.jpg"
    },
    {
      "id": 3,
      "filename": "1225c120d95d55030c4c.jpg",
      "url": "https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/1225c120d95d55030c4c.jpg"
    },
    {
      "id": 4,
      "filename": "12d8ea644b16c7489e07.jpg",
      "url": "https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/12d8ea644b16c7489e07.jpg"
    },
    {
      "id": 5,
      "filename": "152eb9530d21817fd830.jpg",
      "url": "https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/152eb9530d21817fd830.jpg"
    },
    {
      "id": 6,
      "filename": "1976427df50f7951201e.jpg",
      "url": "https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/1976427df50f7951201e.jpg"
    },
    {
      "id": 7,
      "filename": "1d9cc2ac7fdef380aacf.jpg",
      "url": "https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/1d9cc2ac7fdef380aacf.jpg"
    },
    {
      "id": 8,
      "filename": "2332b9b507c78b99d2d6.jpg",
      "url": "https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/2332b9b507c78b99d2d6.jpg"
    },
    {
      "id": 9,
      "filename": "3a0c7d6ec81c44421d0d.jpg",
      "url": "https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/3a0c7d6ec81c44421d0d.jpg"
    },
    {
      "id": 10,
      "filename": "3f82ecb946cbca9593da.jpg",
      "url": "https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/3f82ecb946cbca9593da.jpg"
    },
    {
      "id": 11,
      "filename": "483a43a5f7d77b8922c6.jpg",
      "url": "https://raw.githubusercontent.com/hongphuc120399-netizen/ArchX/main/483a43a5f7d77b8922c6.jpg"
    }
  ]
}
```

---

**Last Updated:** November 2025  
**Repository:** [hongphuc120399-netizen/ArchX](https://github.com/hongphuc120399-netizen/ArchX)
