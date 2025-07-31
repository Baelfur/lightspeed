# scripts/reset_pipeline.py

import os
import shutil
import stat

# Directories to remove entirely
dirs_to_clean = [
    "data",
    "mlruns",
    "models",
    "reports",
    "__pycache__"
]

def handle_remove_readonly(func, path, _):
    """Clear the readonly bit and reattempt removal."""
    os.chmod(path, stat.S_IWRITE)
    func(path)

def remove_dir(path):
    """Remove a directory and its contents if it exists."""
    if os.path.exists(path):
        try:
            shutil.rmtree(path, onerror=handle_remove_readonly)
            print(f"🧹 Removed directory: {path}")
        except Exception as e:
            print(f"❌ Failed to remove {path}: {e}")
    else:
        print(f"⚠️ Directory not found: {path}")

if __name__ == "__main__":
    print("🔄 Cleaning up pipeline artifacts...")

    for dir_path in dirs_to_clean:
        remove_dir(dir_path)

    print("✅ Cleanup complete.")