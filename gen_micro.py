import os
from pathlib import Path

PROGRAMS_DIR = "programs"
OUTPUT_FILE = "micro.html"

def generate_index():
    programs = []
    
    # 扫描programs文件夹中的HTML文件
    for file in os.listdir(PROGRAMS_DIR):
        if file.endswith(".html"):
            name = os.path.splitext(file)[0]
            html_path = os.path.join(PROGRAMS_DIR, file)
            
            # 查找对应的ZIP文件
            zip_file = os.path.join(PROGRAMS_DIR, f"{name}.zip")
            if not os.path.exists(zip_file):
                # 如果没找到同名zip，尝试其他zip命名
                zip_file = None
                for f in os.listdir(PROGRAMS_DIR):
                    if f.startswith(name) and f.endswith('.zip'):
                        zip_file = os.path.join(PROGRAMS_DIR, f)
                        break
            
            programs.append({
                "name": name.replace("_", " ").title(),
                "html": html_path,
                "zip": zip_file
            })

    # 生成HTML内容
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Programs Index</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }}
        h1 {{
            color: #333;
            text-align: center;
            margin-bottom: 30px;
        }}
        .program-list {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
        }}
        .program-card {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}
        .program-title {{
            font-size: 1.2em;
            margin-bottom: 15px;
            color: #333;
        }}
        .program-link {{
            display: inline-block;
            padding: 8px 15px;
            background: #4CAF50;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            margin-right: 10px;
            margin-bottom: 10px;
        }}
        .download-link {{
            display: inline-block;
            padding: 8px 15px;
            background: #2196F3;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            margin-bottom: 10px;
        }}
    </style>
</head>
<body>
    <h1>Available Programs</h1>
    <div class="program-list">
        {"".join([f'''
        <div class="program-card">
            <h3 class="program-title">{p['name']}</h3>
            <a href="{p['html']}" class="program-link">Run Program</a>
            {f'<a href="{p["zip"]}" class="download-link" download>Download ZIP</a>' if p['zip'] else ''}
        </div>
        ''' for p in programs])}
    </div>
</body>
</html>
    """

    # 写入文件
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"✅ Generated: {OUTPUT_FILE}")
    print(f"Found {len(programs)} programs:")
    for p in programs:
        print(f"- {p['name']}")

if __name__ == "__main__":
    if not os.path.exists(PROGRAMS_DIR):
        os.makedirs(PROGRAMS_DIR)
        print(f"⚠️ Created '{PROGRAMS_DIR}' folder. Please add your HTML and ZIP files there.")
    else:
        generate_index()