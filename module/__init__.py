import os
import sys

from module.conf import ROOT_DIR

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '')))

__all__ = ["ROOT_DIR"]
