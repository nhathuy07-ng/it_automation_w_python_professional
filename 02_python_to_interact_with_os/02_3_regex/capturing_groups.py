"""
Capturing Groups
"""

import re

result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)

groups = result.groups()
print(groups) # return capturing groups, both elements matched by (\w*)
print("{} {}".format(groups[1], groups[0]))

# Updated: Supports double surname, middle name and initials
result = re.search(r"^([\w \.-]*), ([\w \.\-]*)$", "Hopper, Grace M.")
groups = result.groups()
print(type(groups))
print("{} {}".format(groups[1], groups[0]))
