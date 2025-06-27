import os
import yaml
from dotenv import load_dotenv

load_dotenv()

def load_config(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def get_env_var(key, default=None):
    return os.environ.get(key, default)

# Example usage:
# api_config = load_config('config/api_keys.yaml')
# model_params = load_config('config/model_params.yaml')
