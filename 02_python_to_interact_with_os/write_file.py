import io

"""Write mode: Write - override on open"""

f = open("zen_of_python copy.txt", "w")
original = open("zen_of_python.txt", "r")
f.write(original.read())
f.close()
original.close()


"""Append mode: Appends file only"""

try:
    f = open("zen_of_python copy.txt", "a")
    print(f.readlines()[:5])
except io.UnsupportedOperation:
    print("Cannot read file in append mode!\n")
f.close()


"""R+ mode: Both reading and writing. Can append to file by doing a `readlines` to
push the cursor to the end of the file."""

f = open("zen_of_python copy.txt", "r+")
print("".join(f.readlines()[-3:])) # prints the last 3 lines of Zen of Python
f.write("QUACK QUACK\n") # Write a new line at the end of the file
f.seek(0)
print("".join(f.readlines()[-4:])) # prints the last 3 lines of Zen of Python + a line saying "QUACK QUACK"

f.close()
