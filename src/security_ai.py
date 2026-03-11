import sys
import io

# This forces the terminal to handle emojis correctly
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import os
import re
from datetime import datetime

# The "Brains" of the scanner
PATTERNS = {
    "GitHub Token": r"ghp_[a-zA-Z0-9]{36}",
    "Private Key": r"-----BEGIN [A-Z ]+ PRIVATE KEY-----",
    "API Secret": r"(?i)secret[\s:=]+['\"]([a-zA-Z0-9]{8,})['\"]"
}

def generate_report():
    print("🛡️  AI Security Scanner: Building your Dashboard...")
    leaks = []
    files_scanned = 0
    
    # Patrol the folders
    for root, dirs, files in os.walk("."):
        if '.venv' in dirs: dirs.remove('.venv')
        if '.git' in dirs: dirs.remove('.git')
        
        for name in files:
            # Don't scan the scanner or the report!
            if name in ["security_ai.py", "security_report.html"]: continue
            
            files_scanned += 1
            path = os.path.join(root, name)
            try:
                with open(path, 'r', errors='ignore') as f:
                    content = f.read()
                    for label, pattern in PATTERNS.items():
                        if re.search(pattern, content):
                            leaks.append({"file": path, "type": label})
            except: continue

    # THE HTML DESIGN (This is where the box-shadow fix is)
    html_content = f"""
    <html>
    <head>
        <title>Security Report</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f0f2f5; padding: 40px; }}
            .container {{ max-width: 800px; margin: auto; background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }}
            h1 {{ color: #1a73e8; border-bottom: 2px solid #e8f0fe; padding-bottom: 10px; }}
            .stats {{ display: flex; gap: 20px; margin: 20px 0; }}
            .stat-box {{ background: #f8f9fa; padding: 15px; border-radius: 8px; flex: 1; text-align: center; border: 1px solid #eee; }}
            .danger {{ color: #d93025; font-weight: bold; font-size: 1.2em; }}
            .safe {{ color: #188038; font-weight: bold; font-size: 1.2em; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 25px; }}
            th {{ background-color: #f8f9fa; text-align: left; padding: 12px; border-bottom: 2px solid #dee2e6; }}
            td {{ padding: 12px; border-bottom: 1px solid #eee; font-family: monospace; color: #444; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🛡️ Security Audit Dashboard</h1>
            <p>Scan Date: {datetime.now().strftime('%B %d, %Y | %H:%M')}</p>
            
            <div class="stats">
                <div class="stat-box">Files Scanned: <br><strong>{files_scanned}</strong></div>
                <div class="stat-box">Status: <br>
                    {f'<span class="danger">🚨 {len(leaks)} Leaks</span>' if leaks else '<span class="safe">✅ Secure</span>'}
                </div>
            </div>

            <table>
                <thead>
                    <tr><th>Location</th><th>Issue Detected</th></tr>
                </thead>
                <tbody>
                    {''.join([f"<tr><td>{l['file']}</td><td>{l['type']}</td></tr>" for l in leaks]) if leaks else "<tr><td colspan='2' style='text-align:center;'>No leaks found! You're good to go.</td></tr>"}
                </tbody>
            </table>
        </div>
    </body>
    </html>
    """
    
    with open("security_report.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print("\n✅ DONE!")
    print(f"📄 Files Scanned: {files_scanned}")
    print(f"🚨 Leaks Found: {len(leaks)}")
    print("👉 Action: Open 'security_report.html' in your browser to see the dashboard.")

if __name__ == "__main__":
    generate_report()
