import os.path
from datetime import datetime
print("file size (bytes)", os.path.getsize("zen_of_python.txt"))

"""
try access the file then get last accessed time.
NOTE: on Linux, if file is only read, not modified, the kernel
might delay updating last accessed time to save disk performance,
resulting in `getatime` not showing the actual last accessed time.
"""

f = open("zen_of_python.txt", "r")
f.readlines()
f.close() 

print("last accessed: unix timestamp (s)", os.path.getatime("zen_of_python.txt"))
print("last accessed: datetime", datetime.fromtimestamp(os.path.getatime("zen_of_python.txt")))
print("last modified: datetime", datetime.fromtimestamp(os.path.getmtime("zen_of_python.txt")))
print("created: datetime", datetime.fromtimestamp(os.path.getctime("zen_of_python.txt")))

print("absolute path:", os.path.abspath("zen_of_python.txt"))
print("is file:", os.path.isfile("zen_of_python.txt"))
print("is dir:", os.path.isdir("zen_of_python.txt"))

"""
try isfile and isdir with a nonexistent (i.e. ghost) path
"""
print("ghost path is file:", os.path.isfile("zen_of_js.txt"))
print("ghost path is dir:", os.path.isfile("zen_of_js.txt"))

print("current working dir (path where the python script is called):", os.getcwd())
# change cwd to a new subdir
os.mkdir("NOTHING_HERE")
os.chdir("NOTHING_HERE")
print('new cwd: ', os.getcwd())