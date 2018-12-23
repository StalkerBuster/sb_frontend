# tests for app.py
import os
from sb_frontend.app import THEME_PATH, app


def test_theme_path_exists():
    assert os.path.exists(THEME_PATH)


def test_static_content_available():
    # we can get content on the `/static` path
    resp = app.test_client().get("/static/index.html")
    assert resp.status == "200 OK"


def test_app_root_reachable():
    # ensure, the root of our web app can be reached
    resp = app.test_client().get("/")
    assert resp.status == '200 OK'
