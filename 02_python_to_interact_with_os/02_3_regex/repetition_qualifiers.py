"""
Repeated matches

`.*`: matches any character, repeated as many times as possible
"""
import re

"""
`.*n`: Matching any characters up until the LAST n.
+: Matches one or more adjacent instances of character before it. 
"""
print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))

# This matches with any alphabetical characters, excluding whitespace.
print(re.search(r"Py[a-z]*n", "Python Programming"))

# This matches one or more adjacent instances of character before it.
print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woollllly"))

# Case-insensitive matching
print(re.search(r"o+l+", "WOOOOOOLY", re.IGNORECASE))


"""
Numeric repetition qualifiers: 

Use: {min_occurence,max_occurence} or {occurences}
{min_occurence,}: at least n occurences
{,max_occurence}: at most n occurences
"""

print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))

# Match whole word
print(re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared"))

# Match whole word of length 5 or more
print(re.findall(r"\b[a-zA-Z]{5,}\b", "a scary ghost appeared"))
