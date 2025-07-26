# src/prepare/main.py

import sys
import subprocess

if __name__ == "__main__":
    # Forward all CLI arguments to the module
    subprocess.run(
        [sys.executable, "-m", "src.prepare.generate_lightspeed_assets", *sys.argv[1:]],
        check=True
    )