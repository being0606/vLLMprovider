# src/config.py
import yaml

with open("config/settings.yaml", "r") as f:
    settings = yaml.safe_load(f)