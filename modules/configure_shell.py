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

"""
This module contains the executable for the interactive configuration mode.
"""

import curses, os
from typing import Union
from copy import deepcopy
from .settings import *
from .backup_handler import BACKUP_PATH as DEFAULT_BACKUP_PATH
from .config_handler import (set_value, 
                             check_configuration_integrity)
from .play_sounds import play


def generate_dynamic_helps() -> tuple:
    bottom_help_configuration_text = (
"""Some arguments may sometimes be introduced unnecessarily, added
incorrectly (perhaps unintentionally), or be incompatible in certain cases.
This setting allows certain errors related to the aforementioned issues to
be ignored, enabling the execution to continue without triggering errors.""",

"""By default, directories are not overwritten unless the -D parameter is used
to execute in directory mode or the same input and output paths are specified
with the -o parameter (e.g., sevven -i folder1 -o folder1).
Disabling directory overwrite protection will cause directories to be
overwritten simply by providing an input (e.g., sevven -i folder1).""",

"""Debug mode provides more detailed information during execution and upon completion.
This is especially useful for developers who want to contribute to the tool, as it
makes it much easier to understand its behavior with greater precision.""",

"""Some languages are not enabled by default because their behavior is not yet fully
controlled and they are still under development.
Enabling this setting will treat these experimental languages the same as others.
It’s important to verify the results after making changes.""",

"""You can adjust the level of information displayed on the screen from multiple levels:

0: Nothing will be displayed, not even errors.                                
1: Only errors will be displayed.                                             
2: Displays the current progress and the size difference upon completion.     
3: Shows updated files during execution.                                      
4: Shows files that were not updated during execution and warnings.           
5: Highlights errors and warnings for easier identification in large projects.""",

f"""When enabled, a backup will be created every time the tool is run on a project
(file or directory), allowing you to recover data in case of loss or other issues.
The backup directory is located at default path, but you can change this.

Default Path: {os.path.abspath(DEFAULT_BACKUP_PATH)}""",

"""You can set the maximum number of backups to be stored in the designated path
before older backups start being deleted. However, you can manually delete 
all backups using the --flush-backups parameter.""",

f"""By default, backups are stored in the default path, but you can change this 
to a custom folder on your device. If the folder becomes inaccessible at any point,
the default path will be restored automatically.

Current Path: {current_configuration['Backup Folder']}""",

"""This setting only affects directories.

Sometimes some projects are extremely large and contain a lot of files, in which
case it is advisable to enable the use of threads so that the execution takes as
little time as possible. On small projects it is not necessary to use threads, 
since the difference will be milliseconds.""",

"""You can specify the number of threads to use.

This defines a maximum number of threads that can be in parallel at the same time
and will never be exceeded. Consider using the most appropriate number for your
computer, considering the resources available."""
    )

    bottom_help_customization_text = (
"""Displays the current progress along with an animated bar at the bottom of the
screen, indicating that the tool is running.""",

"""Displays all output in a colorized format, including within the configuration
menu, help panels, updated files, progress bar, errors, and warnings.
This is useful for making the output much easier to read.""",

"""Enables or disables all application sounds, including for the configuration
menu and notifications. If this setting is turned off, all 
notification-related settings will also be disabled.""",

"""When tasks are completed, a sound will play by default to notify you that
the process has finished. This is useful for large projects that might take
longer than expected.""",

"""For very small projects or single files, processing time is usually brief,
making notifications unnecessary. Set the minimum execution time (in seconds)
after which you wish to be notified. Processes shorter than this time will
not trigger notifications.""",

"""Customize the notification sound for errors.""",

"""Customize the notification sound for successful processes.""",

"""Decide whether to display the help panel alongside the current error when
incorrect parameter or argument usage is detected. If disabled, only the 
error itself will be displayed.""",
    )
    
    return bottom_help_configuration_text, bottom_help_customization_text


shell = ''                                              # Here you will define the type of shell/operating system
SAVED_CONFIGURE_SETTINGS = (SKIP_MISSARGS,              # This tuple will be linked to the variable current_configuration_index and constant CONFIGURATION_VARS and contains the values ​​currently set in the configuration
                            OVERWRITEDIR_LOCK,
                            DEBUG_MODE, BETA_LANGS, 
                            VERBOSITY_LEVEL, 
                            MAKE_PROJECT_BACKUPS, 
                            MAX_BACKUPS, 
                            BACKUP_PATH,
                            USE_THREADS,
                            MAX_THREADS)
SAVED_CUSTOMIZE_SETTINGS = (SHOW_PROGRESSBAR,           # This tuple will be linked to the variable current_customization_index and constant CUSTOMIZATION_VARS and contains the values ​​currently set in the customization
                            COLOR_HIGHLIGHTING, 
                            SOUNDS, 
                            NOTIFICATION_AT_END, 
                            ENABLE_NOTIFY_AFTER, 
                            ERROR_NOTIFICATION, 
                            SUCCESS_NOTIFICATION, 
                            HELP_ON_ARGERRORS)
DEFAULT_CONFIGURATION = {                               # This dictionary contains the factory settings for the configuration.
    "Skip Invalid Parameters": False,
    "Directory Overwrite Lock": True,
    "Debug Mode": False,
    "Beta Languages": False,
    "Verbosity Level": 2,
    "Create Project Backups": True,
    "Maximum Backups": 99,
    "Backup Folder": os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backups')),
    "Use Threads": False,
    "Maximum Threads": 20,
    "Shows Progress Bar": True,
    "Color Highlighting": True,
    "Sounds": True,
    "Completion Notification": True,
    "Time Until Notification": 35,
    "Error Notification": 4,
    "Success Notification":  3,
    "Help on Parameter Errors": True
}
CONFIGURATION_VARS = (                                  # This tuple will be linked to the variable current_configuration_index to detect the active variable in the configuration panel
    "Skip Invalid Parameters", 
    "Directory Overwrite Lock", 
    "Debug Mode", 
    "Beta Languages", 
    "Verbosity Level", 
    "Create Project Backups", 
    "Maximum Backups",
    "Backup Folder",
    "Use Threads",
    "Maximum Threads"
)
CUSTOMIZATION_VARS = (                                  # This tuple will be linked to the variable current_customization_index to detect the active variable in the customization panel
    "Shows Progress Bar", 
    "Color Highlighting", 
    "Sounds", 
    "Completion Notification", 
    "Time Until Notification", 
    "Error Notification", 
    "Success Notification", 
    "Help on Parameter Errors"
)
current_configuration = {                               # Dictionary that holds the keys and values ​​of the user configuration. This dictionary will be modified at each setting.
    "Skip Invalid Parameters": SKIP_MISSARGS,
    "Directory Overwrite Lock": OVERWRITEDIR_LOCK,
    "Debug Mode": DEBUG_MODE,
    "Beta Languages": BETA_LANGS,
    "Verbosity Level": VERBOSITY_LEVEL,
    "Create Project Backups": MAKE_PROJECT_BACKUPS,
    "Maximum Backups": MAX_BACKUPS,
    "Backup Folder": BACKUP_PATH,
    "Use Threads": USE_THREADS,
    "Maximum Threads": MAX_THREADS,
    "Shows Progress Bar": SHOW_PROGRESSBAR,
    "Color Highlighting": COLOR_HIGHLIGHTING,
    "Sounds": SOUNDS,
    "Completion Notification": NOTIFICATION_AT_END,
    "Time Until Notification": ENABLE_NOTIFY_AFTER,
    "Error Notification": ERROR_NOTIFICATION,
    "Success Notification":  SUCCESS_NOTIFICATION,
    "Help on Parameter Errors": HELP_ON_ARGERRORS
}
CURRENT_CONFIGURATION_BACKUP = deepcopy(current_configuration) # This dictionary saves a backup copy of the current configuration (only at the start of the script) and is used to check whether there are differences or not between it and the dictionary that saves the modifications (current_configuration) and to know if any changes were made.
HANGSFROM_RELATIONSHIPS = {                                    # Contains the relationships that some settings have with others and checks if the state of a variable depends on the state of others.
    'Maximum Backups': 'Create Project Backups',
    'Backup Folder': 'Create Project Backups',
    'Maximum Threads': 'Use Threads',
    'Completion Notification': 'Sounds',
    'Time Until Notification': 'Completion Notification',
    'Error Notification': 'Completion Notification',
    'Success Notification': 'Completion Notification'
}
ACTION_TYPES = {                                               # Contains the action types of each variable
    "Skip Invalid Parameters": 'turn',
    "Directory Overwrite Lock": 'turn',
    "Debug Mode": 'turn',
    "Beta Languages": 'turn',
    "Verbosity Level": 'level',
    "Create Project Backups": 'turn',
    "Maximum Backups": 'level',
    "Backup Folder": 'input',
    "Use Threads": 'turn',
    "Maximum Threads": 'level',
    "Shows Progress Bar": 'turn',
    "Color Highlighting": 'turn',
    "Sounds": 'turn',
    "Completion Notification": 'turn',
    "Time Until Notification": 'level',
    "Error Notification": 'level',
    "Success Notification":  'level',
    "Help on Parameter Errors": 'turn'
}

KEY_TYPES_FILTER = {                                          # Contains the value types of each variable
    "Skip Invalid Parameters": bool,
    "Directory Overwrite Lock": bool,
    "Debug Mode": bool,
    "Beta Languages": bool,
    "Verbosity Level": int,
    "Create Project Backups": bool,
    "Maximum Backups": int,
    "Backup Folder": str,
    "Use Threads": bool,
    "Maximum Threads": int,
    "Shows Progress Bar": bool,
    "Color Highlighting": bool,
    "Sounds": bool,
    "Completion Notification": bool,
    "Time Until Notification": int,
    "Error Notification": int,
    "Success Notification":  int,
    "Help on Parameter Errors": bool
}
bottom_help_configuration_text = generate_dynamic_helps()[0]  # Variable that stores the corresponding "configuration" text based on current_configuration_index
bottom_help_customization_text = generate_dynamic_helps()[1]  # Variable that stores the corresponding "customization" text based on current_customization_index

main_keys_help_text = "[Q] Exit       [ESC] Cancel       [H] Help       [ENTER] Modify       [R] Reset"  # Initial footer text
footer_text = main_keys_help_text   # Variable that stores the footer text (will change depending on the mode)

on_chars = (
    '███████████  █████    ██',
    '██       ██  ██ ███   ██',
    '██       ██  ██  ███  ██',
    '██       ██  ██   ███ ██',
    '███████████  ██    █████'
)
off_chars = (
    '███████████  ███████████  ███████████',
    '██       ██  ██           ██         ',
    '██       ██  ██████████   ██████████ ',
    '██       ██  ██           ██         ',
    '███████████  ██           ██         '
)
error_chars = (
    '   ██   ',
    '   ██   ',
    '   ██   ',
    '        ',
    '   ██   ',)
zero_chars = (
    ' ██████ ',
    '██    ██',
    '██    ██',
    '██    ██',
    ' ██████ ',)
one_chars = (
    '   ██   ',
    ' ████   ',
    '   ██   ',
    '   ██   ',
    '   ██   ',)
two_chars = (
    '████████',
    '      ██',
    ' ██████ ',
    '██      ',
    '████████',)
three_chars = (
    '████████',
    '      ██',
    '███████ ',
    '      ██',
    '████████',)
four_chars = (
    '██    ██',
    '██    ██',
    '████████',
    '      ██',
    '      ██',)
five_chars = (
    '████████',
    '██      ',
    '███████ ',
    '      ██',
    '████████',)
six_chars = (
    '██      ',
    '██      ',
    '████████',
    '██    ██',
    '████████',)
seven_chars = (
    '████████',
    '      ██',
    '     ██ ',
    '    ██  ',
    '   ██   ',)
eight_chars = (
    '████████',
    '██    ██',
    ' ██████ ',
    '██    ██',
    '████████',)
nine_chars = (
    '████████',
    '██    ██',
    '████████',
    '      ██',
    '      ██',)


char_sets = {                                     # Simple dictionary of connection between numeric values, boolean values ​​or error states with the corresponding charsets
    'True': on_chars,
    'False': off_chars,
    'ERROR': error_chars,
    0: zero_chars,
    1: one_chars,
    2: two_chars,
    3: three_chars,
    4: four_chars,
    5: five_chars,
    6: six_chars,
    7: seven_chars,
    8: eight_chars,
    9: nine_chars,
}

show_help_panel = False           # Variable that stores the state (shown or hidden) of the help panel
has_hide_before = False           # This variable will be True if the terminal is too small to display the global panel.
dynamic_num_var_left = False      # Variables to generate 
dynamic_num_var_right = False     # the movement of the "gear"
colors_has_changed = False        # Value that checks if the user changed the colors (to call the redraw function only when necessary)
last_check_panel = False          # Variable to save if the help panel was hidden due to lack of size
not_help_possible = False         # This variable will be True when the terminal is too small to display the help panel and will be temporarily closed (it will be reopened when there is space)
current_configuration_index = 0   # Current index in the configuration panel (CONFIGURATION_VARS)
current_customization_index = 0   # Current index in the customization panel (CUSTOMIZATION_VARS)
current_panel = "left"            # Current panel selected

TOP_MARGIN = 2                    # Top margin rows
BOTTOM_MARGIN = 2                 # Bottom margin rows


def generate_dict_to_save_changes(config_dict: tuple = CONFIGURATION_VARS, custom_dict: tuple = CUSTOMIZATION_VARS, combinate_dict: dict = current_configuration) -> dict[str, dict]:
    '''
    Returns a dictionary divided into two sections: Settings and Customization.
    Ready to be sent to the configuration file `config.ini`
    
    :param config_dict (tuple): Configuration tuple
    :param custom_dict (tuple): Customization tuple
    :param combinated_dict (dict): Currents settings combinating both panels
    :return (dict): Dictionary organized into sections

    '''
    final_dict = {'Settings': {}, 'Customize': {}}
    
    for key in combinate_dict.keys():
        ini_var_name = key.lower().replace(' ', '_') 
        
        if key in config_dict: final_dict['Settings'][ini_var_name] = combinate_dict[key]
        elif key in custom_dict: final_dict['Customize'][ini_var_name] = combinate_dict[key]

    return final_dict


def save_changes_on_ini(dict: dict) -> None:
    '''
    Final step to save changes on `config.ini` file before exit
    
    :param dict (dict): The dictionary generated in the `generate_dict_to_save_changes` function
    '''
    for section, keys in dict.items():
        for key, value in keys.items():
            set_value(section=section, option=key, value=value)


def combine_ascii_numbers(number: int, char_sets: dict) -> tuple:
    """
    Combines multi-digit ASCII character tuples into a single tuple to represent the complete number.

    :param number: Integer to be represented (eg. 101).
    :param char_sets: Dictionary with ASCII tuples for each digit.
    :return: A tuple with the lines combined to represent the entire number.
    """
    digits = str(number)    
    combined_lines = [""] * len(next(iter(char_sets.values())))  # Asume que todas las tuplas tienen la misma longitud

    for digit in digits:
        ascii_digit = char_sets[int(digit)]
        # Combine lines with two spaces separating them
        for i, line in enumerate(ascii_digit):
            combined_lines[i] += line + "  "

    # Delete the two spaces to the right of the last digit
    combined_lines = tuple(line[:-2] for line in combined_lines)

    return combined_lines


def get_current_help_option_value() -> str:
    '''
    Function to generate the help panel text dynamically
    '''
    current_index = current_configuration_index if current_panel == 'left' else current_customization_index
    bottom_help_text = bottom_help_configuration_text if current_panel == 'left' else bottom_help_customization_text
    help_text = bottom_help_text[current_index % len(bottom_help_text)]
    
    return help_text


def get_current_key(convert_ini_to_var: bool = False) -> str:
    '''
    Function that returns the value of the currently selected variable
    
    :param convert_ini_to_var (bool): If this value is True, the string will be converted to lowercase and spaces will be replaced with "_" (underscores). Format of the `config.ini` file
    '''
    current_key = CONFIGURATION_VARS[current_configuration_index] if current_panel == 'left' else CUSTOMIZATION_VARS[current_customization_index]
    if convert_ini_to_var: current_key = current_key.lower().replace(' ', '_')
    
    return current_key


def get_current_char_value() -> tuple:
    '''
    Returns the tuple corresponding to the value of the current key.
    '''
    current_key = get_current_key()
    current_value = current_configuration.get(current_key)
    
    if isinstance(current_value, bool):
        current_char = char_sets.get(str(current_value)) 
    elif isinstance(current_value, str):
        current_char = char_sets.get(str(bool(current_value))) if current_value != 'ERROR' else char_sets.get(current_value)
    elif isinstance(current_value, int):
        current_char = combine_ascii_numbers(number=current_value, char_sets=char_sets)
    
    return current_char


def action_logics(key: str, new_value: Union[str, bool, int], config: dict = current_configuration, dependencies: dict = HANGSFROM_RELATIONSHIPS, typelist: dict = KEY_TYPES_FILTER) -> bool:   
    '''
    Checks if a variable has a correct type (int, bool, str) and if it can be set/changed based on its dependencies (dict: HANGSFROM_RELATIONSHIPS)
    '''
    if key in dependencies:
        dependency_key = dependencies[key]

        if not config.get(dependency_key, False):
            return False

    if key in typelist:
        value_type = typelist[key]
        
        if isinstance(new_value, bool):
            if value_type != bool:
                return False            
        elif isinstance(new_value, int): 
            if value_type != int:
                return False
        elif isinstance(new_value, str): 
            if value_type != str:
                return False
    else:
        return False    
    
    return True
    
    
def setup_colors() -> None:
    import platform
    global shell
    """Setting custom colors based on platform"""
    curses.start_color()
    curses.use_default_colors()
    if current_configuration['Color Highlighting'] and curses.can_change_color():
        def init_colors():
            curses.init_color(11, *custom_color_1)
            curses.init_color(12, *custom_color_2)
            curses.init_color(13, *custom_color_3)
            curses.init_color(14, *custom_color_4)
            curses.init_color(15, *custom_color_5)
            curses.init_color(51, *custom_color_61)
            curses.init_color(52, *custom_color_62)
            curses.init_color(53, *custom_color_63)
            curses.init_color(54, *custom_color_64)
            curses.init_color(55, *custom_color_65)
            curses.init_color(56, *custom_color_66)
            curses.init_color(57, *custom_color_67)
            curses.init_color(58, *custom_color_68)
            curses.init_color(59, *custom_color_69)
            curses.init_color(60, *custom_color_70)
            curses.init_color(61, *custom_color_71)
            curses.init_color(108, *custom_color_98)
            curses.init_color(109, *custom_color_99)

            # Inicializar pares de colores
            curses.init_pair(1, curses.COLOR_BLACK, 11)   # Titles
            curses.init_pair(2, 52, 12)                   # Top Right
            curses.init_pair(3, 52, 13)                   # Top Left
            curses.init_pair(4, 11, 14)                   # Bottom Left
            curses.init_pair(5, 51, 15)                   # Bottom Right
            curses.init_pair(43, 57, 53)                  # Selected-Item Enabled
            curses.init_pair(47, 59, 53)                  # Selected-Item Disabled
            curses.init_pair(44, 61, 54)                  # first and last Item (shadow)
            curses.init_pair(45, 56, 55)                  # Non-Selected-Item
            curses.init_pair(46, 60, 58)                  # Dup-Items
            curses.init_pair(97, 11, 54)                  # Footer
            curses.init_pair(98, curses.COLOR_WHITE, 108) # V-Separators
            curses.init_pair(99, curses.COLOR_BLACK, 109) # General Window
            
        if 'windows' in platform.system().lower() and int(platform.version().split('.')[0]) >= 10:
            custom_color_1 = hex_to_rgb("#44475A")  # Title BG
            custom_color_2 = hex_to_rgb("#202228")  # Top Right BG
            custom_color_3 = hex_to_rgb("#242632")  # Top Left BG
            custom_color_4 = hex_to_rgb("#282A36")  # Bottom Right BG
            custom_color_5 = hex_to_rgb("#282A36")  # Bottom Right BG
            custom_color_61 = hex_to_rgb("#44475A") # Bottom Right FG
            custom_color_62 = hex_to_rgb("#44475A") # Top Panels FG
            custom_color_63 = hex_to_rgb("#313242") # Selected-Item BG
            custom_color_64 = hex_to_rgb("#222530") # First & Last item BG
            custom_color_65 = hex_to_rgb("#292a35") # Non-Selected-Item BG
            custom_color_66 = hex_to_rgb("#4c4d62") # Non-Selected-Item FG -----
            custom_color_67 = hex_to_rgb("#8BE9FD") # Selected-Item Enabled FG
            custom_color_68 = hex_to_rgb("#282a35") # Dup-Item BG
            custom_color_69 = hex_to_rgb("#FF79C6") # Selected-Item Disabled FG
            custom_color_70 = hex_to_rgb("#363947") # Dup-Item FG
            custom_color_71 = hex_to_rgb("#2f3240") # First & Last item FG
            custom_color_98 = hex_to_rgb("#282A36") # Separator BG
            custom_color_99 = hex_to_rgb("#282A36") # General Background
            init_colors()
            shell = 'win>10'
        elif 'windows' not in platform.system().lower() and not any(keyword in platform.uname().release.lower() for keyword in ("wsl", "microsoft", "windows")):
            custom_color_1 = hex_to_rgb("#44475A")  # Title BG
            custom_color_2 = hex_to_rgb("#202228")  # Top Right BG
            custom_color_3 = hex_to_rgb("#242632")  # Top Left BG
            custom_color_4 = hex_to_rgb("#282A36")  # Bottom Right BG
            custom_color_5 = hex_to_rgb("#282A36")  # Bottom Left BG
            custom_color_61 = hex_to_rgb("#44475A") # Bottom Right FG
            custom_color_62 = hex_to_rgb("#44475A") # Top Panels FG
            custom_color_63 = hex_to_rgb("#313242") # Selected-Item BG
            custom_color_64 = hex_to_rgb("#222530") # First & Last item BG
            custom_color_65 = hex_to_rgb("#292a35") # Non-Selected-Item BG
            custom_color_66 = hex_to_rgb("#4c4d62") # Non-Selected-Item FG ----
            custom_color_67 = hex_to_rgb("#8BE9FD") # Selected-Item Enabled FG
            custom_color_68 = hex_to_rgb("#282a35") # Dup-Item BG
            custom_color_69 = hex_to_rgb("#FF79C6") # Selected-Item Disabled FG
            custom_color_70 = hex_to_rgb("#363947") # Dup-Item FG
            custom_color_71 = hex_to_rgb("#2f3240") # First & Last item FG
            custom_color_98 = hex_to_rgb("#282A36") # Separator BG
            custom_color_99 = hex_to_rgb("#282A36") # General Background
            init_colors()
            shell = 'unix'
        else:
            curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)    # Titles
            curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)    # Top Right
            curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)    # Top Left
            curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)    # Bottom Right
            curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)    # Bottom Left
            curses.init_pair(43, curses.COLOR_CYAN, curses.COLOR_BLACK)    # Selected-Item 1
            curses.init_pair(44, curses.COLOR_WHITE, curses.COLOR_BLACK)   # First & last item
            curses.init_pair(45, curses.COLOR_WHITE, curses.COLOR_BLACK)   # Non- Selected-Item 1
            curses.init_pair(46, curses.COLOR_WHITE, curses.COLOR_BLACK)   # Non-Selected-Item 2
            curses.init_pair(47, curses.COLOR_RED, curses.COLOR_BLACK)     # Selected-Item 2
            curses.init_pair(48, curses.COLOR_WHITE, curses.COLOR_BLACK)   # Dup-Item
            curses.init_pair(97, curses.COLOR_WHITE, curses.COLOR_BLACK)   # Footer
            curses.init_pair(98, curses.COLOR_RED, curses.COLOR_BLACK)     # V-Separator
            curses.init_pair(99, curses.COLOR_WHITE, curses.COLOR_BLACK)   # General
            shell = 'wsl/win<10'
    else:
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)    # Titles
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)    # Top Right
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)    # Top Left
        curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)    # Bottom Right
        curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)    # Bottom Left
        curses.init_pair(43, curses.COLOR_BLACK, curses.COLOR_WHITE)   # Selected-Item 1
        curses.init_pair(44, curses.COLOR_WHITE, curses.COLOR_BLACK)   # First & last item
        curses.init_pair(45, curses.COLOR_WHITE, curses.COLOR_BLACK)   # Non- Selected-Item 1
        curses.init_pair(46, curses.COLOR_WHITE, curses.COLOR_BLACK)   # Non-Selected-Item 2
        curses.init_pair(47, curses.COLOR_BLACK, curses.COLOR_WHITE)   # Selected-Item 2
        curses.init_pair(48, curses.COLOR_WHITE, curses.COLOR_BLACK)   # Dup-Item
        curses.init_pair(97, curses.COLOR_WHITE, curses.COLOR_BLACK)   # Footer
        curses.init_pair(98, curses.COLOR_WHITE, curses.COLOR_BLACK)   # V-Separator
        curses.init_pair(99, curses.COLOR_WHITE, curses.COLOR_BLACK)   # General
        shell = 'no-color'


def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    '''
    Convert HEX to RGB color
    
    :param hex_color (str): Color on hexadecimal, e.g. `#224646`
    :return: A tuple like [255, 120, 33]
    '''
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
    return int(r * 1000 / 255), int(g * 1000 / 255), int(b * 1000 / 255)

def draw_rotating_list(window, text_list: tuple, current_index: int, width: int, height: int, dynamic: bool, panel: str) -> None:
    """
    Draws a vertically centered rotating list, with the selected item always in the center
    
    :param window: Window object of curses
    :param text_list: tuple of element to show
    :param current_index: Current index of selection on text_list
    :param width: Width of the panel where the list will be displayed
    :param height: Height of the panel where the list will be displayed
    :param dynamic: Indicates whether the panel is active
    :param panel: Indicates the panel from which the function is called
    """
    half_height = height // 2
    list_length = len(text_list)
    list_length_up = list_length // 2
    
    dynamic_num_var = dynamic_num_var_left if panel == 'left' else dynamic_num_var_right
    dynamic_num = 0 if dynamic else 1

    for i in range(-half_height, half_height):
        list_index = (current_index + i) % list_length
        y_pos = half_height + i
        
        # Make sure y_pos is within the window range
        if y_pos < 0 or y_pos >= height or y_pos == 1: # REMOVE LINES OUT OF PANEL & FIRST LINE (for separation)
            continue
        
        # Limit text to window width
        element = text_list[list_index][:width - 1]
        element_width = 26 if i % 2 == dynamic_num else 24
        side_offset_left = (element_width - len(element)) // 2
        side_offset_right = element_width - len(element) - side_offset_left
        display_text = f"    {' ' * side_offset_left}{element}{' ' * side_offset_right}    "
        if not dynamic_num_var: dynamic_spacer, dynamic_decorator = '', '███'
        else: dynamic_spacer, dynamic_decorator = ' ', '██' 
        
        if i == 0:                                                 # CENTER
            display_text = f"{dynamic_decorator}{dynamic_spacer}    {' ' * (side_offset_left - 1 if dynamic else side_offset_left)}{element}{' ' * (side_offset_right - 1 if dynamic else side_offset_right)}    {dynamic_spacer}{dynamic_decorator}"
            window.addstr(y_pos, max(0, (width - len(display_text)) // 2), display_text, curses.color_pair(43 if current_configuration[text_list[list_index]] and action_logics(key=text_list[list_index], new_value=current_configuration[text_list[list_index]]) else 47)) # curses.A_REVERSE |
        elif y_pos == 2 or y_pos == half_height *2 -2:             # TOP & BOTTOM
            window.addstr(y_pos, max(0, (width - len(display_text)) // 2), display_text, curses.color_pair(44))
        elif y_pos == half_height *2 -1:                           # REMOVE LAST BOTTOM LINE
            pass
        elif -list_length_up < i < (list_length - list_length_up): # CENTRAL ELEMENTS
            window.addstr(y_pos, max(0, (width - len(display_text)) // 2), display_text, curses.color_pair(45))
        else:                                                      # DARKEN DUPLICATES
            window.addstr(y_pos, max(0, (width - len(display_text)) // 2), display_text, curses.color_pair(46))
    window.refresh()


def draw_centered_text_in_panel(window, text: str = None, offset_y: int = 0, offset_x: str = 0, charset: tuple = None, multiline: bool = False) -> None:
    """
    This function receives a single line, multiple lines, or a charset (tuple) text and centers it in the received panel.
    """
    panel_height, panel_width = window.getmaxyx()

    if charset:
        display_text = charset
        ascii_height = len(display_text)
        centered_y = max(0, (panel_height - ascii_height) // 2 + offset_y)

        # Draw each ASCII line centered horizontally
        for i, line in enumerate(display_text):
            centered_x = max(0, (panel_width - len(line)) // 2 + offset_x)
            # Asegurarse de no exceder los bordes del panel
            truncated_line = line[:panel_width - 1]
            window.addstr(centered_y + i, centered_x, truncated_line)
            
    elif multiline:
        lines = text.split('\n') if isinstance(text, str) else text
        total_text_height = len(lines)
        start_y = max(0, (panel_height - total_text_height) // 2 + offset_y)

        # Draw each ASCII line centered horizontally
        for i, line in enumerate(lines):
            centered_x = max(0, (panel_width - len(line)) // 2 + offset_x)
            truncated_line = line[:panel_width - 1]  # Limitar para no exceder el ancho
            window.addstr(start_y + i, centered_x, truncated_line)
    
    else:
        centered_y = max(0, (panel_height) // 2 + offset_y)             # V-CENTER  
        centered_x = max(0, (panel_width - len(text)) // 2 + offset_x)  # H-CENTER
        display_text = text[:panel_width - 1]

        window.addstr(centered_y, centered_x, display_text)
    window.refresh()


def draw_screen(stdscr) -> None:
    '''
    Main function that is responsible for drawing all the panels and composes the entire visual layer
    '''
    global show_help_panel, current_configuration_index, current_customization_index, current_panel, last_check_panel, not_help_possible, has_hide_before, colors_has_changed

    curses.curs_set(0)
    if colors_has_changed:
        stdscr.clear()
        colors_has_changed = False
    stdscr.bkgd(' ', curses.color_pair(99))
    stdscr.refresh()

    height, width = stdscr.getmaxyx() 
    
    if height < 5 or width < 75:
        raise Exception('The terminal is too small, resize it')
    
    elif height >= 43 and width >= 110:
        if has_hide_before:
            has_hide_before = False
            stdscr.clear()
            stdscr.refresh()
            
        # Define main panel dimensions #########################################################
        title_panels_height = 3
        title_panels_width = 40
        panel_height = int(height * 0.6) - title_panels_height
        footer_height = 1
        bottom_panel_height = height - panel_height - (footer_height +1) - title_panels_height
        left_bottom_width = int(width * 0.8) - 1
        
        if show_help_panel: right_bottom_width = max(30, width - left_bottom_width - 1)
        else: right_bottom_width = width - 2
    
        adjusted_panel_height = int(height * 0.6) - TOP_MARGIN - BOTTOM_MARGIN
        panel_height = max(5, adjusted_panel_height)
            
        #########################################################################################
        
        total_width = width - 2                  # Subtract 2 for the side edges
        left_width = total_width // 2 
        right_width = total_width - left_width

        left_width = max(left_width, 5)  
        right_width = max(right_width, 5)

        left_window_start_x = 1  
        right_window_start_x = left_window_start_x + left_width + 1  # Separator between windows

        if right_window_start_x + right_width > width - 1:            
            total_width = width - 3 
            left_width = total_width // 2
            right_width = total_width - left_width
            right_window_start_x = left_window_start_x + left_width + 1
        
        title_left_start_x = left_window_start_x + (left_width - title_panels_width) // 2
        title_right_start_x = right_window_start_x + (right_width - title_panels_width) // 2

        # Create the windows #####################################################################
        title_left_window = curses.newwin(
            title_panels_height, title_panels_width,
            TOP_MARGIN,  # Siempre encima de los paneles principales
            max(1, title_left_start_x + 1)  # Asegurar que no salga del borde izquierdo
        )

        title_right_window = curses.newwin(
            title_panels_height, title_panels_width,
            TOP_MARGIN,
            max(1, title_right_start_x + 1)  # Asegurar que no salga del borde izquierdo
        )
        
        
        left_window = curses.newwin(
            panel_height, left_width,
            TOP_MARGIN + title_panels_height,
            left_window_start_x
        )

        right_window = curses.newwin(
            panel_height, right_width,
            TOP_MARGIN + title_panels_height,
            right_window_start_x
        )
        
        left_bottom_window = curses.newwin(bottom_panel_height, 
                                           left_bottom_width, 
                                           panel_height + 1 + BOTTOM_MARGIN + title_panels_height, 
                                           1
        )
        
        right_bottom_window = curses.newwin(bottom_panel_height, 
                                            right_bottom_width if not show_help_panel else right_bottom_width -1, 
                                            panel_height + 1 + BOTTOM_MARGIN + title_panels_height, 
                                            left_bottom_width + 1 if show_help_panel else 1
        )
        
        footer_window = curses.newwin(footer_height, 
                                      width, 
                                      height - footer_height, 
                                      0
        )

        title_left_window.bkgd(' ', curses.color_pair(1))
        title_right_window.bkgd(' ', curses.color_pair(1))
        
        draw_centered_text_in_panel(window=title_left_window,
                                    text="Configuration")
        draw_centered_text_in_panel(window=title_right_window,
                                    text="Customization")
        
        stdscr.hline(title_panels_height + 2, 0, ' ', width)
        
        left_window.bkgd(' ', curses.color_pair(2 if current_panel == 'left' else 3))
        draw_rotating_list(window=left_window, 
                           text_list=CONFIGURATION_VARS, 
                           current_index=current_configuration_index, 
                           width=width // 2, 
                           height=panel_height, 
                           dynamic=dynamic_num_var_left, 
                           panel='left')
        
        right_window.bkgd(' ', curses.color_pair(3 if current_panel == 'left' else 2))
        draw_rotating_list(window=right_window, 
                           text_list=CUSTOMIZATION_VARS, 
                           current_index=current_customization_index, 
                           width=width // 2, 
                           height=panel_height, 
                           dynamic=dynamic_num_var_right, 
                           panel='right')       
        
        if width <= 144: 
            if show_help_panel: last_check_panel = True
            show_help_panel = False
            not_help_possible = True
        else:
            if last_check_panel: 
                show_help_panel = True
                last_check_panel = False
            not_help_possible = False
            

        
        if show_help_panel:
            left_bottom_window.bkgd(' ', curses.color_pair(4))
            draw_centered_text_in_panel(window=left_bottom_window, text=get_current_help_option_value(), offset_y=-1, multiline=True)
            stdscr.vline(panel_height + 1 + BOTTOM_MARGIN + title_panels_height, left_bottom_width, ' ' if shell != 'wsl/win<10' and shell != 'no-color' else '-', bottom_panel_height - footer_height, curses.color_pair(98))

        right_bottom_window.bkgd(' ', curses.color_pair(5)) #! NOTA:   establecer colores de estado 
        if check_configuration_integrity(dict=generate_dict_to_save_changes(), single_key=get_current_key(convert_ini_to_var=True)): 
            current_charset = get_current_char_value() 
            '''if current_charset == on_chars: right_bottom_window.bkgd(' ', curses.color_pair(5))
            elif current_charset == off_chars:  right_bottom_window.bkgd(' ', curses.color_pair(5))
            else: right_bottom_window.bkgd(' ', curses.color_pair(5))'''
        else: 
            current_charset = error_chars
            #right_bottom_window.bkgd(' ', curses.color_pair(5))
            
        draw_centered_text_in_panel(window=right_bottom_window, charset=current_charset)

        footer_window.bkgd(' ', curses.color_pair(97))
        footer_window.addstr(0, max(0, (width - len(footer_text)) // 2), footer_text)
        footer_window.refresh()
    
    else:
        has_hide_before = True
        current_text = "The terminal is too small, resize until the configuration menu is displayed"
        current_text2 = "Press 'ESC' or 'Q' to exit" 
        stdscr.clear()
        stdscr.refresh()
        cant_show_config_mode = curses.newwin(height, width, 0, 0)
        text_y = height // 2
        text_x = (width - len(current_text)) // 2
        text_x2 = (width - len(current_text2)) // 2
        
        cant_show_config_mode.bkgd(' ', curses.color_pair(99))
        cant_show_config_mode.addstr(text_y, text_x, current_text)
        cant_show_config_mode.addstr(height - 1, text_x2, current_text2)
        cant_show_config_mode.refresh()
        
def main(stdscr) -> None:
    '''
    This function is responsible for the main loop and processing all key presses and performing subsequent actions, such as setting new values ​​for variables.
    '''
    global show_help_panel, current_configuration_index, current_customization_index, current_panel, current_configuration, footer_text, dynamic_num_var_left, dynamic_num_var_right
    
    curses.curs_set(0)
    stdscr.keypad(True)
    curses.set_escdelay(1)
    #curses.noecho()  # Desactiva el echo de teclas
    #curses.cbreak()  # Lee teclas sin presionar enter
    #stdscr.nodelay(True)

    current_key = ''
    backup_current_key_value = None
    current_action_type = ''
    input_string = None
    input_mode = False
    func = None
    
    def play_sound_function(sound: str, index: int=None) -> None:
        if current_configuration['Sounds']:
            play(sound=sound, index=index)
           
    def set_new_value(key: str, new_value: Union[str, bool, int], play_sound: bool = True, sound: str = 'turn') -> None:
        global bottom_help_customization_text, bottom_help_configuration_text
        current_configuration[key] = new_value
        bottom_help_configuration_text = generate_dynamic_helps()[0]
        bottom_help_customization_text = generate_dynamic_helps()[1]

        if play_sound: play_sound_function(sound=sound)
                
    def set_backup_folder(key: str, new_value: str, play_sound: bool = False) -> None:
        set_new_value(key=key, new_value=str(new_value), play_sound=play_sound)
    
    def set_notification(key: str, new_value: int, play_sound: bool = False, sound: str = 'turn') -> None:
        def check_notification_type() -> None:
            sound = 'error' if key == 'Error Notification' else 'success'
            play_sound_function(sound=sound, index=new_value)
            
        set_new_value(key=key, new_value=new_value, play_sound=play_sound) 
        if not play_sound and sound == 'switch_option':
            check_notification_type()
            
    def toggle_color_highlighting(key: str, new_value: bool) -> None:
        global colors_has_changed
        set_new_value(key=key, new_value=new_value)
        colors_has_changed = True
        setup_colors()
    
    def autocomplete_path(current_path: str) -> str:
        if not current_path: return ""
        directory, prefix = os.path.split(current_path)
        if not directory: directory = "."

        try:
            items = os.listdir(directory)
            matches = [item for item in items if item.startswith(prefix)]
            return os.path.join(directory, matches[0]) if matches else current_path
        except FileNotFoundError:
            return current_path


    ACTION_FUNCTIONS = {
    'turn': {
        "Skip Invalid Parameters": set_new_value,
        "Directory Overwrite Lock": set_new_value,
        "Debug Mode": set_new_value,
        "Beta Languages": set_new_value,
        "Create Project Backups": set_new_value,
        "Use Threads": set_new_value,
        "Shows Progress Bar": set_new_value,
        "Color Highlighting": toggle_color_highlighting,
        "Sounds": set_new_value,
        "Completion Notification": set_new_value,
        "Help on Parameter Errors": set_new_value
        },
    'level': {
        'Verbosity Level': set_new_value,
        'Maximum Backups': set_new_value,
        'Maximum Threads': set_new_value,
        'Time Until Notification': set_new_value,
        "Error Notification": set_notification,
        "Success Notification": set_notification,
        },
    'input': {
        "Backup Folder": set_backup_folder,
        },
    }

    levels = {
        'Verbosity Level': (0, 5),
        'Maximum Backups': (1, 999),
        'Maximum Threads': (2, 999),
        'Time Until Notification': (0, 999),
        'Error Notification': (1, len([file for file in os.listdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'notification_sounds', 'error')))])),
        'Success Notification': (1, len([file for file in os.listdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'notification_sounds', 'success')))])),
    }
    
    
    setup_colors()
    while True:
        draw_screen(stdscr)

        char = stdscr.getch()
        
        if input_mode:                        
            if input_mode == 'input':
                input_string = str(current_configuration[current_key])
                
                if 32 <= char <= 126:  # Rangos ASCII imprimibles
                    input_string += chr(char)
                
                elif char == 9 and input_string != '' and current_key in {'Backup Folder',}:
                    input_string = autocomplete_path(current_path=input_string)
                
                elif char in (127, curses.KEY_BACKSPACE) and input_string != '':
                    input_string = input_string[:-1] 
                
                func(key=current_key, new_value=str(input_string))

            elif input_mode == 'level':
                input_string = int(current_configuration[current_key])
                
                if char == curses.KEY_UP:
                    input_string += 1
                    if levels[current_key][0] <= input_string <= levels[current_key][1]:
                        func(key=current_key, new_value=int(input_string), sound='switch_option')
                                        
                elif char == curses.KEY_DOWN:
                    input_string -= 1
                    if levels[current_key][0] <= input_string <= levels[current_key][1]: 
                        func(key=current_key, new_value=int(input_string), sound='switch_option')
                    
                elif char == curses.KEY_RIGHT: 
                    if levels[current_key][0] <= input_string <= levels[current_key][1]:
                        func(key=current_key, new_value=int(input_string), sound='switch_option')
                
            
            if char == curses.KEY_ENTER or char in (10, 13):
                footer_text = main_keys_help_text
                if type(input_string) == str and input_string.lstrip() == '':
                    set_new_value(key=current_key, new_value=backup_current_key_value, play_sound=False)
                else: 
                    func(key=current_key, new_value=int(input_string) if KEY_TYPES_FILTER[current_key] == int else str(input_string), play_sound=True)
                
                input_mode = False
                input_string = ''
                continue
                
            elif char == 27:
                footer_text = main_keys_help_text
                set_new_value(key=current_key, new_value=backup_current_key_value, play_sound=False)
                input_mode = False
                input_string = ''
                continue
                       
        else:
            if char == ord('q') or char == ord('Q'):
                if current_configuration != CURRENT_CONFIGURATION_BACKUP: save_changes_on_ini(dict=generate_dict_to_save_changes())
                break
            
            elif char == 27:
                break
            
            elif (char == ord('h') or char == ord('H')) and not not_help_possible and not has_hide_before:
                play_sound_function(sound='toggle')
                show_help_panel = not show_help_panel
                    
            elif char == curses.KEY_LEFT and not has_hide_before:
                play_sound_function(sound='switch_panel')
                current_panel = "left"
                
            elif char == curses.KEY_RIGHT and not has_hide_before:
                play_sound_function(sound='switch_panel')
                current_panel = "right"

            if current_panel == "left" and not has_hide_before:
                current_key = CONFIGURATION_VARS[current_configuration_index]
                backup_current_key_value = current_configuration[current_key]
                current_action_type = ACTION_TYPES[current_key]
                
                if char == curses.KEY_UP:
                    play_sound_function(sound='switch_option')
                    dynamic_num_var_left = not dynamic_num_var_left
                    current_configuration_index = (current_configuration_index - 1) % len(CONFIGURATION_VARS)
                elif char == curses.KEY_DOWN:
                    play_sound_function(sound='switch_option')
                    dynamic_num_var_left = not dynamic_num_var_left
                    current_configuration_index = (current_configuration_index + 1) % len(CONFIGURATION_VARS)
                    
            elif current_panel == "right" and not has_hide_before:
                current_key = CUSTOMIZATION_VARS[current_customization_index]
                backup_current_key_value = current_configuration[current_key]
                current_action_type = ACTION_TYPES[current_key]
                
                if char == curses.KEY_UP:
                    play_sound_function(sound='switch_option')
                    dynamic_num_var_right = not dynamic_num_var_right
                    current_customization_index = (current_customization_index - 1) % len(CUSTOMIZATION_VARS)
                elif char == curses.KEY_DOWN:
                    play_sound_function(sound='switch_option')
                    dynamic_num_var_right = not dynamic_num_var_right
                    current_customization_index = (current_customization_index + 1) % len(CUSTOMIZATION_VARS)
                    
            if char == curses.KEY_ENTER or char in (10, 13) and action_logics(key=current_key, new_value=current_configuration[current_key]) and not has_hide_before:
                if current_action_type == 'turn':
                    func = ACTION_FUNCTIONS[current_action_type].get(current_key)
                    func(key=current_key, new_value=not current_configuration[current_key])

                else:
                    footer_text = "'ESC' to cancel, 'ENTER' to save" if current_action_type == 'input' else "'ESC' to cancel, 'ENTER' to save, arrows to increase or decrease"
                    input_mode = current_action_type
                    if input_mode == 'input': show_help_panel = True
                    input_string = current_configuration[current_key] 
                    func = ACTION_FUNCTIONS[current_action_type].get(current_key)
                    
            elif (char == ord('r') or char == ord('R')) and current_configuration[current_key] != DEFAULT_CONFIGURATION[current_key] and not has_hide_before:
                set_new_value(key=current_key, new_value=DEFAULT_CONFIGURATION[current_key])
                continue
        
            

def init_configuration_shell():
    curses.wrapper(main)

