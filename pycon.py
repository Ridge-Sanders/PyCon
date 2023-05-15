#!/usr/bin/python3

# Import environment variables
from env_vars import *

# Temporary Hostname
hostname = "user"

# Console
def console():
    print(f"{env_vars['motd']} v{env_vars['version']}")
    while True:
        command = input(f"[{hostname}@PyCon]$ ")
        try:
            args = command.split()
            commandInterpreter(command, args)
        except Exception:
            print("Something went wrong...")


# Command Interpreter
def commandInterpreter(command, args):
    if not command:
        return
    
    commands = list(env_vars['commands'].keys())
    if args[0] in commands:

        run = env_vars['commands'][args[0]]['execute']
        if args[0] == "echo":
            run(args)
        else:
            run(env_vars)
    else:
        print(f"Invalid option -> {args[0]}")


# Begin
console()