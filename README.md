## WARNING! By downloading this program, you are aware that this program will potentially delete all chrome data permanently. I am not responsible for any corruption or loss of data. Please use at your discretion.


## About

#### Currently, this version only deletes chrome data and is only available on Windows. I have a linux version that I'm still working on.

Even though you should use incognito, there is probably some information on chrome that you don't want family, friends, or strangers to see. Therefore, I created a very simple program that deletes all chrome (for now - working on expanding to more browsers) data on Windows if the password is incorrect. For example, let's say you were gone for a while and somehow a person was able to access your computer. With this program, you can ask whoever is currently using the computer to input a password. If that password is incorrect, it will trigger the batch file and delete all chrome data. If you use the executable, closing the executable window will also trigger the batch file which will then delete all chrome data. 

*credit to catonmat for the batch script (https://catonmat.net/clear-privacy-ie-firefox-opera-chrome-safari)*

## How to use

#### Executable 

1) Simply download as a ZIP and extract. 

2) Run the program the first time to set up a password.

3) Set up a task schedule to run the program automatically.

When setting up the task schedule, in the `Start in` section, put down the path of where the program is. ex. C:\\Path\to\folder\bestfriend

#### Python script

1) Download as a ZIP and extract.

2) Run the program and set up a password.

3) Set up a task schedule to run the program manually. 

When setting up the task schedule, the program you want to execute is python.exe so you wil have to copy and paste the path the python.exe is on. And then in the `'Add arguments'` section, input the path of the script like so: C:\\path\to\bestfriend\windows_bestfriend_cmd.py. Lastly, in the `'Start in'` section, input the path of where the script is located like so C:\\path\to\bestfriend. 

Tip: Hide the folder so people won't see it.


### Note: It is important to keep all the files all in one folder to ensure everything runs smoothly. If the pw.ini file or clearall.bat file are not in the same folder as the python script or the .exe, it will not run correctly. 

## What if I forget my password?

Go to the folder where the script or program is located. There you will see a file called `'pw.ini'`. Open it and there you will see the password. 
