import subprocess
import configparser
import time
import PySimpleGUI as sg
import os

def countdown(n):
    for i in range(n, 0, -1):
        time.sleep(1)
    
def startupcheck(configpw):
    """Checks if the password has been changed or not.
    If it has not been changed, it will return false."""
    if configpw == 'default':
        return False
    else:
        return True

def passwordcheck(password, configpw):
    """Checks if the password matches the password in the .ini file.
    If it matches, it will return True"""
    if password == configpw:
        return True
    else:
        return False

def savepw(inputpw, filename):
    """Changes the password in the .ini file"""
    config = configparser.ConfigParser()
    config.read(filename)
    config.set("PASSWORD", "password", inputpw)
    with open(filename, 'w') as f:
        config.write(f)
    return True

if __name__ == "__main__":

    #CORE
    file = 'pw.ini'
    config = configparser.ConfigParser()
    config.read(file)
    getpass = config.get("PASSWORD", "password")
    courier = ('Verdana', 15)

    #STARTUP LAYOUT
    sg.ChangeLookAndFeel('Reddit')
    startup_layout = [[sg.Text("Welcome! Please set a password", font=courier, justification='center')],
    [sg.Text('' * 40), sg.Text('Enter Password', font=courier, justification='center'), sg.Input(do_not_clear=True,key='first_att')],
    [sg.Text('' * 39), sg.Text('Verify Password', font=courier, justification='center'), sg.Input(do_not_clear=True, key='sec_att')],
    [sg.Button('Submit', font=courier), sg.Button('Exit', font=courier)],
    [sg.Text('', font=courier, size=(60, 1), text_color='red', key='verify_pass')],
    [sg.Text('', font=courier, size=(60, 1), text_color='green', key='verify_corr')]]

    startup_window = sg.Window('Welcome to your Bestfriend', icon='favicon.ico').Layout(startup_layout)

    #Delete history layout

    DH_layout = [[sg.Text('Please enter your password to keep your history.', font=courier)],
    [sg.Text('Closing this window will cause your history to be deleted.', font=courier)], #closing it won't do anything
    [sg.Text('Warning you only have one chance. Enter password carefully', font='Courier 12', text_color='red')],           
    [sg.Text('Enter password:', font=courier), sg.Input(do_not_clear=True, key='pass')],
    [sg.Button('Submit', font=courier)]]
    
    DH_window = sg.Window('Bestfriend', icon='favicon.ico').Layout(DH_layout)
    

    #START PROGRAM
    x = startupcheck(getpass)
    
    
    if x is False: #This means the program is starting for the first time
        sg.Popup("""

Welcome to Bestfriend. A program that will delete all of your Chrome data.

WARNING! By downloading and using this program, you are aware of the risks 
and consequences. The developer is not responsible for any data loss or corruption. 
Please use at your own risk. 


Read the docs on github.com/ranacenas/bestfriend or
ranacenas.me/blog.
        
Click 'OK' to continue.""", icon='favicon.ico')
    
        while x is False:

            #Warning popup
            
            
            #Popup closes after clicking okay

            #start up window now opens
            event, values = startup_window.Read()
            

            first_input = values['first_att']
            second_input = values['sec_att']
            
            #closes window if 'X' or 'exit' is clicked
            if event is None or event == 'Exit':
                break
            
            if event == 'Submit':
                
                
                #If password match, it saves the password in .ini file
                if passwordcheck(first_input, second_input) is True:
                    savenew = savepw(second_input, file)
                    successful = "Password matches. Please click on 'Exit' to close the program"
                    nope = ''
                    startup_window.FindElement('verify_corr').Update(successful)
                    startup_window.FindElement('verify_pass').Update(nope)
                    
                    
                    
                #if passwords don't match, update window element.    
                else:
                    startup_window.FindElement('verify_pass').Update('Passwords do not match, please try again')
        startup_window.Close()
        

    #If password is changed, this window will now open
    if x is True:
        event, values = DH_window.Read()

        passwd = values['pass']
        
        #correct password
        if passwordcheck(passwd, getpass) is True:

            sg.Popup("Congratulations, you're still alive or you guessed the password correctly. Nothing will be deleted", icon='favicon.ico')
        

        #incorrect password
        else:

            #calls batch file and deletes everything
            subprocess.Popen("clearall.bat", cwd=os.path.dirname(os.path.realpath(__file__)))
            sg.Popup('Everything is now deleted')
    DH_window.Close()



   