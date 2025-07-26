import os
import zipfile
from pathlib import Path

def parse_gitignore(gitignore_path=".gitignore"):
    ignore_paths = set()
    if not os.path.exists(gitignore_path):
        return ignore_paths

    with open(gitignore_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            ignore_paths.add(line.rstrip("/"))
    return ignore_paths

def zip_project(output_zip="d502_project.zip", root="."):
    ignore_paths = parse_gitignore()
    with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
        for foldername, subfolders, filenames in os.walk(root):
            rel_folder = os.path.relpath(foldername, root)
            if rel_folder == ".":
                rel_folder = ""
            if any(Path(rel_folder).match(p) for p in ignore_paths):
                continue

            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                rel_path = os.path.relpath(file_path, root)

                if any(Path(rel_path).match(p) for p in ignore_paths):
                    continue

                zipf.write(file_path, rel_path)
    print(f"✅ Project zipped to: {output_zip}")

if __name__ == "__main__":
    zip_project()