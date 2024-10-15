# Assignments/Shell_Project/Shell/cmd_pkg/__init__.py

# import the relevant classes from the packaged files
from .cat import cat
from .cd import cd
from .chmod import chmod
from .cp import cp
from .grep import grep
from .head import head
from .history import history
from .less import less
from .ls import ls
from .mkdir import mkdir
from .mv import mv
from .pwd import pwd
from .rm import rm
from .sort import sort
from .tail import tail
from .wc import wc
from .who import who
from .x_history import x_history

# put all the classes as a dictionary of commands
__all__ = [
    'cat',
    'cd',
    'chmod',
    'cp',
    'grep',
    'head',
    'history',
    'less',
    'ls',
    'mkdir',
    'mv',
    'pwd',
    'rm',
    'sort',
    'tail',
    'wc',
    'who',
    'x_history'
]