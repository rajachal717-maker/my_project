import subprocess
import sys
import io

# Fixes the Emoji/Unicode crash for Windows terminals
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def run_script(script_path):
    print(f"🚀 Running: {script_path}...")
    # We use 'python' to run the scripts inside our venv
    result = subprocess.run([sys.executable, script_path], capture_output=True, text=True, encoding='utf-8')
    
    if result.returncode == 0:
        print(f"✅ {script_path} finished successfully.")
        print(result.stdout)
        return 0
    else:
        print(f"❌ Error in {script_path}:")
        print(result.stderr)
        return 1

def main():
    print("\n--- 🛡️  Starting AI Project Suite ---")
    
    # 1. Run Security Scan
    if run_script("src/security_ai.py") != 0:
        print("🛑 STOP: Security issues or crashes detected. Fix them first.")
        return

    # 2. Run Pokedex Generator
    run_script("src/pokedex.py")

    print("--- ✨ All Tasks Complete! ---")

if __name__ == "__main__":
    main()