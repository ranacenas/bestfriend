import subprocess
import configparser
import time
import os

def startupcheck(configpw):
    """Checks if the password has been changed or not.
    If it has not been changed, it will return false."""
    if configpw == 'default':
        return False
    else:
        return True

def savepw(inputpw, filename):
    """Changes the password in the .ini file"""
    config = configparser.ConfigParser()
    config.read(filename)
    config.set("PASSWORD", "password", inputpw)
    with open(filename, 'w') as f:
        config.write(f)
    return True

def passwordcheck(password, configpw):
    """Checks if the password matches the password in the .ini file.
    If it matches, it will return True"""
    if password == configpw:
        return True
    else:
        return False

if __name__== "__main__":
    #program_path = os.getcwd()
    file = 'pw.ini' #file

    #GET PASSWORD
    config = configparser.ConfigParser()
    config.read(file)
    getpass = config.get("PASSWORD", "password")

    #Startup
    x = startupcheck(getpass)

    
    while x is False: #Password has not been set. First time starting up program
        print("Welcome! Please set a password. The current password is 'default'")
        pwsetinput = input("Enter password here: ")
        if pwsetinput == 'default': #prevents from password being 'default'
            print("enter a new password please")
            pwsetinput = input("new pass")
            savenew = savepw(pwsetinput, file) 
            x = True
        else:
            savenew = savepw(pwsetinput, file)
            x = True
            print("Thank you!")
            print("This program will now close. Once you run this program again, it will ask for the password to keep your history")
            time.sleep(3)
            break

    #Password has been set. This prompts for the password.
    else:
        print("WARNING! You only get one chance so please enter your password carefully")
        enterpw = input("Please enter the password to keep your history: ")
        
        #correct password
        if passwordcheck(enterpw, getpass) is True:
            print("Correct password! You're still alive and you're history won't be deleted")
            time.sleep(4)
        #incorrect password - triggers .bat file    
        else:
            print("Oh no, I'm now deleting the history and everything else like a good friend!")
            #batch file must be in the same folder as the script/executable
            subprocess.Popen("clearall.bat", cwd=os.path.dirname(os.path.realpath(__file__)))
            time.sleep(3)
            print("Everything has now been deleted")
            time.sleep(3)
            