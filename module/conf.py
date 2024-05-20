import os
from pathlib import Path

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ''))
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), ''))

def get_project_root() -> Path:
    return Path(ROOT_DIR)
