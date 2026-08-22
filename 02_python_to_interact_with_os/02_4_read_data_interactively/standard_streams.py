"""
I/O streams: Basic mechanism to perform input/output operations for the program.

stdin: standard input (target input -> program)
stdout: standard output (program -> target output)
stderr: standard error (program -> target output but for error)
"""

data = input("stdin: ")
print("stdout: " + data)

# this yields a TypeError, which is printed to stderr
print("stderr: " + data + 1)

# note: in Python 2.x, raw_input() gets the input string, but input() evals the string.
