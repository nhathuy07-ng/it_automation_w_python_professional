# Extract the process ID
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"

"""
Naive way: 
Find the first bracket, and extract 5 next digits from there.
Problem: We can never be sure if the process ID is exactly 5-digit long.
"""
index = log.index("[")
print(log[index+1:index+6])

r"""
Use re.search to find the first substring matching the search pattern.
"\[(\d+)\]": Find strings that start with "[", followed by
one or more digits, end with "]".
r: rawstring, prevents Python from interpreting special characters
"""

import re
regex = r"\[(\d+)\]"
result = re.search(regex, log) # returns matched position and string

# get the position range `span()` and first result
print(result.span())
print(result[1])

# find all substrings matching pattern
results = re.findall(regex, log)
print(results)