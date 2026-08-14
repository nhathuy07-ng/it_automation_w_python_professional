import csv

# open and parse CSV file
f = open("csv_file.csv")
csv_f = csv.reader(f) # csv.Reader instance

for row in csv_f:
    # row: list[str]
    name, phone_number, role = row
    print("Name: {},\t Phone: {},\t Role: {}".format(name, phone_number, role))

f.close()