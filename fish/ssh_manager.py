#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path

def load_env():
    env_dict = {}
    env_path = '/home/kiyo/.config/fish/.env'
    
    with open(env_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=', 1)
                env_dict[key.strip()] = value.strip()
    return env_dict

def ssh_connect(host):
    try:
        subprocess.run(['ssh', host])
    except subprocess.CalledProcessError as e:
        print(f"Error connecting to {host}: {e}")
    except KeyboardInterrupt:
        print("\nConnection terminated by user")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 ssh_manager.py <connection_name>")
        sys.exit(1)

    connection_name = sys.argv[1].upper() + "_VPS_HOST"
    env_vars = load_env()

    if connection_name not in env_vars:
        print(f"Error: Connection '{sys.argv[1]}' not found in .env file")
        print("Available connections:")
        for key in env_vars:
            if key.endswith("_VPS_HOST"):
                print(f"  - {key.replace('_VPS_HOST', '').lower()}")
        sys.exit(1)

    host = env_vars[connection_name]
    ssh_connect(host)

if __name__ == "__main__":
    main()