import re

pattern = r'(\w+\s\d+) (\d{2}\:\d{2}:\d{2}) [\w\s\.]+(\[\d+\])'
line = 'Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)'

result = re.search(pattern=pattern, string=line)
print(result[1] + ' ' + result[2] + ' pid:' + result[3])