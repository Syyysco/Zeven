# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""
This module simply contains custom colors for help, errors and warnings.
- You can customize them if you want.

**Note:**\n
Some colors are not being used, they were simply added for future use\n 
and user customization.\n
"""
class Colors:
    """
    The color settings are detailed in this module,\n
    but will be placed here for accessibility:\n
    ---
    `FILE`: Underline\n
    `ARG`: Magenta\n 
    `GRAY`: Gray\n
    `GRAYBG`: Gray Background\n 
    `BLACK`: Black\n
    `POINT`: Blue\n 
    `OKCYAN`: Cyan\n 
    `OKGREEN`: Green\n 
    `WARNING`: Yellow\n 
    `FAIL`: Red\n 
    `END`: End color\n
    """
    FILE = '\033[4m'      # Underline
    ARG = '\033[95m'      # Magenta
    BGRAY = '\033[100m'   # Gray BG 
    GRAY = '\033[90m'     # Gray
    BLACK = '\033[30m'    # Black
    POINT = '\033[94m'    # Blue
    OKCYAN = '\033[96m'   # Cyan
    OKGREEN = '\033[92m'  # Green
    WARNING = '\033[93m'  # Yellow
    FAIL = '\033[91m'     # Red
    END = '\033[0m'       # End Color
    
class NoColors:
    """
    This class is used only in case the `COLOR_HIGHLIGHTING` setting is disabled.
    """
    FILE = '\033[4m'      # Underline
    ARG = '\033[0m'       # None
    BGRAY = '\033[0m'     # None
    GRAY = '\033[0m'      # None
    BLACK = '\033[0m'     # None
    POINT = '\033[0m'     # None
    OKCYAN = '\033[0m'    # None
    OKGREEN = '\033[0m'   # None
    WARNING = '\033[0m'   # None
    FAIL = '\033[0m'      # None
    END = '\033[0m'       # None