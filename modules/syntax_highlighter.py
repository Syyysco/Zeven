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

'''
This module is only responsible for returning any code with syntax highlighting in its only function `highlight_code`
'''
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import TerminalFormatter
from typing import Union

def highlight_code(code: str, syntax: str) -> Union[str , bool]:
    '''
    Returning any code with syntax highlighting
    '''
    try:
        lexer = get_lexer_by_name(syntax, stripall=True)
        formatter = TerminalFormatter()
        highlighted_code = highlight(code, lexer, formatter)
        
        return highlighted_code

    except Exception:
        return False