#  sb_frontend -- web frontend for stalkerbuster
#  Copyright (C) 2018  StalkerBuster
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""Flask app.
"""
import os
from flask import Flask

app = Flask(__name__)
app.root_ca_path = None


THEME_PATH = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "static"))


TEMPLATES_PATH = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "templates"))


@app.route('/')
def index():
    content = open(os.path.join(TEMPLATES_PATH, "index.tmpl"), "r").read()
    return content


@app.route('/sb-root.crt')
def sb_root_crt():
    return ""
