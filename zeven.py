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
                           ▒▒▒▒▒▒▒                        
                          ▒▒▒▒▒▒▒▒▒                       
                          ▒▒▒▒▒▒▒▒▒                       
                          ▒▒▒▒▒▒▒▒▒                       
                            ▒▒▒▒▒                         
                                                  
                                                  
                                                  
                    █████████████████████████████████     
                    █████████████████████████████████     
                    █████████████████████████████████     
                     ████████████████████████████████     
                                            ▒███████▓      
                                           ████████▓       
        ▒▒▒▒▒           ▒▒▒▒▒▒▒▒▒▒▒▒▒     ████████▓        
       ▒▒▒▒▒▒▒      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████▓         
        ▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████▓          
                ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████▓▒▒▒▒▒      
              ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████▓▒▒▒▒▒▒▒▒▒▒  
             ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████▓▒▒▒▒▒▒▒▒▒▒▒▒ 
            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒
           ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒
           ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
           ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
           ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  
           ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒    
           ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████▓▒▒▒▒▒▒▒▒▒▒▒        
           ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████▓▒▒▒▒▒▒▒▒▒▒▒▒        
            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒         
             ▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒         
              ▒▒▒▒▒▒▒▒▒▒▒▒████████▓▒▒▒▒▒▒▒▒▒▒▒▒     ▒▒▒▒  
               ▒▒▒▒▒▒▒▒▒▒████████▓▒▒▒▒▒▒▒▒▒▒▒▒       ▒▒▒  
                 ▒▒▒▒▒▒▒████████▓▒▒▒▒▒▒▒▒▓▓▓              
                   ▒▒▒▒▒▓████████████████▒                
                       ▒▒▒▒▓████████▓▓                    

                       Developed by Sysco
                            ┏┓┏┏┏┏┓
                            ┛┗┫┛┗┗┛
                              ┛    

Sevven is designed to compress and decompress files/projects in various
programming languages in order to make them faster to load and save disk/cloud 
space, as well as being able to work with third-party code that is not readable 
or is not well structured.
------------------------------------------------------------------------------
Author: Jose Francisco López López aka Sysco
Date: October 2024
'''
import sys, importlib, os, mimetypes, time
from modules.config_handler import (check_if_configuration_exists,
                                    check_if_jsonconfig_exists,
                                    check_configuration_integrity,
                                    first_check)
FIRST_CHECK = first_check()
CONF_JSON_EXIST = check_if_jsonconfig_exists()
CONFIGURATION_EXIST = check_if_configuration_exists()
INTEGRITY_CONFIG_CHECK_FAIL = check_configuration_integrity()

try:
    from modules.settings import *
except Exception:
    print(f"\n\033[91mERROR ->\033[0m The 'config.ini' file was not found and a new one has been created, please run sevven again")
    sys.exit(1)

from modules.format_calls import *
from modules.backup_handler import make_project_backup
from modules.calcler import (convert_size, 
                             convert_time)
from modules.system_operations import copy_any
from modules.system_operations import get_terminal_columns
from modules.parser import parse_arguments
    
if COLOR_HIGHLIGHTING: from modules.colors import Colors
else: from modules.colors import NoColors as Colors
if SOUNDS and NOTIFICATION_AT_END: from modules.play_sounds import play



# Function that handles the call to the compression and decompression modules that format the content.
def control(file_format: str, main_content: str) -> str:
    '''
    ### Checkpoint
    Call to pack/unpack function depends of file FORMAT
    '''
    base_module = 'unpack' if args.d else 'pack'                          # Define the base module (pack or unpack)
    file_type = EXT_FUNCTIONS.get(file_format)                            # Get the module name correspondig to file format
    function_module = importlib.import_module(f'mainFunctions.{base_module}.{file_type}') # Importing the module dynamically using importlib
    function_to_call = getattr(function_module, 'init')                    # Get the module "init()" function
    
    # Building basic arguments
    kwargs = {'input_file': main_content}

    if args.d: # If unpacking, add an additional argument
        if args.indent and file_format in ALLOW_INDENT: kwargs['indent'] = args.indent
        if file_format in {'php', 'html'}: kwargs['tags'] = bool(not args.s) # If the file format is 'php' or 'html', pass another additional argument
    
    # Call to function with the correct arguments        
    formated_content = function_to_call(**kwargs) 
    
    return formated_content


def init() -> None:
    '''
    ### Initialize the app flow.
    Contain main functions, file or dir validations and first workflow.
    '''
    ######       FUNCTIONS      #######   
    #_________________________________# 
    def ERROR(str: str, debugID: str, start: str='') -> None:   # Function to handle errors
        nonlocal total_warnings
        if not DEBUG_MODE: debugID = ''
        else: total_warnings += 1
        WARNING(str=str, debugID=debugID, start=start) if recursively else FAIL(str=str, debugID=debugID, start=start)
    
    def FAIL(str: str, debugID: str, start: str='') -> None:    # This function is called when an error occurs and it is necessary to stop execution (code 1).
        if not DEBUG_MODE: debugID = ''
        if VERBOSITY_LEVEL > 0: print(f'{start}{Colors.FAIL}ERROR -> {Colors.END}{str}\t{Colors.FAIL}{debugID}{Colors.END}')
        sys.exit(1)
    
    def WARNING(str: str, debugID: str, start: str='') -> None: # This function is called when an error occurs but it is not necessary to stop execution 
        if not DEBUG_MODE: debugID = ''
        if VERBOSITY_LEVEL >= 4: print(f'{start}{Colors.WARNING}WARNING -> {Colors.END}{str}\t{Colors.WARNING}{debugID}{Colors.END}')
    
    def OUTLOG(str: str, vlevel: int = 10, debug: bool = False, start: str='') -> None:
        if (debug and DEBUG_MODE) or vlevel <= VERBOSITY_LEVEL: print(f'{start}{str}')
    
    def check_configurations() -> None:
        if CONFIGURATION_EXIST[0] == 'ERROR': FAIL(str=CONFIGURATION_EXIST[1], start='\n', debugID='F008') 
        elif DEBUG_MODE and CONFIGURATION_EXIST[0] == 'WARNING': WARNING(str=CONFIGURATION_EXIST[1], start='\n', debugID='W001')
        
        if CONF_JSON_EXIST[0] == 'ERROR': FAIL(str=CONF_JSON_EXIST[1], start='\n', debugID='F012') 
        elif DEBUG_MODE and CONF_JSON_EXIST[0] == 'WARNING': WARNING(str=CONF_JSON_EXIST[1], start='\n', debugID='W002')
        
        if not FIRST_CHECK and INTEGRITY_CONFIG_CHECK_FAIL: FAIL(str=INTEGRITY_CONFIG_CHECK_FAIL, start='\n', debugID='F011')
        
    def check_special_parameters() -> None:
        '''
        Control special parameters that cannot be interpreted after the others
        '''
        if args.C:
            try:
                from modules.configure_shell import init_configuration_shell
                init_configuration_shell()
                sys.exit(0)
            except Exception as e:
                FAIL(str=f'{str(e)}', start='\n', debugID='F009')
            except KeyboardInterrupt:
                FAIL(str='Aborted, changes were not saved', start='\n', debugID='F010') 
        
        elif args.update: 
            from modules.updater import check_update
            update_response = check_update()
            if update_response[0] == 'ERROR': ERROR(str=update_response[1], start='\n', debugID='E022')
            elif update_response[0] == 'OK': OUTLOG(str=update_response[1], vlevel=1, start='\n'); sys.exit(0)
            elif update_response[0] == 'COMPLETED': OUTLOG(str=f'{Colors.OKCYAN}UPDATE COMPLETE -> {Colors.END}{update_response[1]}', vlevel=1, start='\n'); sys.exit(0)

            
        
        elif args.version: from modules.help import VERSION_OUTPUT; print(VERSION_OUTPUT); sys.exit(0)
        
        elif args.reconfigure:
            try:
                from modules.backup_handler import restore_initial_config_backup
                restore_initial_config_backup()
                sys.exit(0)
            except Exception as e:
                FAIL(str=f'{str(e)}', start='\n', debugID='F014')
            except KeyboardInterrupt:
                FAIL(str='Aborted', start='\n', debugID='F015') 
        
        elif args.flush_backups:
            try:
                from modules.backup_handler import remove_all_backups
                remove_all_backups()
                sys.exit(0)
            except Exception as e:
                FAIL(str=f'{str(e)}', start='\n', debugID='F014')
            except KeyboardInterrupt:
                FAIL(str='Aborted', start='\n', debugID='F015') 
      
    def safe_content(file_name: str) -> str: # Returns the contents of the current input file :: (fix remove content on error)
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    
    def what_format(file: str) -> str:       # Try to identify the format of file content
        '''
        Returns the file FORMAT of **input_file**.\n
        ---
        - When the file FORMAT is specified (-f FORMAT), this function don't be called.\n
        > Recomended for recursively and multiple tasks (*executed on directories or a lot of files with the same FORMAT*). 
        '''
        try:
            file_type, _ = mimetypes.guess_type(file)
            if file_type: return file_type
            return 'invalid-format'
        except Exception as e:
            ERROR(str=str(e), debugID='E001')
            return 'invalid-format'
        
    def autodetect(file: str) -> str:
        '''
        #### This function handles file format detections
        - If no specific format was declared, the file extension is taken as the first choice. 
        - If it does not contain an extension, the what_format function is called to identify the format based on the content.
        '''
        step_format = what_format(file)
        if step_format == 'empty': ERROR(str=f'The file "{Colors.FILE}{input_file}{Colors.END} is empty', debugID='E002')
            
        if '.' in os.path.basename(input_file) and not os.path.basename(input_file).startswith('.') and not os.path.basename(input_file).endswith('.'):
            _, extension = os.path.splitext(input_file)
            file_format = extension.lower().strip(".")
            if file_format not in FORMAT_LIST: file_format = step_format
        else: file_format = step_format
        
        return file_format
    
    def save_file(output_file_filename: str, newcontent: str) -> None: # Save the new content of current file
        '''
        ### Save formated content
        \n
        When not specify the output filename,
        the initial file (**input_file**) will be overwrited
        with the new formated content in the next cases:
           - If it is a file
           - If it is a directory and `OVERWRITEDIR_LOCK` is disabled 
           - If an output is specified with `-o`
           - The parameter `-D` is present
        '''
        with open(os.path.abspath(output_file_filename), 'w', encoding='utf-8') as file:
            file.write(newcontent)
            
            
    # LOOP/NOLOOP 
    def launch(input_file: str, output_file: str) -> None:
        '''
        - This is the function that controls the flow of calls to the **control** function a certain number of times and then saves the file(s).
        
        ---
        > This function that will be executed as the last step on init function. 
        > When executed on a directory it will be executed in a '`for`' loop.
        ''' 
        nonlocal file_format, files_updated, total_warnings, size_after
        
        detect = autodetect(input_file).lstrip()
        # Handling the -f parameter input
        if args.format: file_format = args.format.lower().strip() # Manual set 
        else: file_format = detect                                # autodetect 
            
        if ' ' in file_format: file_format = file_format.split(' ')
        elif ',' in file_format: file_format = file_format.split(',')
        else: file_format = [file_format,]
        
        FMT_DETECTION = 'Extension: ' + str(file_format).upper().strip("[]'") if '/' not in file_format and 'invalid-format' not in file_format else 'Mime-type: ' + str(file_format).upper().strip("[]'")
        general_warning = ''
        skip_this_file = False
        
        for i in file_format:
            # Handling the -s parameter
            if args.s and i not in {'php', 'html'} and not SKIP_MISSARGS: general_warning += f'{Colors.WARNING}│{Colors.GRAY if VERBOSITY_LEVEL < 5 else ""} Warning:   The current format cannot contains <tags>{Colors.END}'; total_warnings += 1
            # Handling the -I parameter    
            if args.indent and i not in ALLOW_INDENT and not SKIP_MISSARGS: general_warning += f'{Colors.WARNING}│{Colors.GRAY if VERBOSITY_LEVEL < 5 else ""} Warning:   The indentation size not possible in this filetype{Colors.END}'; total_warnings += 1
            if i not in FORMAT_LIST: general_warning += f'{Colors.FAIL}│{Colors.GRAY if VERBOSITY_LEVEL < 5 else ""} Error:     This format not is avaliable or failed to autodetect{Colors.END}\n'; total_warnings += 1; skip_this_file = True
            if i in BETA_LIST and not BETA_LANGS: general_warning += f'{Colors.FAIL}│{Colors.GRAY if VERBOSITY_LEVEL < 5 else ""} Error:     "{str(i).upper()}" it is a beta language at this time, enable the {Colors.OKCYAN}Beta Languages{Colors.GRAY if VERBOSITY_LEVEL < 5 else ""} configuration with {Colors.ARG}-C{Colors.END}\n'; total_warnings += 1; skip_this_file = True
        
        if not skip_this_file:
            try:
                content = safe_content(input_file)
                if args.print:
                    formated_content = control(file_format=file_format[0], main_content=content) # Format the content
                    from modules.syntax_highlighter import highlight_code
                    output_code = highlight_code(code=formated_content, syntax=str(file_format[0]))
                    if not output_code: ERROR(str=f'The format is not correct, try specifying another one with {Colors.ARG}-f{Colors.END}', start='\n', debugID='E021')
                    else: print(output_code, '\n')
                    if args.output: save_file(output_file, formated_content) #!NOTE: Disable to debug if you wish

                
                else:
                    if any(f in detect for f in file_format):
                        formated_content = control(file_format=detect, main_content=content) # Format the content
                        save_file(output_file, formated_content) #!NOTE: Disable to debug if you wish 
                        size_after += os.path.getsize(os.path.abspath(output_file))
                        files_updated += 1 
                        OUTLOG(str=f'{Colors.OKCYAN}✓ {Colors.END}{os.path.basename(output_file)}', vlevel=3)
                        OUTLOG(str=f'{Colors.GRAY}│ {FMT_DETECTION}\n│ Path:      {input_file}{Colors.END}', debug=True)

            except Exception as e:
                OUTLOG(str=f'{Colors.FAIL}✕ {Colors.END}{os.path.basename(output_file)}', vlevel=4)
                ERROR(str=str(e), debugID='E003', start=f'{Colors.WARNING}│ {Colors.END}')
                if VERBOSITY_LEVEL >= 4:OUTLOG(str=f'{Colors.GRAY}│ {FMT_DETECTION}\n│ Path:      {input_file}{Colors.END}', debug=True)
        else:
            OUTLOG(str=f'{Colors.WARNING}✕ {Colors.END}{os.path.basename(output_file)}', vlevel=4)
            if VERBOSITY_LEVEL >= 4:
                if isdir: OUTLOG(str=f'{general_warning.strip()}\n{Colors.GRAY}│ {FMT_DETECTION}\n│ Path:      {input_file}{Colors.END}', debug=True)
            if not isdir: ERROR(str=general_warning.strip().replace('Warning:   ', '').replace('Error:     ', ''), debugID='E020')


    #---------------------- CHECK CONFIGURATION & SPECIAL PARAMETERS ------------------------#
    check_configurations() ; check_special_parameters()

    #----------------------------------- VARIABLES ------------------------------------------#
    input_file = os.path.abspath(args.input) # Current input file
    output_file= ''                          # Output file
    file_format = ''                         # Format of current file or filter on directories
    recursively =  False                     # Variable to check whether a loop will be executed or not.
    dir_count = 0                            # Counter for directories
    file_count = 0                           # Counter for files
    files_updated = 0                        # Counter for file updates
    total_warnings = 0                       # Warnings ocurred while running on directory mode
    
    
    #------------------------- MAIN VERIFICATION BEFORE EXECUTION ---------------------------#  
    try: # Check if it is a file or directory
        if not os.path.exists(input_file): ERROR(str=f"The file {Colors.FILE}{input_file}{Colors.END} does not exist !", debugID='E006', start='\n')
        
        if os.path.isdir(input_file):        # Handling the -D/-o parameters if necessary, and OVERWRITEDIR_LOCK (on config.ini)
            isdir = True
            if not args.D and not args.output:                           
                if OVERWRITEDIR_LOCK: ERROR(str=f'{Colors.FILE}{input_file}{Colors.END} is a directory. Change the {Colors.OKCYAN}Directory Overwrite Lock{Colors.END} flag or specify ({Colors.ARG}-o{Colors.END} or {Colors.ARG}-D{Colors.END})\t\t', debugID='E007', start='\n')
                # If OVERWRITEDIR_LOCK is enabled, directories will be overwritten
            # If -D is added or specify an output with -o, directories will be overwritten
            
            if not args.output: output_file = os.path.abspath(input_file)
            else: output_file = os.path.abspath(args.output)
            
            recursively = True
        else:
            if args.D and not SKIP_MISSARGS: ERROR(str=f'The {Colors.ARG}-D{Colors.END} parameter only be necessary with directories.\n\t To avoid this type of errors turn ON the flag {Colors.OKCYAN}Skip Invalid Parameters{Colors.END} on the config mode {Colors.ARG}-C{Colors.END}', debugID='E008', start='\n')
            output_file = os.path.abspath(input_file)
            isdir = False

    except OSError as e:
        ERROR(str=str(e), debugID='E009', start='\n')
    except Exception as e:
        ERROR(str=str(e), debugID='E010', start='\n')      
    
    if args.s and not args.d: # Handling -s parameter 
        if not SKIP_MISSARGS: FAIL(str=f'The {Colors.ARG}-s{Colors.END} parameter cannot add on compress method\n\t\tYou can skip this type of checks by enabling the {Colors.OKCYAN}Skip Invalid Parameters{Colors.END} flag', debugID='F001', start='\n')
    
    time_before = time.time()
    
    from alive_progress import alive_bar
    error_while_running = False         # It will indicate if there was an error during execution, and thus play an error or success sound.
    
    if isdir:                           # Determine whether the launch() function is executed in a loop or not.
        if args.print and not SKIP_MISSARGS: FAIL(str=f'The {Colors.ARG}-p{Colors.END} parameter can only be used on files',  start='\n', debugID='F013')
        
        try:
            size_before = 0
            size_after = 0
            print('\r')
            with alive_bar(title=f'◂{Colors.FAIL}FORMATTING{Colors.END}▸' if args.d else f'▸{Colors.OKCYAN}COMPACTING{Colors.END}◂',
                           bar=None, 
                           spinner='waves2', 
                           spinner_length=get_terminal_columns() - 46, 
                           max_cols=get_terminal_columns(), 
                           disable=not SHOW_PROGRESSBAR, 
                           elapsed='files in', 
                           enrich_print=False, 
                           receipt=False) as bar:
            
                try: 
                    make_project_backup(input_project=os.path.abspath(input_file), 
                                        make_backups=MAKE_PROJECT_BACKUPS,
                                        maximum_backups=MAX_BACKUPS)
                except OSError as e:
                    FAIL(str=f'Trying to create a backup: {str(e)}', debugID='F002', start='\n')
                except Exception as e:
                    FAIL(str=f'Trying to create a backup: {str(e)}', debugID='F003', start='\n')
                except KeyboardInterrupt as e:
                    FAIL(str=f'Trying to create a backup: {str(e)}', debugID='F004', start='\n')
                    
                try:
                    copy_any(input=os.path.abspath(input_file), 
                            output=os.path.abspath(output_file))
                except OSError as e:
                    FAIL(str=str(e), debugID='F005', start='\n')
                except Exception as e:
                    FAIL(str=str(e), debugID='F006', start='\n')
                except KeyboardInterrupt as e:
                    FAIL(str=str(e), debugID='F007', start='\n')

                
                
                if USE_THREADS or args.threads:
                    import concurrent.futures, threading, signal
                    stop_event = threading.Event()

                    def signal_handler(sig, frame):
                        ERROR(str="Interrupt received. Aborting...", start='\n', debugID='E013')
                        stop_event.set()
                        sys.exit(0)
                        
                    signal.signal(signal.SIGINT, signal_handler)

                    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS if not args.threads else args.threads) as executor:
                        futures = []
                        
                        for root, dirs, files in os.walk(os.path.abspath(output_file)):
                            dir_count += len(dirs)
                            for file in files: 
                                if stop_event.is_set():
                                    break
                                
                                input_file = file # Is necesary define the input file to update the file in launch function and warnings (ERROR functions)
                                size_before += os.path.getsize(os.path.abspath(os.path.join(root, file)))
                                futures.append(executor.submit(launch, os.path.abspath(os.path.join(root, file)), os.path.abspath(os.path.join(root, file))))
                                file_count += 1
                                bar()
                                
                        concurrent.futures.wait(futures) # Wait for tasks to finish
                
                else:
                    for root, dirs, files in os.walk(os.path.abspath(output_file)):
                        dir_count += len(dirs)
                        for file in files: 
                            input_file = file # Is necesary define the input file to update the file in launch function and warnings (ERROR functions)
                            size_before += os.path.getsize(os.path.abspath(os.path.join(root, file)))
                            launch(input_file=os.path.abspath(os.path.join(root, file)), 
                                output_file=os.path.abspath(os.path.join(root, file)))
                            #size_after += os.path.getsize(os.path.abspath(os.path.join(root, file)))
                            file_count += 1
                            bar()
                    
        except KeyboardInterrupt:
            error_while_running = True; ERROR(str='Aborted', start='\n', debugID='E014')
        except OSError as e:
            error_while_running = True; ERROR(str=str(e), debugID='E015', start='\n')
        except Exception as e:
            error_while_running = True; ERROR(str=str(e), debugID='E016', start='\n')
        finally:
            OUTLOG(f'''

{Colors.OKCYAN} │ Elapsed time:{Colors.END}   {convert_time(time.time() - time_before) if VERBOSITY_LEVEL >= 4 else ''}
{Colors.OKCYAN} │ Total warnings:{Colors.END} {total_warnings}
{Colors.OKCYAN} │ Directories:{Colors.END}    {dir_count}
{Colors.OKCYAN} │ Total files:{Colors.END}    {file_count}
{Colors.OKCYAN} │ Files updated:{Colors.END}  {files_updated}
''', vlevel=4)
                        
            OUTLOG(F'''
{Colors.OKCYAN} │ Size updates:{Colors.END}   {convert_size(size_before)} {f"{Colors.FAIL}<{Colors.END}" if size_before < size_after else f"{Colors.OKCYAN}>{Colors.END}"} {convert_size(size_after)}
''', vlevel=2)
            
            if SOUNDS and NOTIFICATION_AT_END and int(time.time() - time_before) >= ENABLE_NOTIFY_AFTER:
                #notify(sound=error_while_running, number=ERROR_NOTIFICATION if error_while_running else SUCCESS_NOTIFICATION)
                play(sound='error' if error_while_running else 'success', 
                     index=ERROR_NOTIFICATION if error_while_running else SUCCESS_NOTIFICATION)
                                    ####  END FINALLY ###
    
    else: # if is a file
        if args.threads and not SKIP_MISSARGS: ERROR(str='Threads cannot be applied to a single file', start='\n', debugID='E012')
        
        size_before = 0
        size_after = 0
        
        print('\r')
        with alive_bar(title=f'◂{Colors.FAIL}FORMATTING{Colors.END}▸' if args.d else f'▸{Colors.OKCYAN}COMPACTING{Colors.END}◂',
                        bar=None, 
                        spinner='waves2', 
                        spinner_length=get_terminal_columns() - 46, 
                        max_cols=get_terminal_columns(), 
                        disable=not SHOW_PROGRESSBAR, 
                        elapsed='files in', 
                        enrich_print=False, 
                        receipt=False) as bar:
            try:
                make_project_backup(input_project=os.path.abspath(input_file), 
                                    make_backups=MAKE_PROJECT_BACKUPS,
                                    maximum_backups=MAX_BACKUPS)
            except Exception as e:
                ERROR(str=f'Trying to create a backup: {str(e)}', start='\n', debugID='E004')
            except OSError as e:
                ERROR(str=f'Trying to create a backup: {str(e)}', start='\n', debugID='E005')
            
            try:
                size_before = os.path.getsize(input_file)
                launch(input_file=os.path.abspath(input_file), output_file=os.path.abspath(output_file))
                size_after = os.path.getsize(output_file)
                bar()
            except KeyboardInterrupt:    
                error_while_running = True; ERROR(str='Aborted', start='\n', debugID='E017')
            except OSError as e:
                error_while_running = True; ERROR(str=str(e), debugID='E018', start='\n')
            except Exception as e:
                error_while_running = True; ERROR(str=str(e), debugID='E019', start='\n')
            finally:
                if not args.print: OUTLOG(F'''
    {Colors.OKCYAN} │ Size updates:{Colors.END}   {convert_size(size_before)} {f"{Colors.FAIL}<{Colors.END}" if size_before < size_after else f"{Colors.OKCYAN}>{Colors.END}"} {convert_size(size_after)}
    ''', vlevel=2)
                
                if SOUNDS and NOTIFICATION_AT_END and int(time.time() - time_before) >= ENABLE_NOTIFY_AFTER:
                    play(sound='error' if error_while_running else 'success', 
                        index=ERROR_NOTIFICATION if error_while_running else SUCCESS_NOTIFICATION)
# MAIN APP EXECUTION
if __name__ == "__main__":
    args = parse_arguments()
    init()
    
#! NOTES for DEVELOPERS:
'''  > Errors in modules should not be captured from within the modules themselves, 
       but rather in the main script using the ERROR, FAIL or WARNING functionS so 
       that the output maintains the same structure and the DEBUG is more correct
       and understandable.

'''    
    
'''
    #! NOTAS PARA HOY:
    arreglar lo del deno y deno.exe
    
    añadir al man en linux
    añadir opcion para eliminar comentarios
    añadir opcion para eliminar saltos de linea excesivos
    añadir en la funcion pack, compactar todo menos -s css style js javascript script
    añadir opción para ofuscar codigo // tambien en base a una contraseña dada o semilla unica
     #contar los archivos y demass, con barras de progresso; avisar de no parar el programa.
              
    seguir estableciendo los errores
    
    Comprobar los nombres de cada archivo devueltos por whatformat
    averiguar sobre los formatos de chatgpt
    poner varias extensiones de entrada
        arreglar si se introduce una extension solo tocará esos archivos

    
    _______________________________________________________________________________________________________
    
    
 
    
    añadir tipos de archivos (comprobar todos los tipos de extensiones)
    en la actualizacion no modificar fichero personal
    archivo de configuracion y argumentos
    mostrar el tamaño de antes -> despues (mostrar en carpetas archivos separados)
    archivo de configuracion y variables
    configurar pyenv e intalaciones con script
    configurar ejecutador y path
    cambiar a CONSTANTES
    cambiar idioma/comentarios
    
    OPTIONS:
        OVERWRITEDIR_LOCK           BOOL
        DEBUG_MODE BOOL
        VERBOSITY_LEVEL          INT
            size info diff   1
            warnings         2
            name-per-done    3
            scheme/quantity  4
        HIGHLIGHT_COLORS         
        
    '''
