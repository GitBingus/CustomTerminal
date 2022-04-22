# GitBingus CLI main program
# Check the GitHub page for more information

try:
    import os, platform, winapps, math, psutil, sys, webbrowser, GPUtil, cpuinfo # attempts to import libraries
    import datetime as dt # attempts to import libraries
except:
    import os
    os.system('pip install platform && pip install traceback && pip install winapps && pip install datetime') # if it cannot find libraries, it will install them via pip
    import platform, winapps, math, psutil, sys
    import datetime as dt

appDict ={ # a dictionary of .appx apps for app search
            '3D Builder':'com.microsoft.builder3d:',
            '3D Viewer':'com.microsoft.3dviewer:',
            'Action Center':'ms-actioncenter:',
            'Alarms & Clock':'ms-clock:',
            'Available Networks':'ms-availablenetworks:',
            'Calculator':'calculator:',
            'Calendar':'outlookcal:',
            'Camera':'microsoft.windows.camera:',
            'Candy Crush Soda Saga':'candycrushsodasaga:',
            'Connect':'ms-projection:',
            'Cortana':'ms-cortana:',
            'Cortana Connected Services':'ms-cortana://notebook/?ConnectedServices:',
            'Cortana Personal Information':'ms-cortana://settings/ManageBingProfile:',
            'Device Discovery':'ms-settings-connectabledevices:devicediscovery:',
            'Drawboard PDF':'drawboardpdf:',
            'Facebook':'fb:',
            'Feedback Hub':'feedback-hub:',
            'Get Help':'ms-contact-support:',
            'Groove Music':'mswindowsmusic:',
            'Mail':'outlookmail:',
            'Maps':'bingmaps:',
            'Messaging':'ms-chat:',
            'Microsoft Edge':'microsoft-edge:',
            'Microsoft News':'bingnews:',
            'Microsoft Solitaire Collection':'xboxliveapp-1297287741:',
            'Microsoft Store':'ms-windows-store:',
            'Microsoft Store - Music':'microsoftmusic:',
            'Microsoft Store - Movies & TV':'microsoftvideo:',
            'Microsoft Whiteboard':'ms-whiteboard-cmd:',
            'Minecraft Windows 10 Edition':'minecraft:',
            'Mixed Reality Camera':'ms-holocamera:',
            'Mixed Reality Portal':'ms-holographicfirstrun:',
            'Movies & TV':'mswindowsvideo:',
            'Networks':'ms-availablenetworks:',
            'OneNote':'onenote:',
            'Paint 3D':'ms-paint:',
            'People':'ms-people:',
            'People - Settings':'ms-people:settings',
            'Photos':'ms-photos:',
            'Project Display':'ms-settings-displays-topology:projection',
            'Screen Snip':'ms-screenclip:',
            'Settings':'ms-settings:',
            'Snip & Sketch':'ms-ScreenSketch:',
            'Spotify':'%appdata%\\Spotify\\Spotify.exe',
            'Steam':'%programfilesx86%\\Steam\\Steam.exe',
            'Tips':'ms-get-started:',
            'Twitter':'twitter:',
            'Weather':'bingweather:',
            'Windows Mixed Reality Environments':'ms-environment-builder:',
            'Windows Parental Controls':'ms-wpc:',
            'Windows Security':'windowsdefender:',
            'Xbox':'xbox:',
            'Xbox - Friends list':'xbox-friendfinder:',
            'Xbox - Profile page':'xbox-profile:',
            'Xbox - Network settings':'xbox-network:',
            'Xbox - Settings':'xbox-settings:',
            'Xbox One SmartGlass':'smartglass'
}

appDict = {k.lower(): v for k, v in appDict.items()} # makes every key and value lower case for easier search

def bytestoint(bytes, suffix='B'):
    factor = 1024 # 1024 bytes in 1KB, 1024KB in 1MB, etc
    for unit in ["", "K", "M", "G", "T", "P"]: # Byte, KiloByte, Megabyte etc -- Petabyte
        if bytes < factor: # checks to see if the bytes needs to be formatted or not and what too
            return f"{bytes:.2f}{unit}{suffix}" # returns formatted number with unit
        bytes /= factor # divides bytes by factor on every iteration until bytes < factor

def search_filter(app): # filters web apps and local apps
    appOG = app
    app = appDict[app]
    try:
        if not '\\' in app: # if the value found from app entered is not a file
            webbrowser.open(app) # open the web app in the default browser
        else:
            for key, value in sorted(os.environ.items()):
                if '\\' in value:
                    print(f"{key} : {value}")
                    
    except KeyError:
        raise KeyError("The app you have entered does not exist. ") # if the app is not in the dictionary it raises an exception
    finally:
        run() # restarts app


def delete(splitOutput): # main function for deleting files
    if not splitOutput[1:]: # if no file is specified
        print('No file is specified. For help with delete, enter "help delete"')
        run() # restarts app
    else: # if there is a specified file
        try:
            if os.path.exists(splitOutput[1]) == True: # if the file exists
                os.remove(splitOutput[1]) # removes specified file
                run() # restarts app
            else: # if the file does not exist
                print('The file you have specified does not exist. Check the file name and path. ') # throws error
                run() # restarts app
        except Exception as delError: # if it fails to delete
            raise Exception(f'Failed to delete file. Reason: {delError}') # raises exception
        finally:
            run() # restarts app

def write(splitOutput, file, text): # main function for writing to files
    try:
        if not splitOutput[1:]: # if no file is specified
            print('No file is specified. For help with delete, enter "help delete"')
            run() # restarts app
        else:
            name, ext = splitOutput[1].split('.') # splits out the name and extension of file specified
            file = open(name+'.'+ext, 'w') # opens the file with write permissions
            file.write(' '.join(text)) # writes to file
            file.close() # closes file
    except Exception as writeError:
            raise Exception(f'Failed to write to file. Reason: {writeError}') # raises exception if it cannot write
    finally:
        run() # restarts app

def mkfile(splitOutput, defaultPath = os.getcwd()): # main function for making files 
    if not splitOutput[1:]: # if no file name is specified
        print('No file name is specified. For help with mkfile, enter "help mkfile"')
        run() # restarts app
    else:
        try:
            name, ext = splitOutput[1].split('.') # splits out the name and extension of file name specified
            
            if os.path.exists(name+'.'+ext):
                print(f'File {name}.{ext} already exists. Overwriting existing file...')
            
            if defaultPath == os.getcwd():
                print('No folder specified. Using current working directory')
                mkfile = open(name+'.'+ext,'w+') # creates file
            else:
                mkfile = open(defaultPath+'\\'+name+'.'+ext, 'w+')
                
            mkfile.close() # closes file 
            if splitOutput[2] == 'write': # if the user has entered write after entering file
                if not splitOutput[3:]:
                    print('No write argument specified. Will not write anything to file')
                    run()
                else:
                    write(splitOutput, name+'.'+ext, splitOutput[3:]) # executes write function with the required data
                    run() # restarts app
        except Exception as mkfileError:
            raise Exception(f"Failed to make file. Reason: {mkfileError}") # raises exception
        finally:
            run() # restarts app

def mkdir(splitOutput): # main function for making directories
    if not splitOutput[1:]: # if no dir is specified
        print('No path specified. For help with mkdir, enter "help mkdir"')
        run() # restarts app
    else:
        mkdir = splitOutput[1] # creates variable comtaining dir name
        
    try:
        if not os.path.exists(mkdir): # if dir does not exist
            os.makedirs(mkdir) # makes directory
            
    except Exception as mkdirError:
        raise Exception('An exception has occured: %s' % mkdirError) # raises exception
        
    finally:
        run() # restarts app

def chdir(splitOutput): # main function for changing directory, similar to cd in Windows
    splitOutput[1] = splitOutput[1]+'\\' # adds backslash to end of file name
    try:
        if splitOutput[1].replace('\\','').upper() in os.environ: # if dir specified is an environment variable
            os.chdir(os.getenv(splitOutput[1].replace('\\','').upper())) # changes directory to environment variable
            run() # restarts app
        else:
            if splitOutput[1] == '..': # .. is to go back in the dir tree
                os.chdir('..') # changes directory
                os.path.abspath(os.curdir) # returns path
            else:
                os.chdir(splitOutput[1].capitalize()) # changes path to what is specified
    except Exception as chdirError:
        if type(chdirError) == KeyError: # if the error is a keyerror
            pass
        elif type(chdirError) == FileNotFoundError: # if the file specified for chdir does not exist
            raise FileNotFoundError(f'The directory {splitOutput[1].capitalize()} does not exist.') # raise exception
            
    finally:
        run() # restarts app

def list(splitOutput): # main function for listing specified items
    import win32api # imports win32api for listing physical media and volumes
    components = ["cpu","memory","baseboard","system","gpu"]
    try:
        if not splitOutput[1:] or splitOutput[1] == '*': # if nothing specified
            print('\nDirectory of {}:\n'.format(os.getcwd())) # prints current working directory
            root = os.getcwd() # sets var root to cwd
            root = os.fsencode(root) # encodes root to file system encoding
            for path, subdirs, files in os.walk(root): # for every path, sub directories and files in the current directory
                for name in files: # for all names in files
                    try:
                        print(os.path.join(path.decode('latin-1'),name.decode('latin-1'))) # decodes joined path as latin-1
                    except KeyboardInterrupt: # if user pressed ctrl+c (KeyboardInterrupt)
                        raise KeyboardInterrupt('\nSuccessfully stopped listing.\n') # raises exception, but not crucial
                    finally:
                        run() # restarts app
                
        elif splitOutput[1] == 'vol': # if the user wants volumes specified
            if not splitOutput[2:]: # if no specific volume is specifed
                drives = str(win32api.GetLogicalDriveStrings()) # makes var which stores raw disk data from the win32api library
                drives = drives.split('\000')[:-1] # splits them to a human-readable format
                for drive in drives: # for every drive in the list (drive = volume)
                    driveSize = psutil.disk_usage(drive) # gets raw disk (volume) storage data
                    driveTotal = int(driveSize.total) // (1024**3) # converts to GiB
                    driveUsed = int(driveSize.used) // (1024**2) # converts to MiB
                    driveFree = int(driveSize.free) // (1024**3) # converts to GiB
                    print("Data for volume {:<}: Total: {:^}GiB, Used: {:^}MiB, Free: {:^}GiB".format(drive, driveTotal, driveUsed, driveFree)) # prints data for all detected volumes
            else:
                if type(splitOutput[2]) == str: # if a specific volume is specified
                    try:
                        drive = str(splitOutput[2]).lower().replace(splitOutput[2][1:],'') # makes var called drive which stores a formatted drive string
                        drive = drive+":\\" # appends a backslash to the drive variable
                        originalDrive = drive # creates backup of drive name to print later
                        drive = psutil.disk_usage(drive) # gets disk storage data
                        driveTotal = int(drive.total) // (1024**3) # converts to GiB
                        driveUsed = int(drive.used) // (1024**2) # converts to MiB
                        driveFree = int(drive.free) // (1024**3) # converts to GiB
                        print("Data for volume {}: Total: {}GiB, Used: {}MiB, Free: {}GiB".format(originalDrive.capitalize(), driveTotal, driveUsed, driveFree)) # prints volume data
                    except Exception as lsDrvError:
                        if type(lsDrvError) == FileNotFoundError: # if the volume specified does not exist
                            raise FileNotFoundError('The volume, {}, you have selected does not exist. '.format(originalDrive)) # raise exception
                        else: # if unknown error
                            raise Exception(lsDrvError) # raises exception
                    finally:
                        run() # restarts app
        
        elif os.path.exists(os.getcwd()+'\\'+splitOutput[1]): # if user wants all files in a specific dir listed
            print('\nDirectory of {}:\n'.format(os.getcwd()+'\\'+splitOutput[1])) # prints formatted string containing current working directory
            root = os.getcwd() # makes var called root which contains cwd
            root = os.fsencode(root) # encodes root using file system encoding
            for path, subdirs, files in os.walk(root): # for every path, subdirectory and file in the directory specified
                for name in files: # for every name of every file in directory
                    try:
                        print(os.path.join(path.decode('latin-1'),name.decode('latin-1'))) # decodes encoded binary to human-readable format
                    except KeyboardInterrupt:
                        raise KeyboardInterrupt('\nSuccessfully stopped listing.\n') # stops listing if ctrl+c (KeyboardInterrupt) is entered while listing
                    finally:
                        run() # restarts app
                        
        elif splitOutput[1] in components:
            print('Listing (specific) components (data) will take a while. Press ctrl+c to terminate the program if uncertain')
            cpu = {
                'Name' : cpuinfo.get_cpu_info()['brand_raw'], # gets cpu name
                'VID' : platform.processor(), # gets vendor id
                'Architecture' : cpuinfo.get_cpu_info()['arch'], # gets processor architecture
                'xArchitecture' : cpuinfo.get_cpu_info()['bits'], # gets xXX architecture
                'FreqHz' : cpuinfo.get_cpu_info()['hz_actual'][0], # gets frequency in Hz
                'FreqGHz' : cpuinfo.get_cpu_info()['hz_actual_friendly'], # gets frequency in GHz
                'PhysCores' : psutil.cpu_count(logical=False), # gets physical cores
                'LogCores' : psutil.cpu_count(logical=True), # gets logical cores (threads)
                'L2Cache' : int(str(cpuinfo.get_cpu_info()['l2_cache_size']).removesuffix("MiB")) // 1024, # gets L2 cache
                'L3Cache' : int(str(cpuinfo.get_cpu_info()['l3_cache_size']).removesuffix("MiB")) // 1024 # gets L3 cache
            }
            
            mem = {
                'Total' : bytestoint(psutil.virtual_memory().total),
                'Available' : bytestoint(psutil.virtual_memory().available),
                'Used' : bytestoint(psutil.virtual_memory().used),
                'Percent' : psutil.virtual_memory().percent,
                'TotalSwap' : bytestoint(psutil.swap_memory().total),
                'FreeSwap' : bytestoint(psutil.swap_memory().free),
                'UsedSwap' : bytestoint(psutil.swap_memory().used),
                'SwapPercentage' : psutil.swap_memory().percent
            }
            
            mobo = {
                'Manufacturer' : os.popen("wmic baseboard get Manufacturer").read().split('\n')[2], # gets manufacturer for motherboard
                'Product' : os.popen("wmic baseboard get product").read().split('\n')[2], # gets product name 
                'SerialNumber' : os.popen("wmic baseboard get serialnumber").read().split('\n')[2], # gets serial number
                'Version' : os.popen("wmic baseboard get version").read().split('\n')[2] # gets version
            }
            
            OS = {
                'OSName' : platform.uname().system,
                'Version' : platform.uname().version,
                'OSArch' : cpuinfo.get_cpu_info()['arch']
            }
            
            gpus = GPUtil.getGPUs()
            
            global GPUID, GPUName, CurrentGPULoad, FreeGPUMemory, UsedGPUMemory, TotalGPUMemory, CurrentGPUTemperature, GPUUUID
            
            for gpu in gpus:
                GPUID = gpu.id
                GPUName = gpu.name
                CurrentGPULoad = gpu.load*100
                FreeGPUMemory = gpu.memoryFree
                UsedGPUMemory = gpu.memoryUsed
                TotalGPUMemory = gpu.memoryTotal
                CurrentGPUTemperature = gpu.temperature
                GPUUUID = gpu.uuid
            
            gpu = {
                'ID' : GPUID,
                'Name' : GPUName,
                'Load' : CurrentGPULoad,
                'FreeMem' : FreeGPUMemory,
                'UsedMem' : UsedGPUMemory,
                'TotalMem' : TotalGPUMemory,
                'Temp' : CurrentGPUTemperature,
                'UUID' : GPUUUID,
            }
            
            which = splitOutput[1:]
            if which[0] in components:
                try:
                    if which[1]:
                        cpu = {x.lower(): v for x, v in cpu.items()}
                        mem = {x.lower(): v for x, v in mem.items()}
                        mobo = {x.lower(): v for x, v in mobo.items()}
                        OS = {x.lower(): v for x, v in OS.items()}
                        gpu = {x.lower(): v for x, v in gpu.items()}
                            
                        if which[0] == 'cpu':
                            print(cpu.get(which[1]))
                        elif which[0] == 'memory':
                            print(mem.get(which[1]))
                        elif which[0] == 'baseboard':
                            print(mobo.get(which[1]))
                        elif which[0] == 'system':
                            print(OS.get(which[1]))
                        elif which[0] == 'gpu':
                            print(gpu.get(which[1]))
                        else:
                            print('Key specified does not exist. ')
                except:  
                    if which[0] == components[0]:
                        for k, v in cpu.items():
                            print(f"{k} : {v}")
                        
                    elif which[0] == components[1]:
                        for k, v in mem.items():
                            print(f"{k} : {v}")
                                        
                    elif which[0] == components[2]:
                        for k, v in mobo.items():
                            print(f"{k} : {v}")
                                        
                    elif which[0] == components[3]:
                        for k, v in OS.items():
                            print(f"{k} : {v}")
                                        
                    elif which[0] == components[4]:
                        for k, v in gpu.items():
                            print(f"{k} : {v}")
            else:
                print("Not in list. ")
        
        else:
            print('Not a valid "list" command. For help, type "help list"') # if no valid command is entered
    except Exception as lsError:
        raise Exception(f'An exception has occured: {lsError}') # raises exception
    finally:
        run() # restarts app
    
def version(): # returns version
    Version = ( 
    """
       Terminal: By George Dawson - Version 1.0
    """
    )
    return Version, run() # restarts app
    
def advancedHelp(command): # prints advanced help for all commands that apply
    command = command.lower() # converts to lower case
    if command == 'calc': # returns data for calc
        print('''
                The "calc" command calculates a mathematic equation. You can enter "calc 1+1", and it will calculate "1+1".
                If you just enter "calc", it will prompt for a calculation to solve.
                For advanced maths, you can enter the abbreviated version of the function. For example, for square root, you would use "sqrt".
                For "sine", you would use "sin", etc. 
                Below is a list of available commands
                 
                Method	            Description                                                Valid input
                acos	            Calculates the arc cosine of a number                      acos n
                acosh	            Calculates the inverse hyperbolic cosine of a number       acosh n
                asin	            Calculates the arc sine of a number                        asin n
                asinh	            Calculates the inverse hyperbolic sine of a number         asinh n
                atan	            Calculates the arc tangent of a number in radians          atan n    
                atanh	            Calculates the inverse hyperbolic tangent of a number      atanh n
                cos	                Calculates the cosine of a number                          cos n
                cosh	            Calculates the hyperbolic cosine of a number               cosh n
                factorial	        Calculates the factorial of a number                       fact n
                hypot	            Calculates the Euclidean norm                              hypot n
                pow	                Calculates the value of x to the power of y                pow n
                sin	                Calculates the sine of a number                            sin n
                sinh	            Calculates the hyperbolic sine of a number                 sinh n
                sqrt	            Calculates the square root of a number                     sqrt n
                tan	                Calculates the tangent of a number                         tan n
                tanh	            Calculates the hyperbolic tangent of a number              tanh n
                
                (n = number)
            ''')
    elif command == 'time': # returns data for time
        print('''
                The 'time' command retrieves the current time based on your timezone. Time is formatted in 24hr time.
                
                Example             Usage               Description
                
                Time                                    Displays time according to your time zone
              ''')
    elif command == 'date': # returns data for date
        print('''
                The 'date' command retrieves the current date based on your timezone. Date is formatted in MM/DD/YY
                
                Example             Usage               Description
                
                Date                                    Displays date according to your location
              ''')
    elif command == 'program': # returns data for program
        print('''
                When you enter the name of a program, such as Chrome, the app will search through Microsoft's local app database, and attempts 
                to executes the app that matches the name of the app you have entered. 
                For an app with symbols, such as 7-Zip, you must include the symbol or it will fail to execute.
                If it fails to execute, you could try to make sure the app is installed in the first place. 
                If you have verified it is installed and is still not working, make sure the app is added to PATH.
                You can do this by typing "edit the system environment variables", and clicking "environment variables". Then, add the file or folder to the "path" subcatagory.
              ''')
        
    elif command == 'list': # returns data for list
        print('''
                The 'list' command lists everything specified after entering 'list'.
                
                Example             Usage               Description
                
                List                                    If no usage is specified, it will display all files and folders in the current directory.
                
                Vol                 list vol [letter]   Displays data about selected volume. If no volume is selected, it will display all detected volumes
                Part                list part [number]  Displays data about partitions. If no partition is selected, it will display all partitions detected
                
                *Storage is measured in Gibibytes or Mebibytes, which is 1.024% larger than a Gigabyte or Megabyte
              ''')
        
    elif command == 'chdir': # returns data for chdir
        print('''
                The 'chdir' command changes the current working directory (CWD) that the app is running on. By default, the CWD is wherever the app is installed, and resets every time the app is run.
                To change the directory to an environment variable such as %localappdata%, enter 'chdir', followed by which environment variable you want to go to, without the percent symbols.
                
                Example             Usage               Description
                
                chdir %env%            chdir env              Executes changing the directory to an existing environment variable. For a list of environment variables, visit https://pureinfotech.com/list-environment-variables-windows-10
                
              ''')
        
    elif command == 'mkdir': # returns data for mkdir
        print('''
                The 'mkdir' command makes a directory if the directory specified does not already exist.
                
                Example             Usage               Description
                
                mkdir               path or env var     Makes a directory if the directory specified does not already exist. Environment variables are also supported, but you cannot change them.
              ''')

    elif command == 'mkfile': # returns data for mkfile
        print('''
                The 'mkfile' command makes a file if the file specified does not already exist. After the file has been specified, the 'write' command can write the subsequent data to the file.
                
                Example                             Usage                               Description
                
                mkfile                              file name                           Creates a file if it does not already exist
                mkfile [file name] write [text]     mkfile file name write text         Creates a file if it does not already exist, and then writes the text specified
              ''')
    
    else:
        print('Not a command. For a list of available commands, enter "help"') # if not a valid help command
        run() # restarts app

def calculatorSliced(calc): # processes and calculates input from sliced input
    ans = ''.join(calc) # joins slices to string
    print('The answer to {} is {}.'.format(ans,str(eval(ans)))) # processes and returns answer
    run() # restarts app

def calculatorNormal(splitOutput): # processes and calculates input from input and contains complex inputs
    global answer # sets answer to global
    calc = input('Enter a calculation: ') # user input
    splitOutput = calc.split()[0:] # splits input to precess
    if len(splitOutput) == 0: # if no kwarg is entered
        calculatorNormal(splitOutput = None) # restarts function as splitOutput is None
    
    if splitOutput != None: # from here the function uses math library to calculate complex maths
        if splitOutput[0] == 'acos':
                answer = math.acos(math.radians(float(splitOutput[1])))
            
        elif splitOutput[0] == 'acosh':
                answer = math.acosh(math.radians(float(splitOutput[1])))
            
        elif splitOutput[0] == 'asin':
                answer = math.asin(math.radians(float(splitOutput[1])))
            
        elif splitOutput[0] == 'asinh':
                answer = math.asinh(math.radians(float(splitOutput[1])))
            
        elif splitOutput[0] == 'atan':
                answer = math.atan(math.radians(float(splitOutput[1])))
            
        elif splitOutput[0] == 'atanh':
                answer = math.atanh(math.radians(float(splitOutput[1])))
            
        elif splitOutput[0] == 'cos':
                answer = math.cos(math.radians(float(splitOutput[1])))
            
        elif splitOutput[0] == 'cosh':
                answer = math.cosh(math.radians(float(splitOutput[1])))
            
        elif splitOutput[0] == 'fact':
                answer = math.factorial(int(splitOutput[1]))
            
        elif splitOutput[0] == 'hypot':
                answer = math.hypot(float(splitOutput[1]))
            
        elif splitOutput[0] == 'pow':
                answer = math.pow(float(splitOutput[1]))
            
        elif splitOutput[0] == 'sin':
                answer = math.sin(math.radians(float(splitOutput[1])))
            
        elif splitOutput[0] == 'sinh':
                answer = math.sinh(math.radians(float(splitOutput[1])))
            
        elif splitOutput[0] == 'sqrt':
                answer = math.sqrt(float(splitOutput[1]))
            
        elif splitOutput[0] == 'tan':
                answer = math.tan(math.radians(float(splitOutput[1])))
            
        elif splitOutput[0] == 'tanh':
                answer = math.tanh(math.radians(float(splitOutput[1])))
                
        else:
            print("The answer to {} is {}.".format(calc, str(eval(calc)))) # formats and prints answer if no complex input was given but splitOutput was not None
            run() # restarts app
                
        print('The answer to "{} {}" is {}'.format(splitOutput[0],splitOutput[1],answer)) # formats and prints answer
        run() # restarts app
    
    else:
        print("The answer to {} is {}.".format(calc, str(eval(calc)))) # formats and prints answer if no complex input was given
        run() # restarts app

def help(outsideAccess = False): # main simple help function
    global commands 
    commands = (
    """
       Help:

       Commands:                           Usage:                                 Description:

       Help:*                                                                     Displays this screen
       Version:*                           terminal --version, -v                 Displays current version of application 
       Calc:                               [optional(calculation)]                Calculates a mathematical equation. If no calculation is entered after calc, you will be prompted
                                                                                  Else, it will be calculated for you automatically
                                                                                  
       Time:                                                                      Displays current time
       Date:                                                                      Displays current date
       program:                            [program name], eg "chrome"            Attempts to run an installed program
       Whoami:                                                                    Displays your user name based on which account you are signed into in your OS
       List:                               [optional]                             Displays the list of n in a directory, i.e, files, folders, drives, etc

       For more specific help, type "help", followed by the command you want help for
       * = not available for specific help
       
       If no usage is specified, only the command word is necessary to execute the command
       If the command is lower case, the command is not to be entered. Instead, what the usage column states

    """
    )
    if outsideAccess == True: # if other functions are calling this function
        return commands
    else: # if user inputs help
        print(commands)
        run() # restarts app

def terminal(showWelcome=False): # main function for everything
    cwd = os.getcwd() # gets current working directory which can be changed from chdir. Cwd is reset when app is quit
    drvLtr = cwd[0].capitalize() # formats drive letter for cwd
    cwd = drvLtr+cwd[1:] # appends drvLtr to cwd to format it correctly
    if showWelcome == True: # if the user has started the app from off
        output = "Welcome to my terminal!\r\nCurrent OS: " + platform.system() + " " + platform.release() + ", version: " + platform.version() +"\r\n\r\n"+cwd+": " # prints OS info and cwd
        output = str(output).replace("(", "").replace(")","") # formats the output to remove brackets 
        consoleInput = input(output).lower() # sets consoleInput (main input for the app) to output
        splitOutput = (consoleInput).split() # sets splitOutput to split consoleInput (main sliced input)
    else: # if the user has returned to this function 
        consoleInput = input(cwd+": ").lower() # same as previous
        splitOutput = (consoleInput).split() # same as previous
        
    try:   
        if consoleInput == 'help': # if user entered help
            help() # executes help function
        
        elif len(consoleInput) == 0: # if nothing is entered
            run() # restarts app
            
        elif len(''.join(splitOutput)) == 0: # if the length of whatever entered is 0 (user did not enter anything)
            run() # restarts app
        
        elif consoleInput == 'whoami': # same as whoami in command prompt
            print('{}'.format(os.getenv('username'))) # prints username environment variable
            run() # restarts app
        
        elif splitOutput[0] == 'help' and len(splitOutput[0]) != 0: # if user wants advanced help for a specific function
            command = splitOutput[0] # sets command to whatever function user wants help for 
            advancedHelp(command) # executes advancedHelp function
            run() # restarts app
            
        elif splitOutput[0] == 'exit': # if user wants to exit app
            sys.exit() # exits app
            
        elif 'www' in consoleInput: # if user wants to open website
            os.system('start %s' % consoleInput) # uses os.system to open website
            run() # restarts app

        elif '--version' in splitOutput[1:] or '-v' in splitOutput[1:]: # if user wants version info
            version() # executes version function

        elif 'calc' in splitOutput: # if user wants to calculate something
            
            # This code may be omitted in future for efficiency
            
            global answer # sets answer to global
            
            if len(splitOutput[1:]) == 0: # if no calculation is entered
                calculatorNormal(splitOutput) # executes main calc function with splitOutput as kwarg
                
            elif splitOutput[1] == 'acos': 
                answer = math.acos(math.radians(float(splitOutput[2])))
            
            elif splitOutput[1] == 'acosh':
                answer = math.acosh(math.radians(float(splitOutput[2])))
            
            elif splitOutput[1] == 'asin':
                answer = math.asin(math.radians(float(splitOutput[2])))
            
            elif splitOutput[1] == 'asinh':
                answer = math.asinh(math.radians(float(splitOutput[2])))
            
            elif splitOutput[1] == 'atan':
                answer = math.atan(math.radians(float(splitOutput[2])))
            
            elif splitOutput[1] == 'atanh':
                answer = math.atanh(math.radians(float(splitOutput[2])))
            
            elif splitOutput[1] == 'cos':
                answer = math.cos(math.radians(float(splitOutput[2])))
            
            elif splitOutput[1] == 'cosh':
                answer = math.cosh(math.radians(float(splitOutput[2])))
            
            elif splitOutput[1] == 'fact':
                answer = math.factorial(int(splitOutput[2]))
            
            elif splitOutput[1] == 'hypot':
                answer = math.hypot(float(splitOutput[2]))
            
            elif splitOutput[1] == 'pow':
                answer = math.pow(float(splitOutput[2]))
            
            elif splitOutput[1] == 'sin':
                answer = math.sin(math.radians(float(splitOutput[2])))
            
            elif splitOutput[1] == 'sinh':
                answer = math.sinh(math.radians(float(splitOutput[2])))
            
            elif splitOutput[1] == 'sqrt':
                answer = math.sqrt(float(splitOutput[2]))
            
            elif splitOutput[1] == 'tan':
                answer = math.tan(math.radians(float(splitOutput[2])))
            
            elif splitOutput[1] == 'tanh':
                answer = math.tanh(math.radians(float(splitOutput[2])))
            
            else:
                calc = splitOutput[1:] # sets calc to whatever is entered if no complex maths is entered
                calculatorSliced(calc) # exeutes calculatorSliced function
            
            print('The answer to "{}" is {}.'.format(' '.join(splitOutput[1:]), answer)) # formats and prints answer
            run() # restarts app
        elif consoleInput == 'time': # if user wants time
            cTime = dt.datetime.now() # gets raw time
            print('Current time: {}'.format(cTime.strftime('%X'))) # formats and prints time
            run() # restarts app

        elif consoleInput == 'date': # if user wants date
            cDate = dt.datetime.now() # gets raw date
            print('Current date: {}'.format(cDate.strftime('%x'))) # formats and prints date
            run() # restarts app
            
        elif 'list' in splitOutput[0]: # if user wants to list objects
            list(splitOutput) # executes list function with splitOutput as kwarg
            print() # prints a newline / line feed for readability
            run() # restarts app
        
        elif 'chdir' in splitOutput[0]: # if user wants to change current working directory
            chdir(splitOutput) # executes chdir function with splitOutput as kwarg
            run() # restarts app
            
        elif 'mkdir' in splitOutput[0]: # if user wants to make a directory
            mkdir(splitOutput) # executes mkdir function with splitOutput as kwarg
            run() # restarts app
            
        elif 'mkfile' in splitOutput[0]: # if user wants to make file 
            mkfile(splitOutput) # executes mkfile function with splitOutput as kwarg
            run() # restarts app
            
        elif 'delete' in splitOutput[0]: # if user wants to delete a file or directory
            delete(splitOutput) # executes delete function with splitOutput as kwarg
            run() # restarts app
            
        try:
            if tuple(splitOutput) in appDict: # if (maybe) program name is in appDict
                search_filter(app=' '.join(splitOutput)) # executes search_filter function with joined splitOutput as kwarg
                run() # restarts app
            
            global appname # sets var appname to global
            for app in winapps.search_installed(splitOutput[0]): # for every app in apps detected by winapps library and matches the search description
                appname = app.name.lower() # sets alll apps to lower case
                try:
                    os.system(f'start {splitOutput[0]}') # attempts to execute the app
                except:
                    os.system(f'start {appname}') # if it fails, it attemps to use the app name given by winapps
                finally:
                    run() # restarts app
                
        except:
            print('Invalid command. ') # prints exception
            print(help(outsideAccess=True)) # executes help function
        
        try:
            
            # This code here may be omitted
            
            cmdList = ['help','version','calc','time','date','[program]','whoami','list','chdir'] # command list 
            
            global appName, appLocation # sets appName and appLocation to global
            appName = '' # empty string to be written to later
            appLocation = '' # empty string to be written to later
            
            for app in winapps.search_installed(consoleInput.removesuffix('.exe')): # for every app searched by winapps using consoleInput
                appLocation = app.install_location # extracts app location from winapps.search_installed()
                appName = (app.name).lower() # extracts app name from winapps.search_installed() and ets it to lower case
                if len(appName) == 0 or not appName or appName == False: # if no app name is found / if no search result / search result is False
                    run() # restarts app    
        
            if consoleInput.strip().removesuffix('.exe') in appName: # if consoleInput without whitespaces and without '.exe' in app name
                if not consoleInput.strip() in cmdList: # if the consoleInput is not is cmdList
                    try:
                        os.system('start %s' % consoleInput) # attempt to execute raw consoleInput
                        run() # restarts app
                    except:
                        try:
                            os.system('start %s' % appName) # attempt to execute app name given by winapps
                            run() # restarts app
                        except:
                            try:
                                os.system('start "%s"' % appLocation) # attempt to execute app location given bvy winapps *may be omitted*
                            except Exception as startAppError:
                                raise Exception("Could not start application specified. Reason: %s" % startAppError) # raise exception
                            finally:
                                run() # restarts app
                                
        except Exception as appError:
            raise Exception('Could not start application specified. Reason: %s' % appError) # raise exception
        
        else:
            print('Invalid command') # prints exception
            print(help(outsideAccess=True)) # executes help
        finally:
            run() # restarts app
            
    except Exception as termError:
        if type(termError) == ValueError:
            raise ValueError('Not a number. ') # raise exception
            
        elif type(termError) == IndexError:
            raise IndexError(f'Not enough or too many arguments for command {splitOutput[0]}') # raise exception
        else:
            print("An exception has occured: %s" % termError) # print exception as raise makes code above unreachable
        
    finally:
        run() # restarts app

def run(ifClear = False): # main starting function to execute the rest of the app
    try:
        while True:
            if ifClear == True: # if it is first execute after being exited
                ifClear = False # set ifClear to False to prevent clearing by accident
                os.system('cls || clear') # clears screen
                terminal(showWelcome=True) # executes terminal with showWelcome set to True
            else: # if it is not first execute
                terminal() # showWelcome is False
    except Exception as terminalError:
        print('An exception has occured: %s' % terminalError) # prints exception as raise makes code below unreachable
        if ifClear == True: # # = same as above
            ifClear = False #
            os.system('cls || clear') #
            terminal() # executes terminal function
        else: #
            terminal() #

if __name__ == '__main__': #only executes if the name of the file is __main__ to prevent the file being run as a library / import, only as module
    while True: # always runs unless told to exit via command
        run(ifClear = True) # executes run function and clears the screen
