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
This module contains the 'mimeTypes' class with the file types implemented\n
so far and their respective mime types.
"""
class mimeTypes:
    """
    - So far, this is the list of file types implemented in the application:\n
    ---
    ```
    html | css | javascript | json | python | typescript | php | sql
    ```
    """
    HTML = ('html', 'text/html', 'htm')
    CSS = ('css', 'text/css')
    JAVASCRIPT = ('js', 'mjs', 'application/javascript', 'javascript')
    JSON = ('json', 'jsonld', 'application/json', 'application/ld+json')
    TYPESCRIPT = ('ts', 'text/vnd.trolltech.linguist', 'typescript')
    PHP = ('php', 'application/x-httpd-php')
    #-----------------------------------    BETA      -----------------------
    PYTHON = ('py', 'pyz', 'pyc', 'pyo', 'pyw','text/x-python', 'python')
    SQL = ('sql', 'application/octet-stream', 'application/sql')
    

