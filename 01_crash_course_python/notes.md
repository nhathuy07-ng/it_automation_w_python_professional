# Notes

## Some basic theoretical stuffs

- Syntax = rules for writing instructions

- Semantics = meaning of the instructions

- Predicate = statement (verb, or what the subject is doing)

- Script = short & simple programs

- Automation = replace manual steps with automatic ones

    - Automation avoids human mistake

    - Some tasks ARE NOT suited for:

        - Tasks requiring flexibility, creativity, social connection, psychology and other complex analytics work.

        - Complicated & less frequently executed task (automation might cost more time!)

- Keywords = reserved words for a specific purposes

> [!IMPORTANT]
> Understanding Syntax + Semantics is crucial for writing code

> [!IMPORTANT]
> Common semantic errors include: 
>    - Functional code but unintentional output
>    - Poor logic structures


> [!NOTE]
> **Takeaway**: Automation can save time, reduce error and improve consistency, but not all tasks can be automated.

## Why's Python relevant to IT?

- Super popular, one of the most common languages.

- It's becoming more powerful and having more tools for it (e.g for statistics)

- Simple, easy to understand and maintain

- Popular in automation workflow and sysadmin tools

- Other popular scripting languages in automation include PowerShell, Bash, Perl, ...

## Code editors vs IDEs

- Code editors: Provide basic toolings:
    - Syntax highlighting
    - Auto-indentation
    - Error checking
    - Auto-completion

- IDEs: More comprehensive features for software development:
    - Edit, build, test, package in one environment
    - Eliminate manual integration -> Quicker coding

## JupyterLab & Jupyter Notebooks

- JupyterLab: web-based UI to run Python code (via Jupyter Notebooks) in the cloud
- Jupyter Notebooks: live notebooks with runnable code
- Notebooks can be shared via GitHub, email, and viewed thru Jupyter Notebook Viewer

## Variable annotation with Python

- Strings: `name: str = "Stew"`
- Integers: `age: int = 18`
- Lists: `List[type]` (e.g `List[str]` for list of integers)

> [!IMPORTANT]
> Python still decides the variable type at runtime. However, some libs (e.g data validation) reads these annotations at runtime, resulting in overhead if over-annotation occurs.

## Code style

- Having good code style is important for collaboration and maintenance.

- Good style makes the script looks clear to the reader, almost akin to human language.

- No hard and fast rules, but:
    - Code should be self-documenting: intent should be clear
    - Use comments if code is too complex to be self-documenting (e.g notes for improvements)
    - Use style guides if applicable

## For vs While

- `for i in <sequence>`: Iterate thru a sequence (range, list, string, etc.)

- `while <condition>`: Run a loop while condition is True, break out once condition is false.

- `while ... else ...`: Run `else` block if loop completed without invoking `break`

- `range(start, end, step)`: iterates from `start` (default: 0) to the number **before** `end`, at `step` intervals (default: 1)


## String alignment with formatting `{}`

- Aligning to the right: `">x"` - string occupies x spaces, right-aligned
- Aligning to the left: `"<x"` - string occupies x spaces, left-aligned
- Centered: `"^x"` - occupies x spaces, shifted to left if cannot be centered

## List comprehension vs `for` loops append

- List comprehension: `[expr(x) for x in sequence if condition]`
- Use list comprehension for **simple** list generation code.
- For more complex code, using **for loops** is preferred.
- Balances conciseness with ease of comprehension.

## (Extra) some OOP stuffs

- Method types:
    - Instance methods:
        - Creating functions within the class definitions
        - Access to `self` - representing the instance the method being exec'd on.
    - Class method:
        - Decorated with `@classmethod`
        - Takes `cls` parameter - representing the class.
        - Used to create and modify data structures containing records for all instances of a class.
        - Class-wide data structs are defined in the class definition (outside constructor, w/out `self.`)
    - Static method:
        - Decorated with `@staticmethod`
        - For tasks that don't need to access or modify any object or class data.

---

## Problem Statement

- A report-generating tool to track which user are logged in to which machine.
- Input: List of `Event (date, user, machine, type)`
- Output: List all machine names, each with currently logged in users.

> Read-only lab URL: [Here](https://hub.labs.coursera.org/connect/sharedypyecuio?forceRefresh=false&path=%2Fnotebooks%2FC1M6L1_Putting_It_All_Together.ipynb&sessionMigrationMode=shadow)

