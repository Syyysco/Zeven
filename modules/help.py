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
This module contains all lists related to available languages, extensions and mime-types.
'''
from .colors import Colors
from .config_handler import get_json_value

APPNAME = get_json_value(option='app_name')
VERSION = get_json_value(option='version')
VERSION_OUTPUT = f"""
{APPNAME.capitalize()} {VERSION}
Copyright (C) 2024 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Jose Francisco López López aka Sysco.
"""
ARGHELP = f'''
OPTIONS:                  
  {Colors.ARG}-h, --help {Colors.GRAY}─────────────┨ {Colors.END}show this help message and exit
  {Colors.ARG}-H, --fullhelp {Colors.GRAY}─────────┨ {Colors.END}show the full help panel
  {Colors.ARG}-U, --update {Colors.GRAY}───────────┨ {Colors.END}update the app if possible
  {Colors.ARG}--version {Colors.GRAY}──────────────┨ {Colors.END}print the current version of {APPNAME}
  {Colors.ARG}--reconfigure {Colors.GRAY}──────────┨ {Colors.END}restore default settings
  {Colors.ARG}--flush-backups {Colors.GRAY}────────┨ {Colors.END}remove all stored backups
  {Colors.ARG}-C {Colors.GRAY}─────────────────────┨ {Colors.END}launch configuration mode
  {Colors.GRAY}   ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·   {Colors.END}
  {Colors.ARG}-i, --input {Colors.GRAY}────────────┨ {Colors.END}specify an input to format
  {Colors.ARG}-o, --output {Colors.GRAY}───────────┨ {Colors.END}specify an output (overwrite directories)
  {Colors.ARG}-f, --format {Colors.GRAY}───────────┨ {Colors.END}specify format of files (not be necessary)
  {Colors.ARG}-I, --indent {Colors.GRAY}───────────┨ {Colors.END}define the indentation size (default: 4)
  {Colors.ARG}-t, --threads {Colors.GRAY}──────────┨ {Colors.END}indicates the number of threads to use
  {Colors.ARG}-p, --print {Colors.GRAY}────────────┨ {Colors.END}print the compressed/formatted code
  {Colors.ARG}-D {Colors.GRAY}─────────────────────┨ {Colors.END}specify a directory mode to format all files
  {Colors.ARG}-d {Colors.GRAY}─────────────────────┨ {Colors.END}turn to decompress method
  {Colors.ARG}-s {Colors.GRAY}─────────────────────┨ {Colors.END}<style> and <script> tags will not be affected
'''

FULL_ARGTITLES = (
                f'\n{Colors.END}{Colors.FILE} OPTIONS{Colors.GRAY}   {Colors.END}\n          {Colors.GRAY}│{Colors.END}',
                f'\n{Colors.END}{Colors.FILE} NOTES{Colors.GRAY}     {Colors.END}\n          {Colors.GRAY}│{Colors.END}',
                f'\n{Colors.END}{Colors.FILE} EXAMPLES{Colors.GRAY}  {Colors.END}\n          {Colors.GRAY}│{Colors.END}',
                f'\n{Colors.END}{Colors.FILE} GITHUB{Colors.GRAY}    {Colors.END}\n          {Colors.GRAY}│{Colors.END}',
                )

FULL_ARGHELP = (
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}{ARGHELP.splitlines()[2]}
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}Displays the basic help panel. 
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}It is quick to remember what each option is used for and
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}how the tool syntax works.
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}{ARGHELP.splitlines()[3]}
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}Displays the full help panel, with detailed descriptions, 
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}notes, and examples.
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ ''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}{ARGHELP.splitlines()[4]}
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}Download de new version if it available.
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ ''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}{ARGHELP.splitlines()[5]}
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ ''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}{ARGHELP.splitlines()[6]}
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}Sets all zeven configuration values to default values.
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ ''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}{ARGHELP.splitlines()[7]}
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}Delete all project backups. Be careful, you may lose important data.
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ ''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}{ARGHELP.splitlines()[8]}
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}Starts configuration mode and allows you to change app 
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}settings such as verbosity, directory overwrite protection, and more.
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ ''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}{ARGHELP.splitlines()[9]}
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}Indicate the input file or folder.
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ ''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}{ARGHELP.splitlines()[10]}
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}Indicate the input file or folder.
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ ''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}{ARGHELP.splitlines()[11]}
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}Create a copy of the input or overwrite it as needed.
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ ''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}{ARGHELP.splitlines()[12]}
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}Typically used when a file is not autodetected or to specify one of 
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}several file types to format in recursive/directory mode.
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ ''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}{ARGHELP.splitlines()[13]}
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}In case of formatting files that contain tags, it is possible to 
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}specify the tab size, or rather the number of spaces that the code 
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}indentation contains (only on decompress mode).
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ ''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}{ARGHELP.splitlines()[14]}
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}Run the application with threads (only on directory mode).
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ ''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}{ARGHELP.splitlines()[15]}
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}Prints the final code of the input file (single files only).
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ ''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}{ARGHELP.splitlines()[16]}
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}It is used to indicate that a directory will be formatted recursively
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}to avoid having to specify an output to overwrite.
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ ''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}{ARGHELP.splitlines()[17]}
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}Useful for making the code more legible and organized, 
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}although it takes up more space. 
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ ''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}{ARGHELP.splitlines()[18]}
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}It is practical to maintain control over CSS and JavaScript tags in
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ {Colors.END}HTML and PHP files (only on decompress mode).
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│ ''',
)

NOTES = (
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END} {Colors.POINT}1{Colors.END}. The {Colors.ARG}--help{Colors.END} and {Colors.ARG}--fullhelp{Colors.END} parameters do not accept arguments 
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}    and are always used alone, unlike {Colors.ARG}-h{Colors.END} and {Colors.ARG}-H{Colors.END} ({Colors.POINT}2{Colors.END}).
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END} {Colors.POINT}2{Colors.END}. It is possible to use the {Colors.ARG}-h{Colors.END} or {Colors.ARG}-H{Colors.END} parameters alone or by 
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}    specifying another argument/word to search for it in the 
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}    corresponding help panel.
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END} {Colors.POINT}3{Colors.END}. The {Colors.ARG}-U{Colors.END} or {Colors.ARG}--update{Colors.END} parameter cannot be combined with others.
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}    (personal configurations not will be affected)
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END} {Colors.POINT}4{Colors.END}. The {Colors.ARG}-C{Colors.END} parameter launchs an interactive mode.  
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END} {Colors.POINT}5{Colors.END}. The {Colors.ARG}-i{Colors.END} parameter indicates the file that will be taken as input.
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}    It can be used with or without the {Colors.ARG}-D{Colors.END} parameter ({Colors.POINT}9{Colors.END}).
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}''',

f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END} {Colors.POINT}6{Colors.END}. The {Colors.ARG}-o{Colors.END} parameter not be necessary.
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}    If used, this argument sets directory overwriting to occur if the 
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}     same output name as the input name is specified.
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}    By default files are overwritten if no output is specified. However 
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}     directories are protected against overwriting ({Colors.POINT}9{Colors.END}) (this can be 
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}     changed with {Colors.ARG}-C{Colors.END}) ({Colors.POINT}4{Colors.END}).
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END} {Colors.POINT}7{Colors.END}. The {Colors.ARG}-f{Colors.END} parameter can indicate the format(s) you want to include 
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}     when running on a directory (Files with other formats will not be 
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}     affected)({Colors.POINT}9{Colors.END}).
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END} {Colors.POINT}8{Colors.END}. The {Colors.ARG}-p{Colors.END} parameter it can be used to print the final output of a file without
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}     modifying it, but if an output is specified with -o it will also
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}     save the result in that file.
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END} {Colors.POINT}8{Colors.END}. The {Colors.ARG}-I{Colors.END} parameter it can be used with/out the {Colors.ARG}-d{Colors.END} (decompress)
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}     mode or in normal mode.
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END} {Colors.POINT}9{Colors.END}. The {Colors.ARG}-D{Colors.END} parameter does overwrite directories by default, 
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}     if you do not specify an output ({Colors.ARG}-o{Colors.END}) or specify the same output as the
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}     input file it will be overwritten. {Colors.WARNING}BE CAREFUL!{Colors.END}.
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}''',
)

EXAMPLES = (
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}├{Colors.END} View and search for arguments or keywords in help panels.
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}  {APPNAME} {Colors.ARG}-h
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}  {APPNAME} {Colors.ARG}-H
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}  {APPNAME} {Colors.ARG}--help
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}  {APPNAME} {Colors.ARG}--fullhelp
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}  {APPNAME} {Colors.ARG}-h indent
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}  {APPNAME} {Colors.ARG}-H -U
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}├{Colors.END} Update {APPNAME.capitalize()} if possible.
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}  {APPNAME} {Colors.ARG}-U
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}  {APPNAME} {Colors.ARG}--update
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}├{Colors.END} Initiate the configuration mode.
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}  {APPNAME} {Colors.ARG}-C
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}├{Colors.END} Indicate the input file or directory.
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}  {APPNAME} {Colors.ARG}-i {Colors.END}{Colors.FILE}file.html{Colors.END}
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}  {APPNAME} {Colors.ARG}--input {Colors.END}{Colors.FILE}file.html{Colors.END}
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}├{Colors.END} Indicate the output file or directory.
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}  {APPNAME} {Colors.ARG}-o {Colors.END}{Colors.FILE}file.php{Colors.END}
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}  {APPNAME} {Colors.ARG}--output {Colors.END}{Colors.FILE}my_newfolder{Colors.END}
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}├{Colors.END} Indicate the format(s) of input filter(-D) or file.
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}  {APPNAME} {Colors.ARG}-f {Colors.END}css {Colors.ARG}-i{Colors.END} {Colors.FILE}file{Colors.END}
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}  {APPNAME} {Colors.ARG}--format {Colors.END}"html, json" {Colors.ARG}-D -i{Colors.END} {Colors.FILE}myfolder{Colors.END}
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}├{Colors.END} Specify the number of spaces or indentation size.
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}  {APPNAME} {Colors.ARG}-I {Colors.END} 8 {Colors.ARG}-d {Colors.END}{Colors.ARG}-i{Colors.END} {Colors.FILE}file.css{Colors.END}
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}  {APPNAME} {Colors.ARG}--indent {Colors.END} 8 {Colors.ARG}-d {Colors.END}{Colors.ARG}-i{Colors.END} {Colors.FILE}file.css{Colors.END}
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}├{Colors.END} Indicates the directory mode (recursive).
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}  {APPNAME} {Colors.ARG}-D -i{Colors.END} {Colors.FILE}myfolder{Colors.END}
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}├{Colors.END} Compress everything that isn't CSS <style> and JavaScript <script> tags.
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}  {APPNAME} {Colors.ARG}-i{Colors.END} {Colors.FILE}myfolder{Colors.END} {Colors.ARG}-sD{Colors.END}
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}├{Colors.END} On -d (decompress) mode and compress only that is <script> and <style> tags.
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}  {APPNAME} {Colors.ARG}-i{Colors.END} {Colors.FILE}myfolder{Colors.END} {Colors.ARG}-sdD{Colors.END}
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}├{Colors.END} View the formatted code of a file without saving changes.
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}  {APPNAME} {Colors.ARG}-i{Colors.END} {Colors.FILE}file.html{Colors.END} {Colors.ARG}-dp{Colors.END}
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}├{Colors.END} Browse the compact code of a file indicating the format and saving it.
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}  {APPNAME} {Colors.ARG}-i{Colors.END} {Colors.FILE}file{Colors.END} {Colors.ARG}-o{Colors.END} {Colors.FILE}file2{Colors.END} {Colors.ARG}-p -f{Colors.END} php
{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}'''
)

GITHUB = (
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}  About me: {Colors.OKCYAN}https://www.sysco.github.io{Colors.END}''',
f'''{Colors.BGRAY}          {Colors.END}{Colors.GRAY}│{Colors.END}  Issues:   {Colors.OKCYAN}https://github.com/Syyysco/{APPNAME.capitalize()}/issues{Colors.END}''',
f'''\n''',
)                                 #! NOTA: Falta colocar el enlace al repositorio y buymeacoffe o github. 
