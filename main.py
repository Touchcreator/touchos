import time, os, platform, webbrowser
from os.path import exists

plat = platform.system() # get the os
archie = platform.machine() # get the architeture
ver = "0.0.2.3" # this builds version

homedir = os.getcwd() # set the home directory to the init location

if (plat!="Windows"): # inform the user that touch os was made for windows
    useanyway = input("Your host OS was detected as " + plat + ". However, Touch OS was designed for Windows. Use anyway? (y/n) ")
    if (useanyway == "n"):
        print("Ok then, exiting")
        time.sleep(1)
        exit()

toi = exists(homedir + "/tmp")
if (not toi):
    os.mkdir(homedir + "/tmp")

def check_updates():
    os.chdir("tmp")
    nve = exists("newver")
    if (nve):
        os.remove("newver")
    os.system("curl https://touchcreator.github.io/touchos-needed-file-repo/newver -outfile")
    os.rename("utfile", "newver")
    filepath = "newver"
    with open(filepath) as fp:
        for index, line in enumerate(fp):
            newestver = line.strip()
    if (newestver!=ver):
        veranyway = input("The newest version of Touch OS is version " + newestver + ", but you are using version " + ver + ". Use anyway? (y/n) ")
        if veranyway == "n":
            print("Ok then, opening the github page")
            time.sleep(1)
            webbrowser.open("https://github.com/Touchcreator/touchos")
            exit()
    os.remove("newver")
    os.chdir("..")

check_updates()

os.system("cls")
print("""
 ______________________
|   Touch OS 0.0.2.3   |
|                      |
|    POV: Not an OS    |
|______________________|
""")

da_commands = ["exit", "listfiles", "gotodir", "clear", "host", "say", "run", "passout", "help", "read", "abouthost", "myver", "quine"]
def read_cmd(cmd):
    if cmd == "exit":
        exit()
    elif cmd == "listfiles":
        print(os.listdir(cwd))
    elif (cmd.__contains__("gotodir ")):
        try:
            os.chdir(cmd[8:len(cmd)]) # chdirs to the listed dir
        # any errors vvvvvvvvvvvvvvvvvvvvvvvvvvv
        except FileNotFoundError:
            print("That folder doesn't exist")
        except NotADirectoryError:
            print("That is not a folder")
        except PermissionError:
            print("Cannot access that folder right now")
    elif cmd == "clear":
        os.system("cls") # cls means clear
    elif (cmd.__contains__("host ")):
        os.system(cmd[5:len(cmd)]) # does the listed command
    elif (cmd.__contains__("say ")):
        print(cmd[4:len(cmd)]) # prints what you want it to print
    elif (cmd.__contains__("run ")):
        filepath = cmd[4:len(cmd)]
        try:
            with open(filepath) as fp:
                for index, line in enumerate(fp):
                    read_cmd(line.strip()) # reads the file, then reads the command on there
        except FileNotFoundError:
            print("That file doesn't exist")
        except PermissionError:
            print("Cannot access that folder right now")
    elif (cmd.__contains__("passout ")):
        time.sleep(int(cmd[8:len(cmd)]))
    elif cmd == "help":
        print(da_commands)
    elif (cmd.__contains__("read ")): # literally just the run command
        filepath = cmd[5:len(cmd)]
        try:
            with open(filepath) as fp:
                for index, line in enumerate(fp):
                    print(line.strip())
        except FileNotFoundError:
            print("That file doesn't exist")
        except PermissionError:
            print("Cannot access that folder right now")
    elif cmd == "abouthost":
        print("Host OS: " + plat)
        print("Host Architecture: " + archie)
    elif cmd == "myver":
        print("Touch OS Version: " + ver)
    elif cmd == "quine":
        os.chdir(homedir)
        read_cmd("read main.py")
        workque = input("Did it work? (y/n) ")
        if workque == "n":
            print("You probably renamed main.py")

    else:
        print("That command doesn't exist")
while True:
    cwd = os.getcwd()
    the_cmd = input("touchosuser@" + cwd + ": ")
    read_cmd(the_cmd)
