import subprocess
import sys

def run_script(script_path):
    print(f"🚀 Running: {script_path}...")
    result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"✅ {script_path} finished successfully.")
        print(result.stdout)
    else:
        print(f"❌ Error in {script_path}:")
        print(result.stderr)
    return result.returncode

def main():
    print("--- 🛡️  Starting AI Project Suite ---")
    
    # 1. Security First! If there's a leak, we stop everything.
    if run_script("src/security_ai.py") != 0:
        print("🛑 STOP: Security issues detected. Fix them before continuing.")
        return

    # 2. Update the Pokedex
    run_script("src/pokedex.py")

    print("--- ✨ All Tasks Complete! Check your HTML files. ---")

if __name__ == "__main__":
    main()