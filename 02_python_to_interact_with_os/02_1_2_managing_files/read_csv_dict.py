import csv

"""
Use DictReader to turn each row into a dictionary. 
Key = Column name. 
Value is empty string if cell is empty.
"""

with open('csv_file_with_header.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        
        print(row)
        if row['phone']:
            print("{} is a {}. Contact him/her via: {}".format(row['name'], row['role'], row['phone']))
        else:
            print("{} is a {}. No contact information available.".format(row['name'], row['role']))


    # field names
    print("fields:", reader.fieldnames)
    