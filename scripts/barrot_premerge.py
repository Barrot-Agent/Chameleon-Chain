#!/usr/bin/env python3

import os
import yaml
import pathlib

CONFIG_PATH = ".barrot.yml"
MAX_FILENAME_LENGTH = 255

def load_config():
    if not os.path.exists(CONFIG_PATH):
            print("No .barrot.yml found. Skipping.")
                    return {}
                        with open(CONFIG_PATH, "r") as f:
                                return yaml.safe_load(f).get("permissions", {})

                                def sanitize_filenames(config):
                                    if not config.get("sanitize_filenames", {}).get("enabled", False):
                                            return
                                                max_len = config["sanitize_filenames"].get("max_length", 128)
                                                    strategy = config["sanitize_filenames"].get("strategy", "truncate_pr")

                                                        for root, _, files in os.walk("."):
                                                                for name in files:
                                                                            full_path = os.path.join(root, name)
                                                                                        if len(name) > max_len:
                                                                                                        new_name = name[:max_len]
                                                                                                                        new_path = os.path.join(root, new_name)
                                                                                                                                        print(f"Renaming: {full_path} → {new_path}")
                                                                                                                                                        pathlib.Path(full_path).rename(new_path)

                                                                                                                                                        def resolve_conflicts(config):
                                                                                                                                                            if not config.get("resolve_merge_conflicts", False):
                                                                                                                                                                    return
                                                                                                                                                                        print("Barrot is authorized to resolve merge conflicts — but this script does not auto-resolve yet.")

                                                                                                                                                                        def arbitrate_motifs(config):
                                                                                                                                                                            if not config.get("motif_arbitration", {}).get("enabled", False):
                                                                                                                                                                                    return
                                                                                                                                                                                        precedence = config["motif_arbitration"].get("precedence", [])
                                                                                                                                                                                            print(f"Motif arbitration enabled. Precedence: {precedence}")

                                                                                                                                                                                            def main():
                                                                                                                                                                                                config = load_config()
                                                                                                                                                                                                    sanitize_filenames(config)
                                                                                                                                                                                                        resolve_conflicts(config)
                                                                                                                                                                                                            arbitrate_motifs(config)

                                                                                                                                                                                                            if __name__ == "__main__":
                                                                                                                                                                                                                main()