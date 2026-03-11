import os
import re

# 1. THE BRAIN: These are the "shapes" of secrets the AI hunts for
# We use 'r' before the quotes to tell Python this is a "Pattern" (Regex)
PATTERNS = {
    "GitHub Token": r"ghp_[a-zA-Z0-9]{36}",
    "Generic Secret": r"(?i)(api_key|secret|password|token)[\s:=]+['\"]([a-zA-Z0-9]{8,})['\"]",
    "Private Key": r"-----BEGIN RSA PRIVATE KEY-----"
}

def start_scan():
    print("🛡️  AI Security Scanner is patrolling your files...")
    print("-----------------------------------------------")
    
    leaks_found = 0
    
    # 2. THE PATROL: This walks through every folder in your project
    for root, dirs, files in os.walk("."):
        
        # Don't look in these folders (they are safe or too big)
        if '.venv' in dirs: dirs.remove('.venv')
        if '.git' in dirs: dirs.remove('.git')
        
        for file_name in files:
            # Skip the scanner file itself
            if file_name == "security_ai.py":
                continue
                
            file_path = os.path.join(root, file_name)
            
            try:
                with open(file_path, 'r', errors='ignore') as f:
                    content = f.read()
                    
                    # 3. THE INSPECTION: Check every file for our "Wanted" patterns
                    for label, pattern in PATTERNS.items():
                        if re.search(pattern, content):
                            print(f"🚨 ALERT: {label} found in {file_path}!")
                            leaks_found += 1
            except Exception as e:
                print(f"⚠️ Could not read {file_path}: {e}")

    # 4. THE FINAL REPORT
    print("-----------------------------------------------")
    if leaks_found > 0:
        print(f"❌ SCAN FINISHED: Found {leaks_found} security leaks!")
        print("Action Required: Delete these secrets before pushing to GitHub!")
    else:
        print("✅ SCAN FINISHED: No secrets found. Your code is clean!")

if __name__ == "__main__":
    start_scan()