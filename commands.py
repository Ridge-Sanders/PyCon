#!/usr/bin/python3

# Help
def PyCon_Help(var):
    commands = var['commands']
    for command, value in commands.items():
        description = value['description']
        print(f"  * {command}    : {description}")

# Quit
def PyCon_Quit(var: None):
    print("PyCon closed.")
    quit()


# Echo
def PyCon_Echo(var):
    var.pop(0)
    for i in range(len(var)):
        print(f"{var[i]}",end=" ")
    print()


# Clear
def PyCon_Clear(var: None):
    print("\033\143",end="")


# Version
def PyCon_Ver(var):
    version = var['version']
    print(version)


# MOTD
def PyCon_MOTD(var):
    motd = var['motd']
    print(motd)