import os # abstraction layer for OS-specific functions
import os.path # deals with path information

"""List directory, remove a file then check again"""
try:
    print(os.listdir())

    # Delete file!
    os.remove("zen_of_python copy.txt")
    
    print("\nfile zen_of_python copy deleted!")
except FileNotFoundError:
    print("\nfile zen_of_python copy.txt not found!")

"""Check if file exists"""
print("zen_of_python.txt exists?", os.path.exists("zen_of_python.txt"))
print("zen_of_python copy.txt exists?", os.path.exists("zen_of_python copy.txt"))