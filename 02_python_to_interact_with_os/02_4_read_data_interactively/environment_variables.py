"""
Shell: a CLI for interacting with our OS.
Environment variable: variables set inside the shell. Linux systems mostly use
bash by default.
"""

import os

# os.environ is a dictionary.
print(os.environ["SHELL"]) # KeyError if key isn't present
print(os.environ.get("HOME", "__unknown__")) # __unknown__ if key isn't present
print(os.environ.get("FRUIT", "__unknown__")) # __unknown__ if key isn't present

# this WILL NOT set the shell env
os.environ["FRUIT"] = "apple"

