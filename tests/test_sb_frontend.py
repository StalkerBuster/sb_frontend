# tests for sb_frontend
import os
from sb_frontend import THEME_PATH


def test_theme_path_exists():
    assert os.path.exists(THEME_PATH)
