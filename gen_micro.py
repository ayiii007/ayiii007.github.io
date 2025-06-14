import os
from pathlib import Path

PROGRAMS_DIR = "programs"
OUTPUT_FILE = "micro.html"
NAV_FILE = "nav.html"

def generate_micro():
    programs = []
    
    for file in os.listdir(PROGRAMS_DIR):
        if file.endswith(".html"):
            name = os.path.splitext(file)[0]
            html_path = os.path.join(PROGRAMS_DIR, file)
            
            zip_file = None
            possible_zips = [f for f in os.listdir(PROGRAMS_DIR) 
                          if f.startswith(name.split('_')[0]) and f.endswith('.zip')]
            if possible_zips:
                zip_file = os.path.join(PROGRAMS_DIR, possible_zips[0])

            programs.append({
                "name": name.replace("_", " ").title(),
                "html": html_path,
                "zip": zip_file
            })

    try:
        with open(NAV_FILE, 'r') as f:
            nav_content = f.read()
    except FileNotFoundError:
        nav_content = '''<nav>
  <a href="index.html">Home</a>
  <a href="photography.html">Photography</a>
  <a href="blog.html">Blog</a>
  <a href="micro.html">Micro Programs</a>
  <a href="#contact">Contact</a>
</nav>'''

    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Micro Programs</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background: #f5f5f5;
        }}
        nav {{
            background: rgba(0,0,0,0.8);
            padding: 15px;
            position: sticky;
            top: 0;
            z-index: 100;
        }}
        nav a {{
            color: white;
            margin: 0 15px;
            text-decoration: none;
            font-weight: bold;
        }}
        .container {{
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
        }}
        h1 {{
            text-align: center;
            margin: 30px 0;
        }}
        .program-list {{
            list-style: none;
            padding: 0;
        }}
        .program-item {{
            background: white;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 15px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .program-name {{
            font-size: 1.1em;
            font-weight: bold;
        }}
        .program-links a {{
            display: inline-block;
            padding: 8px 16px;
            margin-left: 10px;
            border-radius: 4px;
            text-decoration: none;
            color: white;
        }}
        .open-link {{
            background: #4CAF50;
        }}
        .download-link {{
            background: #2196F3;
        }}
    </style>
</head>
<body>
    {nav_content}
    <div class="container">
        <h1>Micro Programs</h1>
        <ul class="program-list">
            {''.join([f'''
            <li class="program-item">
                <span class="program-name">{p['name']}</span>
                <div class="program-links">
                    <a href="{p['html']}" class="open-link">Open</a>
                    {f'<a href="{p["zip"]}" class="download-link" download>Download</a>' if p['zip'] else ''}
                </div>
            </li>
            ''' for p in programs])}
        </ul>
    </div>
</body>
</html>'''

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"Generated: {OUTPUT_FILE}")
    print(f"Found {len(programs)} programs")

if __name__ == "__main__":
    if not os.path.exists(PROGRAMS_DIR):
        os.makedirs(PROGRAMS_DIR)
        print(f"Created {PROGRAMS_DIR} folder")
    generate_micro()