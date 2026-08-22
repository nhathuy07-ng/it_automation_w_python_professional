import csv


"""
Write list of Dictionaries into CSV, using keys as header.
Header must be written explicitly using .writeheader()
If a field is empty or not declared, it's written as an empty string.
If a row contains fields not declared in fieldnames, ValueError is thrown.
"""

with open("csv_write_sample.csv", "w") as f:
    f_csv = csv.DictWriter(f, fieldnames=["app", "sizeMB", "author"])
    f_csv.writeheader()
    f_csv.writerow({"app": "Flatseal", "sizeMB": 1.4, "author": "tchx84"})
    f_csv.writerow({"app": "OBS Studio", "sizeMB": 528.5, "author": "obsproject"})

 