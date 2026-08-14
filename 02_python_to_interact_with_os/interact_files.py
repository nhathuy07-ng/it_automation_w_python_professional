
"""
Open-Use-Close pattern
"""

f = open("zen_of_python.txt")

# Read the current line (including the trailing newline character) then jump to the next
print("read", f.readline())
print("read", f.readline())

# Read from the current position to the end
print(f.read())

# Close file
f.close()
print("file closed")

"""
With block. No need to close
"""

print("---")

with open('zen_of_python.txt') as f:
    print(f.read())