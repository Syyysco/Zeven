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

def init(input_file: str) -> str:
    import re
    typescript_formatted = re.sub(r'//(.*)', r'/*\1*/', input_file)          # Reemplazar comentarios de una línea por comentarios de varias líneas
    typescript_formatted = re.sub(r'\n\s*\n', '\n', typescript_formatted)    # Eliminar líneas en blanco
    typescript_formatted = re.sub(r'\s+', ' ', typescript_formatted).strip() # Compactar espacios en blanco
    typescript_formatted = re.sub(r'>\s+<', '><', typescript_formatted)      # Compactar espacio entre etiquetas HTML si están presentes

    return typescript_formatted