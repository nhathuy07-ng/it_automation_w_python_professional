import subprocess

# Run function returns a `CompletedProcess` object
# subprocess's standard output is printed to the Python script process's STDOUT
# subprocess.run is a blocking function.
subprocess.run(["clear"])
subprocess.run(["date"])
completed = subprocess.run(["sleep", "2"])
print(completed.returncode) # gets the subprocess's return code
