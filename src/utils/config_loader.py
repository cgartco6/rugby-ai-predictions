# src/utils/config_loader.py
import os
import yaml
from dotenv import load_dotenv
from pathlib import Path

# Handle path resolution for config files
def resolve_config_path(file_path):
    base_dir = Path(__file__).resolve().parent.parent
    return base_dir / 'config' / file_path

load_dotenv()

def load_config(file_name):
    """Load YAML configuration file"""
    config_path = resolve_config_path(file_name)
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def get_env_var(key, default=None):
    return os.environ.get(key, default)
