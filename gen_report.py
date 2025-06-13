import os

folder = "reports" 
output_file = "reports.html"

pdf_files = sorted([f for f in os.listdir(folder) if f.lower().endswith(".pdf")])

with open(output_file, "w", encoding="utf-8") as f:
    f.write('''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Reports</title>
<style>
  body { font-family: Arial, sans-serif; margin: 0; padding: 0; background: #fafafa; }
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
  h1 { margin-top: 70px; text-align: center; padding: 20px; }
  .pdf-list {
    max-width: 900px; margin: 20px auto; padding: 0 20px;
  }
  .pdf-item {
    background: white; margin-bottom: 15px; padding: 15px 20px;
    border-radius: 8px; box-shadow: 0 0 5px rgba(0,0,0,0.1);
    display: flex; align-items: center; justify-content: space-between;
    transition: background-color 0.3s;
  }
  .pdf-item:hover {
    background-color: #fff7e6;
  }
  .pdf-item a {
    text-decoration: none; color: #333; font-size: 1.1em;
    word-break: break-word;
  }
  .pdf-item a:hover {
    color: #f0a500;
  }
</style>
</head>
<body>

<nav>
  <a href="index.html">Home</a>
  <a href="photography.html">Photography</a>
  <a href="blog.html">Blog</a>
  <a href="reports.html">Reports</a>
  <a href="#contact">Contact</a>
</nav>

<h1>Reports</h1>
<div class="pdf-list">
''')

    for pdf in pdf_files:
        path = f"{folder}/{pdf}"
        f.write(f'<div class="pdf-item"><a href="{path}" target="_blank" rel="noopener">{pdf}</a></div>\n')

    f.write('''
</div>

</body>
</html>
''')

print("✅ reports.html generated successfully!")
