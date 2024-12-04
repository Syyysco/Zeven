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
import requests, os, shutil, platform, subprocess
from .system_operations import get_terminal_columns
from alive_progress import alive_bar
from .config_handler import (ini_to_dict, 
                             set_value,
                             set_json_value)
from .settings import COLOR_HIGHLIGHTING
if COLOR_HIGHLIGHTING: from .colors import Colors
else: from .colors import NoColors as Colors

def count_requirements(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return lines

def count_items(dictionary):
    total = 0
    for value in dictionary.values():
        if isinstance(value, dict):
            total += count_items(value)
        else:
            total += 1 
    return total

def update_zeven(new_version: str, app_path: str):
    # Testing 0004
    old_versions_count = 1
    try:
        system = platform.system().lower()
        current_configuration_dict = ini_to_dict()
        new_path_name = os.path.abspath(os.path.join(app_path, '..', f'Zeven_old_version{old_versions_count}'))
        os.rename(app_path, new_path_name)
        
        subprocess.run(['git', 'clone', 'https://github.com/Syyysco/Zeven', app_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        requirements_txt = os.path.join(app_path, f"{'win-' if system == 'windows' else ''}requirements.txt")
        requirements_txt_items = count_requirements(requirements_txt)
        old_requirements_txt = os.path.join(new_path_name, f"{'win-' if system == 'windows' else ''}requirements.txt")
        old_requirements_txt_items = count_requirements(old_requirements_txt)
        conf_variable_count = count_items(current_configuration_dict)

        with alive_bar(5 + conf_variable_count + len(requirements_txt_items),
            title=f' {Colors.OKGREEN}UPDATING{Colors.END} ',
            bar='filling',
            spinner='waves2',
            spinner_length=3,
            length=get_terminal_columns() - 46,
            max_cols=get_terminal_columns(),
            disable=False,
            dual_line=True,
            elapsed=None,
            enrich_print=False,
            receipt=False) as bar:
        
            def update_bar(str: str = None):
                if str: print(f' {Colors.OKCYAN} • {Colors.END}{str}')
                bar()

            try:
                update_bar(str='Installing dependencies')
                for requirement in requirements_txt_items:
                    update_bar(str=f"{'Checking' if requirement in old_requirements_txt_items else 'Installing'} module: {requirement}")
                    subprocess.run(['python3', 'install', requirement, '--break-system-packages'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                
                update_bar(str=f'Setting user configurations')
                conf_count = 0
                set_json_value(option='first_check', value=0, json_path=os.path.abspath(os.path.join(app_path, 'config', 'config.json')))
                conf_count += 1; update_bar(str=f'Updating configuration ({conf_count}/{conf_variable_count + 1})')
                
                try:
                    for section_name, section in current_configuration_dict.items():
                        for key, value in section.items():
                            conf_count += 1
                            update_bar(str=f'Updating configuration ({conf_count}/{conf_variable_count + 1})')
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
                update_bar('Deleting old version')
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
    in_process = False
    print('\n')

    try:
        with alive_bar(title=f' {Colors.OKGREEN}SEARCH FOR UPDATES {Colors.END} ',
                bar=None,
                spinner='waves2',
                spinner_length=get_terminal_columns() - 46,
                max_cols=get_terminal_columns(),
                disable=False,
                elapsed=None,
                enrich_print=False,
                receipt=False,
                monitor=False) as bar:
            

            have_conection = True if requests.get("https://google.com").status_code == 200 else False; print(f' {Colors.OKCYAN} • {Colors.END}Checking connection')
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
                        print(f' {Colors.OKCYAN} • {Colors.END}New version available -> {new_version}')
                        in_process = True
                    else:
                        return 'OK', 'Zeven is up to date with the latest version'

    except Exception as e:
        return 'ERROR', f'There was an error checking for the update {str(e)}'

    if in_process:
        print(f' {Colors.OKCYAN} • {Colors.END}Downloading update from github')
        update_response = update_zeven(new_version=str(new_version), app_path=app_path)
        return update_response

        