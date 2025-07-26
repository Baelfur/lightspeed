# src/train/main.py

import argparse
import subprocess

def parse_args():
    parser = argparse.ArgumentParser(description="Train one or more models using config files")
    parser.add_argument("--inventory_config", type=str, default="config/inventory_full.json")
    parser.add_argument("--ipam_config", type=str, default="config/ipam_full.json")
    return parser.parse_args()

def main():
    args = parse_args()
    # Train inventory model
    subprocess.run([
        "python", "-m", "src.train.train_from_config", "--config", args.inventory_config
    ], check=True)
    # Train IPAM model
    subprocess.run([
        "python", "-m", "src.train.train_from_config", "--config", args.ipam_config
    ], check=True)

if __name__ == "__main__":
    main()