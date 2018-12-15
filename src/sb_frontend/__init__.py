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
import os
from flask import Flask

app = Flask(__name__)

THEME_PATH = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "theme"))


@app.route('/')
def index():
    return "<h1>Hello World</h1>"


@app.route('/user/<name>')
def user(name):
    return "<h2>Hello %s!</h2>" % name


if __name__ == "__main__":
    app.run(debug=True)
