#  sb_frontend -- web frontend for stalkerbuster
#  Copyright (C) 2019  StalkerBuster
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
import argparse
from flask import (
    Flask, flash, redirect, render_template, request, session, abort,
    make_response, url_for, Response)
from sb_frontend.mock import (
    get_current_wlan, get_avail_wlans, select_wlan, unselect_wlan)

#Argument Parser for setting port and host
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', help='the port StalkerBuster binds to', default=5000, type=int)
    parser.add_argument('--host', help='the host StalkerBuster is running', default='localhost')
    args = parser.parse_args()
    return args


app = Flask(__name__)
app.root_ca_path = None


THEME_PATH = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "static"))


TEMPLATES_PATH = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "templates"))


@app.route('/', methods=['POST', 'GET'])
def index():
    # handle_settings(request)
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('index.tmpl')

@app.route('/about', methods=['POST', 'GET'])
def about():
    return render_template('about.tmpl')

@app.route('/settings', methods=['POST', 'GET'])
def settings():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('settings.tmpl')

@app.route('/scan', methods=['POST', 'GET'])
def scan():
    if not session.get('logged_in'):
        return render_template('login.html')
    session['scan_started'] = True
    if "stop" in request.form.keys() or "results" in request.form.keys():
        session['scan_started'] = False
    return render_template('scan.html')


@app.route('/results', methods=['POST', 'GET'])
def results():
    if not session.get('logged_in'):
        return render_template('login.html')
    session['scan_started'] = True
    if "stop" in request.form.keys() or "results" in request.form.keys():
        session['scan_started'] = False
    return render_template('results.html')


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
    session['scan_started'] = False
    flash('You are now logged out.')
    return redirect(url_for('login'))


@app.route('/sb-root.crt')
def sb_root_crt():
    return ""


@app.context_processor
def template_vars():
    handle_settings()
    return dict(
        ssid=get_current_wlan(),
        avail_wlans=get_avail_wlans(),
    )


def handle_settings():
    if "submit-settings-wlan" in request.form:
        select_wlan(
            request.form.get('ssid'),
            request.form.get('ssid_password'))
    if "submit-settings-wlan-disconnect" in request.form:
        unselect_wlan()
