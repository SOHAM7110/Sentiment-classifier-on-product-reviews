import os
import random

import numpy as np
import yaml


def set_seed(seed: int = 42) -> None:
    """Make runs reproducible across Python, NumPy, and PyTorch."""
    random.seed(seed)
    np.random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    try:
        import torch
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
    except ImportError:
        pass


def load_config(path: str = "configs/base.yaml") -> dict:
    with open(path, "r") as f:
        return yaml.safe_load(f)