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

def init(input_file: str, indent: int=4) -> str:
    import cssbeautifier
    import re

    css_content = re.sub(r'\s+', ' ', input_file).strip()
    css_formated = cssbeautifier.beautify(css_content, {"indent_size": indent})
        
    return css_formated
    

