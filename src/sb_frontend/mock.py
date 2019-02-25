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

"""
Components to simulate real-world hardware env.
"""
uplink_up = False
curr_wlan = None


def get_avail_wlans():
    return ["my honeypot", "WifiOnICE", "aiport1"]


def get_current_wlan():
    return curr_wlan


def select_wlan(ssid, password):
    global curr_wlan, uplink_up
    if ssid not in get_avail_wlans():
        return False
    if password != "123456":
        return False
    curr_wlan = ssid
    uplink_up = True
    return True


def unselect_wlan():
    global curr_wlan, uplink_up
    curr_wlan = None
    uplink_up = False
