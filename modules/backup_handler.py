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
This module manages all the processes related to backups.
'''
import os
from datetime import datetime
from .system_operations import (remove_any, 
                                copy_any)
from .settings import BACKUP_PATH as INI_BACKUP_FOLDER

VERSION = '1.0'
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(CURRENT_DIR, '..', 'config', 'config.ini')
JSON_PATH = os.path.join(CURRENT_DIR, '..', 'config', 'config.json')
INITIAL_BACKUP_PATH = os.path.join(CURRENT_DIR, '..', 'backups')

BACKUP_PATH = INI_BACKUP_FOLDER if INI_BACKUP_FOLDER.strip() != '' and INI_BACKUP_FOLDER != None else INITIAL_BACKUP_PATH

CONFIG_INI_BACKUP =f'''[Settings]
skip_invalid_parameters = OFF
directory_overwrite_lock = ON
debug_mode = OFF
beta_languages = OFF
verbosity_level = 2
create_project_backups = ON
maximum_backups = 99
backup_folder = {os.path.abspath(INITIAL_BACKUP_PATH)}
use_threads = OFF
maximum_threads = 20

[Customize]
shows_progress_bar = ON
color_highlighting = ON
sounds = ON
completion_notification = ON
time_until_notification = 35
error_notification = 4
success_notification = 3
help_on_parameter_errors = ON'''

CONFIG_JSON_BACKUP = {
    'app_name': 'zeven',
    'version': f'{VERSION}',
    'config_hash': '',
}

def restore_initial_config_backup() -> None:
    '''
    Resets the config.ini file to its default state, and creates it if it does not exist.
    '''
    try:
        with open(os.path.abspath(CONFIG_PATH), "w") as config_file:
            config_file.write(CONFIG_INI_BACKUP)
        return 'OK'
    except Exception as e:
        return str(e)


def restore_initial_json_backup() -> None:
    '''
    Resets the config.json file to its default state, and creates it if it does not exist.
    '''
    try:
        import json
        with open(os.path.abspath(JSON_PATH), "w") as json_file:
            json.dump(CONFIG_JSON_BACKUP, json_file, indent=4)
        return 'OK'
    except Exception as e:
        return str(e)
        


def make_project_backup(input_project: str, make_backups: bool, maximum_backups: int) -> None:
    '''
    Create a new backup, and if there are more backups than allowed in the settings it will delete the oldest one
    '''
    if make_backups:
               
        num_of_backups = len([file for file in os.listdir(".")])
        output_file = os.path.join(BACKUP_PATH, f'{os.path.basename(input_project)}_{datetime.now().strftime("%d%m%Y-%H%M%S")}')
        
        if os.path.exists(os.path.join(BACKUP_PATH, "-- Backups go here --")): max_backups = maximum_backups + 1
        else: max_backups = maximum_backups
        if num_of_backups >= max_backups: remove_first_backup()
        
        copy_any(input=os.path.abspath(input_project), output=os.path.abspath(output_file))


def remove_first_backup() -> None:
    '''
    Delete the oldest backup
    '''
    proyects = [os.path.join(BACKUP_PATH, f) for f in os.listdir(BACKUP_PATH) if f != "-- Backups go here --"]
    if not proyects: return
    else: oldest_proyect = min(proyects, key=os.path.getmtime)
    
    remove_any(path=os.path.abspath(oldest_proyect))


def remove_all_backups() -> None:
    '''
    Delete all stored backups (files and folders)
    '''
    proyects = [os.path.join(BACKUP_PATH, f) for f in os.listdir(BACKUP_PATH) if f != "-- Backups go here --"]
    for proyect in proyects: remove_any(path=os.path.abspath(proyect))




