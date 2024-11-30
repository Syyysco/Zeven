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
This module is intended to carry out operations related to the operating system.
'''
import platform, os, shutil, hashlib

def what_os() -> str:
    '''
    Returns the name of the operating system in lowercase
    '''
    return platform.system().lower()


def remove_any(path: str) -> None:
    '''
    Delete a file given a path
    '''
    if what_os() == 'windows':
        try:
            os.system(f'powershell -Command "Remove-Item -Path \'{path[3:]}\' -Recurse -Force"')
        except Exception:
            os.system(f'cmd /c "rd /S /Q {path} > NUL 2>&1"') if os.path.isdir(path) else os.system(f'cmd /c "del /F /Q {path} > NUL 2>&1"')
    else:
        os.system(f'rm -{"r" if os.path.isdir(path) else ""}f "{path}" &> /dev/null')
        
        
def copy_any(input: str, output: str) -> None:
    '''
    Copy a file or folder given a path
    '''
    if platform.system().lower() == 'windows': 
        if os.path.isdir(input): os.system(f'xcopy /E /I /Q /Y "{input}" "{output}"')
        else: os.system(f'cmd /c "copy /Y {input} {output} > NUL 2>&1"')
    else: os.system(f'[ -d "{output}" ] || cp -{"r" if os.path.isdir(input) else ""}f "{input}" "{output}"')
    

def get_terminal_columns() -> int:
    '''
    Returns the total columns of the current terminal
    '''
    columns, _ = shutil.get_terminal_size(fallback=(80, 20))
    return columns


def get_md5_hash(file_path) -> str:
    '''
    Returns the md5 hash of a file
    '''
    hasher = hashlib.md5()
    with open(file_path, "rb") as file:
        while chunk := file.read(8192):  # read in 8 KB blocks
            hasher.update(chunk)
    return str(hasher.hexdigest())