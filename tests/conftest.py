import os
import sys

import pytest

# Add project root and .agent/scripts to Python path
root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, root)
sys.path.insert(0, os.path.join(root, ".agent", "scripts"))


@pytest.fixture(scope="session")
def project_root():
    """Returns the absolute path to the project root."""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
