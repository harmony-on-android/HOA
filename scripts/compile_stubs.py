import subprocess
import os
import glob
import sys

def find_es2abc():
    # 1. Check system path
    for path in os.environ.get("PATH", "").split(os.pathsep):
        exe = os.path.join(path, "es2abc.exe")
        if os.path.exists(exe):
            return exe
            
    # 2. Check standard DevEco Studio installation path
    dev_eco_studio_root = r"C:\Program Files\Huawei\DevEco Studio"
    if os.path.exists(dev_eco_studio_root):
        pattern = os.path.join(dev_eco_studio_root, "**", "es2abc.exe")
        matches = glob.glob(pattern, recursive=True)
        if matches:
            return matches[0]
            
    return None

def main():
    es2abc = find_es2abc()
    if not es2abc:
        print("ERROR: es2abc.exe could not be found. Please make sure DevEco Studio is installed or add it to PATH.")
        sys.exit(1)
        
    print(f"Found es2abc: {es2abc}")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(script_dir, "stubs")
    dest_dir = os.path.join(script_dir, "..", "app", "src", "main", "assets", "sys", "systemres", "abc")
    dest_dir = os.path.abspath(dest_dir)
    
    os.makedirs(dest_dir, exist_ok=True)
    
    js_files = glob.glob(os.path.join(src_dir, "*.js"))
    if not js_files:
        print(f"No .js files found in {src_dir}")
        return
        
    for js_file in js_files:
        basename = os.path.basename(js_file)
        name, _ = os.path.splitext(basename)
        abc_file = os.path.join(dest_dir, f"{name}.abc")
        
        print(f"Compiling {basename} -> {name}.abc...")
        cmd = [es2abc, js_file, "--module", "--output", abc_file]
        try:
            subprocess.run(cmd, check=True)
            print(f"  Successfully compiled {name}.abc")
        except Exception as e:
            print(f"  ERROR compiling {name}.abc: {e}")

if __name__ == "__main__":
    main()
