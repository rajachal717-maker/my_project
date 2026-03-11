import os
import re

# This is the "Brain" of the AI: a list of patterns it looks for
SECURITY_PATTERNS = {
    "GitHub Token": r"ghp_[a-zA-Z0-9]{36}",
    "Generic API Key": r"(?i)(api_key|secret|password|token)[\s:=]+['\"]([a-zA-Z0-9]{8,})['\"]",
    "Private Key": r"-----BEGIN [A-Z]+ PRIVATE KEY-----" }

def scan_file(file_path):
    print(f"🔍 Scanning: {file_path}")
    findings = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
            for label, pattern in SECURITY_PATTERNS.items():
                if re.search(pattern, content):
                    findings.append(f"🚨 ALERT: Potential {label} found!")
                    
        return findings
    except Exception as e:
        return [f"❌ Error reading file: {e}"]

def run_security_scan():
    print("🛡️ --- GitHub Security AI Starter --- 🛡️")
    
    # We will scan your current project directory
    target_dir = "." 
    
    for root, dirs, files in os.walk(target_dir):
        # Ignore the .venv and .git folders (they are huge and safe)
        if '.venv' in dirs: dirs.remove('.venv')
        if '.git' in dirs: dirs.remove('.git')
        
        for name in files:
            # If the file is the scanner itself, skip it!
            if name == "security_ai.py":
                continue
                
            file_path = os.path.join(root, name)
            results = scan_file(file_path)
            
            if results:
                for r in results:
                    print(r)
            else:
                print(f"✅ {name} is clean.")

if __name__ == "__main__":
    run_security_scan()