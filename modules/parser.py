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
This module handles input arguments and much of the checking related to them.
'''
from .help import *
from .settings import (COLOR_HIGHLIGHTING,
                      HELP_ON_ARGERRORS,
                      VERBOSITY_LEVEL)
if COLOR_HIGHLIGHTING: from .colors import Colors
else: from .colors import NoColors as Colors
from argparse import ArgumentParser
import sys

class customParser(ArgumentParser):
    def format_help(self):
        super().format_help()
        return f'''
{APPNAME.capitalize()} v{VERSION} by Sysco Labs™ {Colors.GRAY}\thttps://github.com/Syyysco/{APPNAME.capitalize()}{Colors.END}
____________________________
    
USAGE: {Colors.OKCYAN}{APPNAME}{Colors.END} [{Colors.ARG}-h{Colors.END}] [{Colors.ARG}-H{Colors.END}] [{Colors.ARG}-C{Colors.END}] [{Colors.ARG}-U{Colors.END}] [{Colors.ARG}--version{Colors.END}] [{Colors.ARG}--flush-backups{Colors.END}] [{Colors.ARG}--reconfigure{Colors.END}] |
             [{Colors.ARG}-i{Colors.END} INPUT] [{Colors.ARG}-o{Colors.END} OUTPUT] [{Colors.ARG}-f{Colors.END} FORMAT] [{Colors.ARG}-t{Colors.END} THREADS] [{Colors.ARG}-I{Colors.END} INDENT] [{Colors.ARG}-dDsp{Colors.END}]

DESCRIPTION: This tool allows you to format and/or compact your projects.
             Designed for quick setup and execution on multiple platforms.
{ARGHELP}
'''

    def error(self, message):
        if HELP_ON_ARGERRORS: self.print_help()
        if VERBOSITY_LEVEL > 0: sys.stderr.write(f"\n{Colors.FAIL} Error -> {Colors.END}{message}\n")
        sys.exit(2)


#Arguments control
def parse_arguments(): 
    
    def full_help_call(query: str = None) -> None: # Function that handles the search for queries in the full help panel
        FULL_CONTENTS = (FULL_ARGHELP, NOTES, EXAMPLES, GITHUB)
        temptext_list = []
        temptitle_list = []
        
        if query:
            for i in range(4):
                for x in range(len(FULL_CONTENTS[i])):
                    if query.lstrip().lower() in FULL_CONTENTS[i][x].lower() and FULL_CONTENTS[i][x] not in temptext_list:
                        if FULL_ARGTITLES[i] not in temptitle_list:
                            print(FULL_ARGTITLES[i])
                            temptitle_list.append(FULL_ARGTITLES[i])
                        print(FULL_CONTENTS[i][x].replace(query, f'{Colors.FAIL}{query}{Colors.END}'))
                        temptext_list.append(FULL_CONTENTS[i][x])

        else: 
            for i in range(4):
                print(FULL_ARGTITLES[i])
                for x in range(len(FULL_CONTENTS[i])):
                    print(FULL_CONTENTS[i][x])
        sys.exit(0)
        
    #Main argument control
    parser = customParser(description="Tool to save space in files of any programming language.")
    req_args = parser.add_mutually_exclusive_group(required=True) 
    req_args.add_argument('-H', '--fullhelp', action='store_true', help='Show the full help panel')
    req_args.add_argument('-U', '--update', help='Update')
    req_args.add_argument('-C', action='store_true', help='Launch a configuration mode')
    req_args.add_argument('--version', action='store_true', help='Print the app version')
    req_args.add_argument('--reconfigure', action='store_true', help='Restore default configuration')
    req_args.add_argument('--flush-backups', action='store_true', help='Remove all stored backups')
    req_args.add_argument('-i', '--input', type=str, help='Specify an input_file file to format')
    
    parser.add_argument('-o', '--output', required=False, type=str, help='Specify an output_file file')
    parser.add_argument('-f', '--format', required=False, type=str, help='Specify format of files')
    parser.add_argument('-p', '--print', action='store_true', help='Print the compressed/formatted code')
    parser.add_argument('-D', action='store_true', help='Specify a directory mode to format all files recursively')
    parser.add_argument('-s', action='store_true', help='For HTML or PHP files, <style> and <script> tags will not be affected on decompress') #! NOTE: cambiar a -s css, php, script
    parser.add_argument('-d', action='store_true', help='Turn to decompress method')
    parser.add_argument('-I', '--indent', required=False, type=int, help='Define the indentation size (not all languages)')
    parser.add_argument('-t', '--threads', required=False, type=int, help='Indicates the number of threads to use')
    
    #-----------------------------------------------------------------------------------------------------------------------    
    # Prevent none parameter.
    if len(sys.argv) == 1:
        parser.error(f'You must specify one of the required commands [{Colors.ARG}-i{Colors.END}, {Colors.ARG}-C{Colors.END}, {Colors.ARG}-U{Colors.END}]')

    
    # Fix no-error when duplicate arguments.
    ARGS_W_STR = ('-i', '-o', '-f')     # Arguments that can cause errors with duplicates
    prefs = set()                       # Set to detect duplicate in arguments
    
    for element in sys.argv:            # Verify duplicates
        for pref in ARGS_W_STR:
            if element.startswith(pref):
                if pref in prefs:
                    parser.error(f'The {Colors.ARG}{pref}{Colors.END} argument are duplicated')
                prefs.add(pref)
                
    # Handling the individual help commands
    if sys.argv == [sys.argv[0], '-H']:
        full_help_call()
    
    elif (sys.argv[1].startswith('-h') and sys.argv != [sys.argv[0], '-h']) or (sys.argv[1].startswith('-H') and sys.argv != [sys.argv[0], '-H']):
        if len(sys.argv) > 3:
            print(f'\n{Colors.WARNING}WARNING -> {Colors.END}Help command {Colors.ARG}{f"-H" if sys.argv[1][1] == "H" else "-h"}{Colors.END}) only accept one argument.\n'); sys.exit(1)
        elif len(sys.argv[1]) > 2:
            print(f'\n{Colors.WARNING}WARNING -> {Colors.END}Help command {Colors.ARG}{f"-H" if sys.argv[1][1] == "H" else "-h"}{Colors.END} must be separated from the others arguments.\n'); sys.exit(1)
                            
        if sys.argv[1][1] == 'H':
            if len(sys.argv[2]) < 2:
                print(f'\n{Colors.WARNING}HELP -> {Colors.END}Enter at least two characters in the search \n'); sys.exit(1)
            else: full_help_call(sys.argv[2])
        else: # Handle query search with -h option
            found = False
            for line in ARGHELP.splitlines():
                if sys.argv[2] in line:
                    if 'USAGE' not in line: print('\n'+line) if not found else print(line); found = True
            
            if not found: print(f'{Colors.WARNING}HELP -> {Colors.END}The element "{sys.argv[2]}" was not found.')
            sys.exit(0)
    
    return parser.parse_args()