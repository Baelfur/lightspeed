# src/prepare/main.py

import subprocess

if __name__ == "__main__":
    subprocess.run(["python", "-m", "src.prepare.generate_lightspeed_assets"], check=True)