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
class SB_Mock(object):
    uplink_up = False
    
    def get_avail_wlans(self):
        return ["my honeypot", "WifiOnICE", "aiport1"]

    def select_wlan(self, ssid, password):
        if not ssid in self.get_avail_wlans():
            return False
        if password != "123456":
            return False
        self.wlan = ssid
        self.uplink_up = True
        return True        
    
    def unselect_wlan(self):
        self.wlan = None
        self.uplink_up = False

    
