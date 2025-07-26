# main.py

import argparse
import subprocess
import sys

def run_generate(args):
    cmd = [
        sys.executable,
        "src/generate/main.py",
        "--num_assets", str(args.num_assets),
        "--seed", str(args.seed),
        "--raw_dir", args.raw_dir
    ]
    subprocess.run(cmd, check=True)

def run_prepare(args):
    cmd = [
        sys.executable,
        "src/prepare/main.py",
        "--raw_dir", args.raw_dir,
        "--processed_dir", args.processed_dir
    ]
    subprocess.run(cmd, check=True)

def run_train(args):
    cmd = [
        sys.executable,
        "-m", "src.train.train_from_config",
        "--config", args.config
    ]
    subprocess.run(cmd, check=True)

def run_pipeline(args):
    # Generate
    generate_args = argparse.Namespace(
        num_assets=args.num_assets,
        seed=args.seed,
        raw_dir=args.raw_dir
    )
    run_generate(generate_args)
    # Prepare
    prepare_args = argparse.Namespace(
        raw_dir=args.raw_dir,
        processed_dir=args.processed_dir
    )
    run_prepare(prepare_args)
    # Train inventory
    train_inventory_args = argparse.Namespace(
        config=args.inventory_config
    )
    run_train(train_inventory_args)
    # Train ipam
    train_ipam_args = argparse.Namespace(
        config=args.ipam_config
    )
    run_train(train_ipam_args)

def main():
    parser = argparse.ArgumentParser(description="D502 Lightspeed ML Pipeline Orchestrator")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # generate
    generate_parser = subparsers.add_parser("generate", help="Run the generate step")
    generate_parser.add_argument("--num_assets", type=int, default=11246)
    generate_parser.add_argument("--seed", type=int, default=42)
    generate_parser.add_argument("--raw_dir", type=str, default="data/raw")

    # prepare
    prepare_parser = subparsers.add_parser("prepare", help="Run the prepare step")
    prepare_parser.add_argument("--raw_dir", type=str, default="data/raw")
    prepare_parser.add_argument("--processed_dir", type=str, default="data/processed")

    # train
    train_parser = subparsers.add_parser("train", help="Run the train step")
    train_parser.add_argument("--config", type=str, default="config/inventory_full.json")

    # pipeline
    pipeline_parser = subparsers.add_parser("pipeline", help="Run the full ML pipeline")
    pipeline_parser.add_argument("--num_assets", type=int, default=11246)
    pipeline_parser.add_argument("--seed", type=int, default=42)
    pipeline_parser.add_argument("--raw_dir", type=str, default="data/raw")
    pipeline_parser.add_argument("--processed_dir", type=str, default="data/processed")
    pipeline_parser.add_argument("--inventory_config", type=str, default="config/inventory_full.json")
    pipeline_parser.add_argument("--ipam_config", type=str, default="config/ipam_full.json")

    args = parser.parse_args()

    if args.command == "generate":
        run_generate(args)
    elif args.command == "prepare":
        run_prepare(args)
    elif args.command == "train":
        run_train(args)
    elif args.command == "pipeline":
        run_pipeline(args)
    else:
        raise ValueError(f"Unknown command: {args.command}")

if __name__ == "__main__":
    main()