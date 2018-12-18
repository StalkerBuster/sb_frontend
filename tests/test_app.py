# tests for app.py
import os
from sb_frontend.app import THEME_PATH, app


def test_theme_path_exists():
    assert os.path.exists(THEME_PATH)

def test_index():
    resp = app.test_client().get("/")
    assert resp.status == '200 OK'
