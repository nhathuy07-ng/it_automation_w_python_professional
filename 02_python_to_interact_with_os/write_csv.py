import csv

hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]

with open("hosts.csv", "w") as f:
    csv_f = csv.writer(f)
    for host in hosts:
        csv_f.writerow(host) # write one row at a time