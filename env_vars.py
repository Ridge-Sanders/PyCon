#!/usr/bin/python3

# Import command functions
from commands import *

env_vars = {
    'version': '1.0.0',
    'motd': 'Welcome to PyCon',
    'commands': {
        'help': {
            'description': 'Show a list of usable PyCon commands.',
            'execute': PyCon_Help
        },
        'quit': {
            'description': 'Close PyCon.',
            'execute': PyCon_Quit
        },
        'echo': {
            'description': 'Print arguments to PyCon console.',
            'execute': PyCon_Echo
        },
        'clear': {
            'description': 'Clear PyCon console.',
            'execute': PyCon_Clear
        },
        'version': {
            'description': 'Print PyCon\'s current version.',
            'execute': PyCon_Ver
        },
        'motd': {
            'description': 'Print PyCon\'s motd.',
            'execute': PyCon_MOTD
        }
    }
}