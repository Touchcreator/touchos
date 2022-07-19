import time, os

print("""
 ______________________
|    Touch OS 0.0.1    |
|                      |
|    POV: Not an OS    |
|______________________|
""")

da_commands = ["exit", "gotodir", "clear", "host", "say", "run", "passout", "help"]
def read_cmd(cmd):
    if cmd == "exit":
        exit()
    elif cmd == "listfiles":
        print(os.listdir(cwd))
    elif (cmd.__contains__("gotodir ")):
        try:
            os.chdir(cmd[8:len(cmd)])
        except FileNotFoundError:
            print("That folder doesn't exist")
        except NotADirectoryError:
            print("That is not a folder")
        except PermissionError:
            print("Cannot access that folder right now")
    elif cmd == "clear":
        os.system("cls")
    elif (cmd.__contains__("host ")):
        os.system(cmd[5:len(cmd)])
    elif (cmd.__contains__("say ")):
        print(cmd[4:len(cmd)])
    elif (cmd.__contains__("run ")):
        filepath = cmd[4:len(cmd)]
        with open(filepath) as fp:
            for index, line in enumerate(fp):
                read_cmd(line.strip())
    elif (cmd.__contains__("passout ")):
        time.sleep(int(cmd[8:len(cmd)]))
    elif cmd == "help":
        print(da_commands)

    else:
        print("That command doesn't exist")
while True:
    cwd = os.getcwd()
    the_cmd = input("touchosuser@" + cwd + ": ")
    read_cmd(the_cmd)
