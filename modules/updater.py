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
import requests, os, shutil
from .config_handler import (ini_to_dict, 
                             set_value,
                             set_json_value)

def update_zeven(new_version: str, app_path: str):
    # Testing 0003
    old_versions_count = 1
    try:
        try:
            current_configuration_dict = ini_to_dict()
            new_path_name = os.path.abspath(os.path.join(app_path, '..', f'Zeven_old_version{old_versions_count}'))
            os.rename(app_path, new_path_name)
            os.system(f'git clone https://github.com/Syyysco/Zeven {app_path}')
            
            set_json_value(option='first_check', value=1, json_path=os.path.abspath(os.path.join(app_path, 'config', 'config.json')))
            # first_check
            
            try:
                for section_name, section in current_configuration_dict.items():
                    for key, value in section.items():
                        set_value(section=section_name, option=key, value=value, config_path=os.path.abspath(os.path.join(app_path, 'config', 'config.ini')))
            except Exception as e:
                return 'ERROR', str(e)
            
        except Exception as e:
            if os.path.exists(app_path):
                try: 
                    shutil.rmtree(app_path)
                except:
                    for i in range(1000):
                        if os.path.exists(os.path.abspath(os.path.join(app_path, '..', f'Zeven_update_error{old_versions_count}'))):
                            old_versions_count += 1
                            continue
                        else:
                            os.rename(app_path, os.path.abspath(os.path.join(app_path, '..', f'Zeven_update_error{old_versions_count}')))
            
            os.rename(new_path_name, app_path)
            return 'ERROR', f'There was an error updating the application: {str(e)}'
        
        if os.path.exists(new_path_name):
            try: shutil.rmtree(new_path_name)
            except Exception as e: 
                old_versions_count = 0
                for i in range (1000):
                    if os.path.exists(os.path.abspath(os.path.join(app_path, '..', f'Zeven_old_version{old_versions_count}'))):
                        old_versions_count += 1
                        continue
                    else:
                        os.rename(new_path_name, os.path.abspath(os.path.join(app_path, '..', 'Zeven_old_version')))
        
        return 'COMPLETED', f'Zeven updated to v{new_version}'
    except Exception as e:
        return 'ERROR', f'There was an error updating the application: {str(e)}'



def check_update(app_path: str) -> list:
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
                    update_response = update_zeven(new_version=str(new_version), app_path=app_path)
                    return update_response
                else:
                    return 'OK', 'Zeven is up to date with the latest version'

    except Exception as e:
        return 'ERROR', f'There was an error checking for the update {str(e)}'