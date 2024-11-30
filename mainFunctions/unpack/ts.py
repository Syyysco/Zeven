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

def init(input_file: str, indent: int=2) -> str:
    import os, subprocess
    test_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    
    command = [
        f'deno{".exe" if not test_path.startswith("/") else ""}', 
        "fmt",
        "--options-indent-width",
        str(indent),
        "-"
    ]

    process = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    typescript_formatted, error = process.communicate(input=input_file)

    if process.returncode != 0:
        raise RuntimeError(f"Error al formatear el código: {error.strip()}")
    
    return typescript_formatted