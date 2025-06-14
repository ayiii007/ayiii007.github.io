import os

folder = "reports"
output_file = "reports.html"
nav_file = "nav.html"

pdf_files = sorted([f for f in os.listdir(folder) if f.lower().endswith(".pdf")])

with open(nav_file, "r", encoding="utf-8") as nav_f:
    nav_content = nav_f.read()


with open(output_file, "w", encoding="utf-8") as f:
    f.write(f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Reports</title>
<style>
  body {{ 
    font-family: Arial, sans-serif; 
    margin: 0; 
    padding: 0; 
    background: #fafafa; 
    line-height: 1.6;
  }}
  nav {{
    position: fixed; 
    top: 0; 
    left: 0; 
    right: 0;
    background: rgba(0,0,0,0.8); 
    height: 50px;
    display: flex; 
    align-items: center; 
    padding: 0 20px; 
    z-index: 1000;
  }}
  nav a {{
    color: white; 
    margin-right: 25px; 
    text-decoration: none; 
    font-weight: bold;
    font-size: 1em; 
    padding: 6px 10px; 
    border-radius: 4px;
    transition: background-color 0.3s, color 0.3s;
    white-space: nowrap;
  }}
  nav a:hover, 
  nav a:focus {{
    background-color: #f0a500; 
    color: black;
  }}
  nav a.active {{
    background-color: #f0a500;
    color: black;
  }}
  h1 {{ 
    margin-top: 70px; 
    text-align: center; 
    padding: 20px; 
    color: #333;
  }}
  .container {{
    max-width: 900px; 
    margin: 20px auto; 
    padding: 20px;
  }}
  .pdf-list {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 15px;
    margin-top: 30px;
  }}
  .pdf-item {{
    background: white; 
    padding: 20px;
    border-radius: 8px; 
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    transition: transform 0.3s, box-shadow 0.3s;
    display: flex;
    flex-direction: column;
    height: 100%;
  }}
  .pdf-item:hover {{
    transform: translateY(-5px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
  }}
  .pdf-link {{
    text-decoration: none; 
    color: #0066cc;
    font-size: 1.1em;
    margin-bottom: 10px;
    word-break: break-word;
    flex-grow: 1;
  }}
  .pdf-link:hover {{
    color: #f0a500;
    text-decoration: underline;
  }}
  .pdf-meta {{
    color: #666;
    font-size: 0.9em;
    margin-top: 10px;
    display: flex;
    justify-content: space-between;
  }}
  .pdf-icon {{
    color: #e74c3c;
    margin-right: 5px;
  }}
  @media (max-width: 768px) {{
    .pdf-list {{
      grid-template-columns: 1fr;
    }}
    nav {{
      height: auto;
      flex-wrap: wrap;
      padding: 10px;
    }}
    nav a {{
      margin: 5px;
      font-size: 0.9em;
    }}
    h1 {{
      margin-top: 90px;
      font-size: 1.5em;
    }}
  }}
</style>
</head>
<body>

{nav_content}

<h1>Reports</h1>
<div class="container">
  <div class="pdf-list">
''')

    for pdf in pdf_files:
        file_path = f"{folder}/{pdf}"
        file_size = round(os.path.getsize(file_path) / (1024 * 1024), 2)  # 获取文件大小(MB)
        file_name = os.path.splitext(pdf)[0].replace('_', ' ').title()  # 格式化文件名
        f.write(f'''
    <div class="pdf-item">
      <a href="{file_path}" class="pdf-link" target="_blank" rel="noopener noreferrer">
        <span class="pdf-icon">📄</span> {file_name}
      </a>
      <div class="pdf-meta">
        <span>PDF Document</span>
        <span>{file_size} MB</span>
      </div>
    </div>
''')

    f.write('''
  </div>
</div>

<script>
// 设置当前活动导航项
document.addEventListener('DOMContentLoaded', function() {
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('nav a').forEach(link => {
    const linkPath = link.getAttribute('href').split('#')[0];
    if(linkPath === currentPage) {
      link.classList.add('active');
    }
  });
  
  // 平滑滚动到锚点
  document.querySelectorAll('nav a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      const targetId = this.getAttribute('href');
      if(targetId === '#') return;
      
      const targetElement = document.querySelector(targetId);
      if(targetElement) {
        window.scrollTo({
          top: targetElement.offsetTop - 60,
          behavior: 'smooth'
        });
      }
    });
  });
});
</script>

</body>
</html>
''')

print("✅ reports.html generated successfully with all fixes applied!")