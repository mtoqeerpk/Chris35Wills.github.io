#!/usr/bin/env python

"""Test script to check required Python version.

Execute this code at the command line by typing:

  python installation-test-1.py

How to get a command line:

- On OSX run this with the Terminal application.

- On Windows, go to the Start menu, select 'Run' and type 'cmd'
(without the quotes) to run the 'cmd.exe' Windows Command Prompt.

- On Linux, either use your login shell directly, or run one of a
  number of graphical terminals (e.g. 'xterm', 'gnome-terminal', ...).

For some screen shots, see:

  http://software-carpentry.org/setup/terminal.html

Run the script and follow the instructions it prints at the end.  If
you see an error saying that the 'python' command was not found, than
you may not have any version of Python installed.  See:

  http://www.python.org/download/releases/2.7.3/#download

for installation instructions.

**ADAPTED DIRECTLY FROM THE SOFTWARE CARPENTRY INSTALLATION TEST SCRIPT: swc-installation-test-1.py**
**SEE: http://andreww.github.io/2016-01-06-bristol/setup/index.html**
"""

import sys as _sys


__version__ = '0.2'


def check():
    if _sys.version_info < (3, 3):
        print('check for Python version (python):')
        print('outdated version of Python: ' + _sys.version)
        return False
    return True


if __name__ == '__main__':
    if check():
        print('      ')
        print('******')
        print('Passed')
        print('******')
        print('      ')
    else:
        print('      ')
        print('******')
        print('Failed')
        print('Outdated Python versions might work but some things are not back compatible')
        print('Better to install a current version of Python 3!')
        print('http://continuum.io/downloads')
        print('******')
        print('      ')
        _sys.exit(1)
