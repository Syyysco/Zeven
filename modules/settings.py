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
This module contains the value of the configuration variables of the "config/config.ini" file
'''
from .config_handler import get_value

SKIP_MISSARGS = get_value('Settings', 'skip_invalid_parameters')        # Enable/disable the errors or warnings related to missed parameters
OVERWRITEDIR_LOCK = get_value('Settings', 'directory_overwrite_lock')   # Enable/diable the dir overwrite protection 
DEBUG_MODE = get_value('Settings', 'debug_mode')                        # Enable/disable debugging to show debugID's and extra info
BETA_LANGS = get_value('Settings', 'beta_languages')                    # Enable/disable BETA langujes ( CAUTION! The comments here will be deleted )
VERBOSITY_LEVEL = get_value('Settings', 'verbosity_level')              # Sets the level of verbosity (amount of information represented) on the output
MAKE_PROJECT_BACKUPS = get_value('Settings', 'create_project_backups')  # Enables/disables the creation of backup copies of projects (whether files or folders)
MAX_BACKUPS = get_value('Settings', 'maximum_backups')                  # Maximum total backups to keep (when the maximum is reached, the oldest projects will be deleted first).
BACKUP_PATH = get_value('Settings', 'backup_folder')                    # Path that establishes the directory where backups will be saved.
USE_THREADS = get_value('Settings', 'use_threads')                      # Enables/disables the use of threads over directories.
MAX_THREADS = get_value('Settings', 'maximum_threads')                  # Specifies the number of threads to use (never exceed that number).
SHOW_PROGRESSBAR = get_value('Customize', 'shows_progress_bar')         # Show/hide the main progress bar
COLOR_HIGHLIGHTING = get_value('Customize', 'color_highlighting')       # Enable/disable the output colorization
SOUNDS = get_value('Customize', 'sounds')                               # Enable/disable all sounds
NOTIFICATION_AT_END = get_value('Customize', 'completion_notification') # Enable/disable notification sound at end
ENABLE_NOTIFY_AFTER = get_value('Customize', 'time_until_notification') # Notify when processes longer than (Number) seconds finish
ERROR_NOTIFICATION = get_value('Customize', 'error_notification')       # The sound of error-notifications (So far there are 4)
SUCCESS_NOTIFICATION = get_value('Customize', 'success_notification')   # The sound of success-notifications (So far there are 4)
HELP_ON_ARGERRORS = get_value('Customize', 'help_on_parameter_errors')  # Show/hide the help panel when there are errors in the parameters or arguments entered.
