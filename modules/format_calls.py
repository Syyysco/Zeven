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
This module contains the names of the modules that will be called depending on the extensions and mimetypes allowed so far.\n
'''
from .mimetypes import mimeTypes
FORMAT_LIST = (mimeTypes.HTML[0],           #CONTROL: Allowed formats will be called after on ext_functions list
               mimeTypes.HTML[1],
               mimeTypes.HTML[2],
               mimeTypes.CSS[0],
               mimeTypes.CSS[1],
               mimeTypes.JAVASCRIPT[0],
               mimeTypes.JAVASCRIPT[1],
               mimeTypes.JAVASCRIPT[2],
               mimeTypes.JAVASCRIPT[3],
               mimeTypes.JSON[0],
               mimeTypes.JSON[1],
               mimeTypes.JSON[2],
               mimeTypes.JSON[3],
               mimeTypes.TYPESCRIPT[0],
               mimeTypes.TYPESCRIPT[1],
               mimeTypes.TYPESCRIPT[2],
               mimeTypes.PHP[0],
               mimeTypes.PHP[1],
               mimeTypes.PYTHON[0],
               mimeTypes.PYTHON[1],
               mimeTypes.PYTHON[2],
               mimeTypes.PYTHON[3],
               mimeTypes.PYTHON[4],
               mimeTypes.PYTHON[5],
               mimeTypes.PYTHON[6],
               mimeTypes.SQL[0],
               mimeTypes.SQL[1],
               mimeTypes.SQL[2],
               )

BETA_LIST = (                             # List of languages ​​in development to prevent possible errors in formatting and compaction
    mimeTypes.PYTHON[0],
    mimeTypes.PYTHON[1],
    mimeTypes.PYTHON[2],
    mimeTypes.PYTHON[3],
    mimeTypes.PYTHON[4],
    mimeTypes.PYTHON[5],
    mimeTypes.PYTHON[6],
    mimeTypes.SQL[0],
    mimeTypes.SQL[1],
    mimeTypes.SQL[2],
)

EXT_FUNCTIONS = {                                              # Name of module to call + ".html"      (for example)
        mimeTypes.HTML[0]: mimeTypes.HTML[0],                  # depending on the input/detect file format.
        mimeTypes.HTML[1]: mimeTypes.HTML[0],
        mimeTypes.HTML[2]: mimeTypes.HTML[0],
        mimeTypes.CSS[0]: mimeTypes.CSS[0],
        mimeTypes.CSS[1]: mimeTypes.CSS[0],
        mimeTypes.JAVASCRIPT[0]: mimeTypes.JAVASCRIPT[0],
        mimeTypes.JAVASCRIPT[1]: mimeTypes.JAVASCRIPT[0],
        mimeTypes.JAVASCRIPT[2]: mimeTypes.JAVASCRIPT[0],
        mimeTypes.JAVASCRIPT[3]: mimeTypes.JAVASCRIPT[0],
        mimeTypes.JSON[0]: mimeTypes.JSON[0],
        mimeTypes.JSON[1]: mimeTypes.JSON[0],
        mimeTypes.JSON[2]: mimeTypes.JSON[0],
        mimeTypes.JSON[3]: mimeTypes.JSON[0],
        mimeTypes.TYPESCRIPT[0]: mimeTypes.TYPESCRIPT[0],
        mimeTypes.TYPESCRIPT[1]: mimeTypes.TYPESCRIPT[0],
        mimeTypes.TYPESCRIPT[2]: mimeTypes.TYPESCRIPT[0],
        mimeTypes.PHP[0]: mimeTypes.PHP[0],
        mimeTypes.PHP[1]: mimeTypes.PHP[0],
        mimeTypes.PYTHON[0]: mimeTypes.PYTHON[0],
        mimeTypes.PYTHON[1]: mimeTypes.PYTHON[0],
        mimeTypes.PYTHON[2]: mimeTypes.PYTHON[0],
        mimeTypes.PYTHON[3]: mimeTypes.PYTHON[0],
        mimeTypes.PYTHON[4]: mimeTypes.PYTHON[0],
        mimeTypes.PYTHON[5]: mimeTypes.PYTHON[0],
        mimeTypes.PYTHON[6]: mimeTypes.PYTHON[0],
        mimeTypes.SQL[0]: mimeTypes.SQL[0],
        mimeTypes.SQL[1]: mimeTypes.SQL[0],
        mimeTypes.SQL[2]: mimeTypes.SQL[0],
    }

ALLOW_INDENT = (mimeTypes.HTML[0],
                mimeTypes.PHP[0],
                mimeTypes.CSS[0],
                mimeTypes.JAVASCRIPT[0],
                mimeTypes.JSON[0],
                mimeTypes.TYPESCRIPT[0],)