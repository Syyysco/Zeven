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
This is the main module in charge of checking if there are any updates available
and updating Zeven from the official Github repository
'''
import requests

def update_zeven():
    # Testing 0001
    try:
        return 'COMPLETED', f'Zeven updated to v{new_version}'
    except Exception as e:
        return 'ERROR', f'There was an error updating the application: {str(e)}'



def check_update() -> str:
    try:
        have_conection = True if requests.get("https://google.com").status_code == 200 else False
        if not have_conection:
            return 'ERROR', 'It seems that you are not connected, please try again later'
        else:
            url = "https://raw.githubusercontent.com/Syyysco/Zeven/refs/heads/main/VERSION"
            response = requests.get(url)

            if response.status_code != 200:
                return 'ERROR', 'The update could not be verified. Please report the error at https://github.com/Syyysco/Zeven/issues'
            else:
                from .config_handler import get_json_value
                version = float(get_json_value(option='version'))
                new_version = float(response.text.strip())

                if version < new_version: 
                    update_response = update_zeven(new_version)
                    return update_response
                else:
                    return 'OK', 'Zeven is up to date with the latest version'

    except Exception as e:
        return 'ERROR', f'There was an error checking for the update {str(e)}'