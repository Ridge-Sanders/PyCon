# PyCon
Python3 Console: Command-Line Interface. Simple, lightweight & Fast (as python can be).
_Just a concept I've been working on_

## Installation

```bash
git clone https://github.com/Ridge-Sanders/PyCon.git ~/.scripts/PyCon
```

## Configure
Custom commands can be added to the PyCon library as follows:

1. Open the file **'env_vars.py'** and add a new entry to the commands nested dictionary.
  1. All new command entries need a description key-value pair, and an execution key-value pair that points to the command in the commands.py file.
  
```python
#!/usr/bin/python3

# Necessary import for executing command functions.
from commands import *

env_vars = {
  'version': '1.0.0',
  'motd': 'Welcome to PyCon',
  'commands': {
    'help': {
      'description': 'Show a list of usable commands.',
      'execute': PyCon_Help
      },
      
      'myCommand': {
        'description': 'Does something in the PyCon CLI.',
        'execute': myCommand
        }
    }
 }
```

2. Open the file **'commands.py'** and add your command function.
  1. In this current version all command functions require at least one parameter even if it remains unused.
 
```python
#!/usr/bin/python3

# myCommand
def myCommand(var):
  print("Hello, World!")
```
## License
[GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html)
