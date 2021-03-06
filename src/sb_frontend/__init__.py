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
from sb_frontend.app import app, get_args
import os


def main():
    args = get_args()
    app.secret_key = os.urandom(12)
    app.run(debug=True, host=args.host, port=args.port)
