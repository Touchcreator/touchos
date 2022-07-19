import time, os, platform

plat = platform.system() # get the os
archie = platform.machine() # get the architeture

if (plat!="Windows"): # inform the user that touch os was made for windows
    useanyway = input("Your host OS was detected as " + plat + ". However, Touch OS was designed for Windows. Use anyway? ")
    if (useanyway == "n"):
        print("Ok then, exiting")
        time.sleep(1)
        exit()

print("""
 ______________________
|   Touch OS 0.0.2.1   |
|                      |
|    POV: Not an OS    |
|______________________|
""")

da_commands = ["exit", "gotodir", "clear", "host", "say", "run", "passout", "help", "read", "abouthost"]
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

    else:
        print("That command doesn't exist")
while True:
    cwd = os.getcwd()
    the_cmd = input("touchosuser@" + cwd + ": ")
    read_cmd(the_cmd)
