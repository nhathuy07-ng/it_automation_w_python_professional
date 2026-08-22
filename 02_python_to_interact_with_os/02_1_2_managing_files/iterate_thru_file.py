f = open("zen_of_python.txt")

# Use iteration
for line in f:
    print(type(line), line)

# List of lines
f.seek(0)
print(f.readlines())