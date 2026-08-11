# Reflections

## Reflection 1: Your Python automation journey

**Question 1**

Scenario: The power of programming lies in its ability to automate repetitive tasks, making IT roles more efficient and interesting. Consider the skills you've started to build with Python. 

Prompt: Reflect on your personal experience with repetitive tasks and the Python skills you've started to acquire. Then, complete the following:

Describe a repetitive or tedious task you've had to do more than once.

Explain one specific way Python could make that task more efficient or easier to accomplish.

Share one new thing you learned about how Python works (e.g., a function, an operation, a data type).

Describe one overall benefit this kind of automation would have for an IT professional's role. 

**Response**
- One repetitive task I've had to do is to clean up the system cache and other application-specific temporary files. These can be scattered across directories (e.g "~/.cache"), or have different safe cleaning methods (e.g calling a terminal command that belongs to the app). This process is repetitive in nature, so automation can be safely used here.

- One specific way Python could make that task more efficient is to loop through a pre-programmed list of cache/temp directories then delete them from the system, and interact with the OS to call terminal commands for apps whose cache needs to be cleaned safely that way.

- One thing I learned about how Python works is that it can call other programs using what called subprocesses (mainly via `subprocess.run()` function) and retrieves their outputs, meaning you can automate a task quickly by chaining existing command-line utilities together rather than reimplementing them from scratch.

- This kind of automation helps keep large fleets of machines run efficiently and serve more actual purposes in the long-term by frequently trimming the unneccessary files and keeping disk storage usage optimal.

**Question 2**

