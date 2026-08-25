import subprocess

# `host` looks up a DNS's name based on its IP address.
result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.returncode)

# result.stdout is actually an array of bytes, not a proper Python string
print(result.stdout)
print(result.stdout.decode('utf-8'))
print(type(result.stdout))

# try with stderr
# text=True converts byte array into a standard `str`
result = subprocess.run(["rm", "ghost_file"], capture_output=True, text=True)
print(result.returncode)
print(result.stderr)
print(type(result.stderr))

"""
NOTE: using subprocesses requires assumption about the underlying environment
our script will be running on. missing command(s) might cause our script to fail
either noticably or unnoticably (depending on how the script is written).
"""
