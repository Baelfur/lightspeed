# src/prepare/generate_lightspeed_assets.py

import os
import pandas as pd
import argparse
from src.shared.constants import DEVICE_ROLE_CODES, REGION_SITE_MAP

def enrich_assets(raw_dir, processed_dir):
    INPUT_FILE = os.path.join(raw_dir, "labeled_asset_dataset.csv")
    OUTPUT_FILE = os.path.join(processed_dir, "labeled_asset_dataset_enriched.csv")
    os.makedirs(processed_dir, exist_ok=True)

    ROLE_CODE_TO_NAME = {v: k for k, v in DEVICE_ROLE_CODES.items()}
    SITE_TO_REGION = {
        site: region
        for region, sites in REGION_SITE_MAP.items()
        for site in sites
    }

    df = pd.read_csv(INPUT_FILE)
    df["site_code"] = df["hostname"].str[0:3]
    df["state_code"] = df["hostname"].str[3:5]
    df["role_code"] = df["hostname"].str[5:7]
    df["parsed_role"] = df["role_code"].map(ROLE_CODE_TO_NAME)
    df["parsed_region"] = df["site_code"].map(SITE_TO_REGION)
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"✅ Enriched dataset written to: {OUTPUT_FILE}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw_dir", type=str, default="data/raw", help="Path to the raw data directory")
    parser.add_argument("--processed_dir", type=str, default="data/processed", help="Path to the processed data directory")
    args = parser.parse_args()

    enrich_assets(args.raw_dir, args.processed_dir)