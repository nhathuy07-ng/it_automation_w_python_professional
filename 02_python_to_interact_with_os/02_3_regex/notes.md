# Notes

- Regular expression (Regex or Regexp): Search query for text represented as a pattern.
- Used in Programming language, and cmdline tools like `grep`, `sed`, `awk`

- `grep`:
    - If given a pure, non-regex string, it would print any lines containing that string, case-sensitive.
    - Use `grep <pattern> <file_name>`
    - Add `-i` flag for case-insensitive matching
    - Can use regex

- Some regex stuffs for matching lines:
    - `.`: any single character
    - `^` + pattern: lines starting with pattern
    - pattern + `$`: lines ending with pattern
    - `[Ab]`: one character matching with either A or b
    - `[^Ab]`: one character NOT matching with eithe A or B
    - `[a-z]`: one character matching with the range a-z
    - `cat|dog`: string matches either phrase "cat" or "dog"
    - `.*n`: Matching any (can be none) characters up until the LAST n.
    - `+`: Matches one or more adjacent instances of pattern before it. 
    - `\w`: Matches alphanumericals and underscores
    - `\s`: Matches whitespaces
    - `\d`: Matches digits
    - `\b`: Boundary anchor to match a 0-width position between a word and non-word character. In practice, bounding a pattern with `\b` will match with the whole word (not part of a word) matching that pattern. 
    - pattern + `?`: zero or one matching.
    - pattern + `{3}`: Matches a pattern 3 times

    > These are called "reserved characters"
    > `[]` and `[^]` can contain multiple ranges and character. String matches if it matches at least one range or character in the bracket.
    > When you want to match the reserved characters as-is, use backslash.

- Capturing groups: Portions of the pattern enclosed in parentheses

- Test regexes at [](www.regex101.com)

## Splitting and Replacing

- Splitting: `re.split(pattern, input_str)`:
    - Returns a list of strings split at matching substrings. Substrings matching capture groups are kept.
- Substituting: `re.sub(pattern, new_str, old_str):
    - Replaces matching substrings with new_str
    - `new_str` can refer to the i-th capture group with `\i` (1-based indexing). These are called **backreference**
