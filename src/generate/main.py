# src/generate/main.py

import argparse
import os
import sys
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.generate.generate_base_assets import generate_assets
from src.generate.inject_presence_noise import inject_noise

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)

def main():
    parser = argparse.ArgumentParser(description="Generate synthetic asset data.")
    parser.add_argument("--num_assets", type=int, default=11246)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--raw_dir", type=str, default="data/raw")
    parser.add_argument(
        "--config", type=str, default="config/generation_params.json",
        help="Path to probability config JSON"
    )
    args = parser.parse_args()

    os.makedirs(args.raw_dir, exist_ok=True)
    base_file = os.path.join(args.raw_dir, "base_asset_dataset.csv")
    labeled_file = os.path.join(args.raw_dir, "labeled_asset_dataset.csv")

    logging.info("🚀 Starting data generation pipeline...")
    generate_assets(args.num_assets, base_file)
    logging.info(f"CALLING inject_noise with config: {args.config}")
    inject_noise(base_file, labeled_file, args.seed, args.config)
    logging.info("🏁 Data generation pipeline completed.")

if __name__ == "__main__":
    main()