#!/usr/bin/env python3
import shutil
import psutil

while True:
    # get disk usage of root
    du = shutil.disk_usage("/")
    print(du)
    # % free
    print("{:.2f}% free".format(du.free / du.total * 100))

    # cpu usage (average of last 1s)
    print("{:.2f}% CPU".format(psutil.cpu_percent(1)))