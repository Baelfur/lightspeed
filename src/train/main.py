import argparse
import subprocess

def run_inventory(config):
    subprocess.run([
        "python", "-m", "src.train.train_from_config", "--config", config
    ], check=True)

def run_ipam(config):
    subprocess.run([
        "python", "-m", "src.train.train_from_config", "--config", config
    ], check=True)

def run_both(inventory_config, ipam_config):
    run_inventory(inventory_config)
    run_ipam(ipam_config)

def main():
    parser = argparse.ArgumentParser(description="Train inventory and/or IPAM models")
    subparsers = parser.add_subparsers(dest="command", required=True)

    inv_parser = subparsers.add_parser("inventory", help="Train inventory model")
    inv_parser.add_argument("--config", type=str, default="config/inventory_full.json")

    ipam_parser = subparsers.add_parser("ipam", help="Train ipam model")
    ipam_parser.add_argument("--config", type=str, default="config/ipam_full.json")

    both_parser = subparsers.add_parser("both", help="Train both models")
    both_parser.add_argument("--inventory_config", type=str, default="config/inventory_full.json")
    both_parser.add_argument("--ipam_config", type=str, default="config/ipam_full.json")

    args = parser.parse_args()

    if args.command == "inventory":
        run_inventory(args.config)
    elif args.command == "ipam":
        run_ipam(args.config)
    elif args.command == "both":
        run_both(args.inventory_config, args.ipam_config)
    else:
        raise ValueError("Invalid train command.")

if __name__ == "__main__":
    main()