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
This module is responsible for reading, writing data from the user configuration file ("config/config.ini")
and manage configuration-related functions
'''
import configparser, os, json
from .system_operations import get_md5_hash
from typing import Union

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(CURRENT_DIR, '..', 'config', 'config.ini')
JSON_PATH = os.path.join(CURRENT_DIR, '..', 'config', 'config.json')


try:
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
except Exception:
    pass

def first_check() -> str:
    if get_json_value(option='first_check') == 0:
        from .backup_handler import restore_initial_config_backup
        restore_initial_config_backup()
        set_json_value(option='first_check', value=1)
        return True
    return False

def check_if_configuration_exists() -> str:
    '''
    Checks if the configuration (config.ini) file exists and if not, creates it again in the default path
    '''
    if not os.path.exists(CONFIG_PATH):
        from .backup_handler import restore_initial_config_backup
        try_restore = restore_initial_config_backup()
        if try_restore != 'OK': 
            try: set_json_value(option='config_hash', value=get_md5_hash(file_path=os.path.abspath(CONFIG_PATH)))
            except Exception: pass
            return 'ERROR', f'Error to restore initial config.ini backup: {try_restore}'
        
        else: return 'WARNING', 'The file "config.ini" was not found and a new one was created'
    else: return 'OK', None

def check_if_jsonconfig_exists() -> str:
    '''
    Checks if the configuration (config.json) file exists and if not, creates it again in the default path
    '''
    if not os.path.exists(JSON_PATH):
        from .backup_handler import restore_initial_json_backup
        try_restore = restore_initial_json_backup()
        if try_restore != 'OK': return 'ERROR', f'Error to restore initial config.json backup: {try_restore}'
        else: return 'WARNING', 'The file "config.json" was not found and a new one was created'
    else: return 'OK', None
        

def ini_to_dict() -> dict:
    """
    Reads a .ini file and converts it to a dictionary.

    Returns:
        dict (dict): Dictionary with the values from the .ini file.
    """
    ini_dict = {}
    for section in config.sections():
        ini_dict[section] = {
            key: True if value.upper() == 'ON' else False if value.upper() == 'OFF' else value
            for key, value in config.items(section)
        }
    return ini_dict

def last_hash_equal_to_last() -> str:
    """
    Checks the hash of the 'config.ini' file and compares it to the last hash saved in 'config.json'. If it is different, it performs a check of the 'config.ini' file.

    The purpose is to avoid having to check the integrity of the 'config.ini' file on each run.
    
    Returns:
        Hash-MD5 (str): A `config.ini` file hash
    """
    last_hash = get_json_value(option='config_hash')
    hash = get_md5_hash(file_path=os.path.abspath(CONFIG_PATH))
    
    if str(hash) != str(last_hash):
        return False
    return True

def check_configuration_integrity(dict: dict=ini_to_dict(), single_key: str=None) -> Union[str , bool]:
    """
    Checks if all configuration types match the values assigned to each one.

    Args:
        dict (dict): By default it will read a dictionary equivalent to the config.ini file

        single_key (str): Indicates that it does not want to check the integrity of a complete configuration file, but only that of a key.

    Returns:
        Any (str | bool): For full dictionaries it will return each and every error found in each configuration variable if something is wrong, otherwise nothing will return. In `single mode` it will simply return False or True depending on whether the key value is correct or not.
        

    ---
    ### Notes:
        Values (dictionaries or unique keys) must be converted to variable names in the config.ini file before adding them as an argument to this function.
    """
    keys_error_returns = ''
    
    LEVELS = {
        'verbosity_level': (0, 5),
        'maximum_backups': (1, 999),
        'maximum_threads': (2, 999),
        'time_until_notification': (0, 999),
        'error_notification': (1, len([file for file in os.listdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'notification_sounds', 'error')))])),
        'success_notification': (1, len([file for file in os.listdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'notification_sounds', 'success')))])),
    }
    
    PATHS = (
        'backup_folder',
             )
    
    BOOLEANS = (
        'skip_invalid_parameters',
        'directory_overwrite_lock',
        'debug_mode',
        'beta_languages',
        'create_project_backups',
        'use_threads',
        'shows_progress_bar',
        'color_highlighting',
        'sounds',
        'completion_notification',
        'help_on_parameter_errors'
    )
    
    if not single_key and not last_hash_equal_to_last():
        try:
            set_json_value(option='config_hash', value=get_md5_hash(file_path=os.path.abspath(CONFIG_PATH)))
            for section_name, section in dict.items():
                for key, value in section.items():
                    try:
                        if value is None or str(value).lstrip() == '':
                            keys_error_returns += f'\n\t {key}: does not contain any value'
                        elif key in LEVELS and (not isinstance(int(value), int) or not LEVELS[key][0] <= int(value) <= LEVELS[key][1]):
                                keys_error_returns += f'\n\t {key}: must contain a numeric value (int) between {LEVELS[key][0]} and {LEVELS[key][1]}, not "{value}"'
                        elif key in PATHS and not os.path.exists(os.path.abspath(value)):
                                keys_error_returns += f'\n\t {key}: The specified route does not exist in the system or could not be found'
                        elif key in BOOLEANS and not isinstance(value, bool):
                                keys_error_returns += f'\n\t {key}: The specified value "{value}" is not valid, it must be "ON" or "OFF"'
                    except Exception as e:
                        keys_error_returns += f'\n\t {key}: {str(e)}'
            if keys_error_returns:
                return f'The following errors were detected in the configuration file:{keys_error_returns}' 
        except Exception as e:
            return f'Errors detected in configuration: {str(e)}'
        
    elif single_key:
        try:
            for section_name, section in dict.items():
                for key, value in section.items():
                    if key == single_key:
                        if (
                            value is None or str(value).strip() == ''
                            or (single_key in LEVELS and (not isinstance(value, int) or not LEVELS[single_key][0] <= value <= LEVELS[single_key][1]))
                            or (single_key in PATHS and not os.path.exists(os.path.abspath(value)))
                            or (single_key in BOOLEANS and not isinstance(value, bool))
                        ):
                            return False
                        return True
            return True
        except Exception:
            return False


def get_value(section: str, option: str) -> Union[str , bool , int]:
    '''
    Returns the value of the given key (config.ini)
    '''
    value = config.get(section, option).strip()

    if value.upper() == 'ON': return True
    elif value.upper() == 'OFF': return False
    elif value.isdigit(): return int(value)

    return value                      


def set_value(section: str, option: str, value, config_path: str=None) -> None:
    '''
    Sets the value of the given key (config.ini)
    '''
    if config_path:
        file = config_path
        config.read(file)
    else:
        file = CONFIG_PATH
        
    if isinstance(value, bool): new_value = 'ON' if value else 'OFF'
    elif isinstance(value, int): new_value = str(value)
    else: new_value = str(value)

    config.set(section, option, new_value)
    with open(os.path.abspath(file), 'w') as configfile:
        config.write(configfile)
    
            
            
def get_json_value(option: str, option_list: tuple=None) -> Union[str , bool , int , list]:
    '''
    Get the value of the given key (config.json)
    '''
    with open(os.path.abspath(JSON_PATH), "r") as json_file:
        data = json.load(json_file)
    
    if not option_list:
        return data[option]  
    else:
        value_list = []
        for key in option_list:
            value_list.append(data[key])
        return value_list
    
    
def set_json_value(option: str, value, json_path: str=None) -> None:
    '''
    Sets the value of the given key (config.json)
    '''
    if json_path: file = json_path
    else: file = JSON_PATH
    
    with open(os.path.abspath(JSON_PATH), "r") as json_file:
        data = json.load(json_file)

    data[option] = value

    with open(os.path.abspath(JSON_PATH), "w") as file:
        json.dump(data, file, indent=4)
