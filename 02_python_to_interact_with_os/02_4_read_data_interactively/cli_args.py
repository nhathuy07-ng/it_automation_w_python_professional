import sys

"""
Print the argument list.

Arguments are stored within the sys library.
First element is path of the program relative to the directory 
from which it's called.
"""

print(sys.argv)

"""
Exit status: Value ret'd by a program to the shell.
Status 0 if it exits, not 0 if fails.

In bash, variable `?` stores the error code of the last executed program in the shell. 
Exit code range is within 0-255.
"""

sys.exit(67)