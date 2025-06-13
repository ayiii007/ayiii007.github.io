import os

folder = "photos"
output_file = "photography.html"

files = sorted([f for f in os.listdir(folder) if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp", ".gif"))])

with open(output_file, "w", encoding="utf-8") as f:
    f.write('''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Photography</title>
<style>
body { font-family: Arial, sans-serif; margin: 0; padding: 0; background: #f9f9f9; }
h1 { text-align: center; padding: 20px; }
.gallery { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; padding: 20px; }
.gallery img { width: 100%; height: 250px; object-fit: cover; border-radius: 8px; cursor: pointer; transition: transform 0.3s; }
.gallery img:hover { transform: scale(1.05); }
.lightbox {
  position: fixed; top: 0; left: 0; width: 100%; height: 100%;
  background: rgba(0,0,0,0.9); display: none; align-items: center; justify-content: center;
  z-index: 1000; flex-direction: column;
}
.lightbox img {
  max-width: 90%; max-height: 80vh; border-radius: 10px;
  box-shadow: 0 0 20px rgba(0,0,0,0.5);
}
.lightbox .controls {
  margin-top: 10px; width: 100%; text-align: center;
}
.lightbox button {
  background: rgba(255,255,255,0.8);
  border: none; padding: 10px 20px; margin: 0 10px;
  font-size: 18px; cursor: pointer; border-radius: 5px;
  transition: background 0.3s;
}
.lightbox button:hover {
  background: #f0a500;
  color: white;
}
nav {
  position: fixed; top: 0; left: 0; right: 0;
  background: rgba(0,0,0,0.8); height: 50px;
  display: flex; align-items: center; padding: 0 20px; z-index: 1000;
}
nav a {
  color: white; margin-right: 25px; text-decoration: none; font-weight: bold;
  font-size: 1em; padding: 6px 10px; border-radius: 4px;
  transition: background-color 0.3s, color 0.3s;
}
nav a:hover, nav a:focus {
  background-color: #f0a500; color: black;
}
</style>
</head>
<body>

<nav>
  <a href="index.html">Home</a>
  <a href="#about">About</a>
  <a href="photography.html">Photography</a>
  <a href="blog.html">Blog</a>
  <a href="reports.html">Reports</a>
  <a href="#contact">Contact</a>
</nav>

<h1 style="margin-top:70px;">My Photography</h1>
<div class="gallery">
''')


    for file in files:
        f.write(f'<img src="photos/{file}" alt="{file}" data-index="{files.index(file)}" onclick="showLightbox({files.index(file)})">\n')

    f.write('''
</div>

<div class="lightbox" id="lightbox" onclick="hideLightbox(event)">
  <img id="lightbox-img" src="" alt="">
  <div class="controls">
    <button onclick="prevImage(event)">&#9664; Prev</button>
    <button onclick="nextImage(event)">Next &#9654;</button>
    <button onclick="hideLightbox(event)">Close &#10006;</button>
  </div>
</div>

<script>
const images = [
''')

    for file in files:
        f.write(f'"photos/{file}",\n')

    f.write('''];

let currentIndex = 0;

function showLightbox(index) {
  currentIndex = index;
  document.getElementById('lightbox-img').src = images[currentIndex];
  document.getElementById('lightbox').style.display = 'flex';
}

function hideLightbox(event) {
  if(event.target.id === 'lightbox' || event.target.tagName === 'BUTTON') {
    document.getElementById('lightbox').style.display = 'none';
  }
}

function prevImage(event) {
  event.stopPropagation();
  currentIndex = (currentIndex - 1 + images.length) % images.length;
  document.getElementById('lightbox-img').src = images[currentIndex];
}

function nextImage(event) {
  event.stopPropagation();
  currentIndex = (currentIndex + 1) % images.length;
  document.getElementById('lightbox-img').src = images[currentIndex];
}

// 键盘支持
document.addEventListener('keydown', function(event) {
  if(document.getElementById('lightbox').style.display === 'flex') {
    if(event.key === 'ArrowLeft') {
      prevImage(event);
    } else if(event.key === 'ArrowRight') {
      nextImage(event);
    } else if(event.key === 'Escape') {
      hideLightbox({target: document.getElementById('lightbox')});
    }
  }
});
</script>

</body>
</html>
''')

print("✅ photography.html with slider generated successfully!")

