import math

try:
    import os, platform, traceback, winapps
    import datetime as dt
except:
    import os
    os.system('pip install platform && pip install traceback && pip install winapps && pip install datetime')
    import platform, traceback, winapps
    import datetime as dt

def version():
    Version = (
    """
       Terminal: By George Dawson - Version 1.0
    """
    )
    print(Version)
    terminal()
    
def advancedHelp(command):
    command = command.lower()
    if command == 'calc':
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
    elif command == 'time':
        print('''
                The 'time' command retrieves the current time based on your timezone. 
              ''')
    elif command == 'date':
        print('''
                The 'date' command retrieves the current date based on your timezone.
              ''')
    elif command == 'program':
        print('''
                When you enter the name of a program, such as Chrome, the app will search through Microsoft's local app database, and attempts 
                to executes the app that matches the name of the app you have entered. 
                For an app with symbols, such as 7-Zip, you must include the symbol or it will fail to execute.
                If it fails to execute, you could try to make sure the app is installed in the first place. 
                If you have verified it is installed and is still not wokring, make sure the app is added to PATH.
                You can do this by typing "edit the system environment variables", and clicking "environment variables". Then, add the file or folder to the "path" subcatagory.
              ''')
    else:
        print('Not a command. For a list of available commands, enter "help"')
        terminal()

def calculatorSliced(calc):
    ans = ''.join(calc)
    print('The answer to {} is {}.'.format(ans,str(eval(ans))))
    terminal()

def calculatorNormal():
    calc = input('Enter a calculation: ')
    print("The answer to {} is {}.".format(calc, str(eval(calc))))
    terminal()

def help(outsideAccess = False):
    global commands 
    commands = (
    """
       Help:

       Commands:                           Usage:                                 Description:

       Help:*                                                                     Displays this screen
       Version:*                           terminal --version, -v                 Displays current version of application 
       Calc:                               [optional(calculation)]                Calculates a mathematical equation. If no calculation is entered after calc, you will be prompted. 
                                                                                  Else, it will be calculated for you automatically
                                                                                  
       Time:                                                                      Displays current time
       Date:                                                                      Displays current date
       program:                            [program name], eg "chrome"            Attempts to run an installed program

       For more specific help, type "help", followed by the command you want help for.
       * = not available for specific help

    """
    )
    if outsideAccess == True:
        return commands
    else:
        print(commands)
        terminal()

def terminal(consoleOutput=None):
    try:
        cwd = os.getcwd()
        try:
            consoleInput = input(consoleOutput.replace("'", "")).lower()
        except AttributeError:
            consoleInput = input(cwd+": ").lower()

        splitOutput = (consoleInput.lower()).split()
        
        cmdList = ['help','version','calc','time','date','[program]']
        
        try:
            for app in winapps.search_installed(consoleInput):
                global appName, appLocation
                appLocation = app.install_location
                appName = (app.name).lower()
        
            if consoleInput.strip() in appName:
                if not consoleInput.strip() in cmdList:
                    try:
                        os.system('start %s' % consoleInput)
                        terminal()
                    except:
                        try:
                            os.system('start %s' % appName)
                            terminal()
                        except:
                            try:
                                os.system('start "%s"' % appLocation)
                            except Exception as startAppError:
                                print("Could not start application specified. Reason: %s" % startAppError)
                                terminal()
        except NameError:
            pass
        
        if consoleInput == 'help':
            help()
            
        elif splitOutput[0] == 'help' and len(splitOutput[1]) != 0:
            command = splitOutput[1]
            advancedHelp(command)
            terminal()
            
        elif 'www' in consoleInput:
            os.system('start %s' % consoleInput)
            terminal()

        elif '--version' in splitOutput[1:] or '-v' in splitOutput[1:]:
            version()

        elif 'calc' in splitOutput:
            
            global answer
            
            if len(splitOutput[1:]) == 0:
                calculatorNormal()
                
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
                calc = splitOutput[1:]
                calculatorSliced(calc=calc)
            
            print('The answer to "{}" is {}.'.format(' '.join(splitOutput[1:]), answer))
            terminal()
        elif consoleInput == 'time':
            cTime = dt.datetime.now()
            print('Current time: {}'.format(cTime.strftime('%X')))
            terminal()

        elif consoleInput == 'date':
            cDate = dt.datetime.now()
            print('Current date: {}'.format(cDate.strftime('%x')))
            terminal()
        
        elif len(consoleInput) == 0:
            terminal()
        
        else:
            print('Invalid command')
            print(help(outsideAccess=True))
            terminal()
    except Exception as termError:
        print("Error: %s - %s" % (termError, traceback.format_exc()))

def run():
    try:
        os.system('cls')
        while True:
            if __name__ == "__main__":
                cwd = os.getcwd()
                output = "Welcome to my terminal!\r\nCurrent OS: " + platform.system() + " " + platform.release() + ", version: " + platform.version() +"\r\n\r\n"+cwd+": "
                output = str(output)
                output = output.replace("(", "")
                output = output.replace(")","")
                print(output)
                terminal(consoleOutput=output)
    except Exception as terminalError:
        if terminalError == ZeroDivisionError:
            print('Very funny...')
            terminal()
        else:
            print('An exception has occured: %s: %s' % terminalError, traceback.format_exc())
            os.system('cls')
            terminal()

while True:
    run()