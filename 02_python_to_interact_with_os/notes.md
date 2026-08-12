# Notes: Using Python to interact with the OS

- `arrow`: library to simplify managing and operating on date

## Interpreted vs Compiled Languages

- Compiled:
    - Source code ->  Compiler -> Machine code (Architecture-specific)
    - Runs faster, but takes time to compile
    - Examples include: C, C++, Go, Rust

- Interpreted:
    - Runs code directly via Interpreter
    - Does not need to wait for compilation
    - Examples include: Python, Ruby, JS, Bash, PowerShell

- Mixed approach:
    - Code -> Compiler -> Intermediate code (Architecture-agnostic) -> VM/Language Runtime (Architecture-specific)
    - Used in Java and C#

## Using shebang with `venv`
(or any interpreters specified in current environment's `PATH` variable, so as to avoid having to hardcode the absolute interpreter path)
- `#!/usr/bin/env <interpreter>`
- Python: `#!/usr/bin/env python3`
- This works because:
    - Within a Python `venv`, the `PATH` env var contains the directory `{project root}/.venv/bin`, which is where the Python executable for the current venv is.

## Create own Python module
- Purpose: Enables code re-use
- Modules must contain `__init__.py`, which is the module's entrypoint
- Module name is the module directory's name.
- Importing submodules take the form `import module.submodule` or `from module import submodule`, whether done outside or inside of the module.

## Notes on IDE usage

> [!NOTE]
> Do not be too anchored to your favorite code editor/IDE. Learn at least a system-native code editor (e.g `nano` on Linux) in case you're servicing or interacting with a machine that does not have your preferred editor.


## Pros and Cons of Automation

### Pros
- Scalability: The ability for a system to do whatever it needs to take on more work
- Improves consistency and reduces human error in repetitive tasks.

### Cons
- Sometimes the process of automating a task takes more time than what it saves down the line. **In which case, automation is not worth it.**
- Infrequent and complex tasks might not be good candidates for automation most of the time, but sometimes it can if the goal is to minimize human error.
- Sometimes, underlying systems change, requiring automations to be updated.
    - Add notification mechanism into automations to catch these failures.