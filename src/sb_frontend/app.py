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
import os, time
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, make_response, url_for, Response

app = Flask(__name__)
app.root_ca_path = None
app.secret_key = 'StalkerBuster'


THEME_PATH = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "static"))


TEMPLATES_PATH = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "templates"))


@app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    scan_running = session.get('scan_started')
    return render_template('index.tmpl')

@app.route('/about')
def about():
    return render_template('about.tmpl')

@app.route('/scan', methods=['POST', 'GET'])
def scan():
    if not session.get('logged_in'):
        return render_template('login.html')
    session['scan_started'] = True
    if "stop" in request.form.keys() or "results" in request.form.keys():
        session['scan_started'] = False
    return render_template('scan.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    username = request.form.get('username', None)
    password = request.form.get('password', None)
    if password == 'password' and username == 'admin':
        session['logged_in'] = True
        session['username'] = username
        flash('You were successfully logged in.')
        return redirect(url_for('index'))
    else:
        if 'username' in request.form:
            flash('WRONG PASSWORD. TRY AGAIN!')
    return render_template('login.html', error=None)

@app.route('/logout')
def logout():
    session['logged_in'] = False
    flash('You are now logged out.')
    return redirect(url_for('login'))


@app.route('/sb-root.crt')
def sb_root_crt():
    return ""

if __name__ =="__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0.', port=5000)
