"""Some exercises to introduce regex"""

import re
from pathlib import Path

# Exercise 1: Validate IP address

ips = ["123.456.789.032", "0.0.0.0", "1.900..35", "hello", "95.123.21.687", "hello 95.123.21.687 world"]

regex = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"

for ip in ips:
    if re.search(regex, ip):
        print("This is a valid IP:", ip)


# Exercise 2: parse IP, date, timezone, request, status code and size in server.log
regex = r'''^                                                              # Start of string
            (?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s                   # IP adress
            (?P<id>\S+)\s                                                  # id
            (?P<username>\S+)\s                                            # Username
            (?P<date>\[\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}\s[+-]\d{4}\])\s # date & timezone
            (?P<req>"[^"]+")\s                                             # request
            (?P<status>\d{3})\s                                            # status code
            (?P<size>\d+)                                                  # size
            $                                                              # End of string
            '''

path = Path("server.log")

with path.open(mode='r') as log_file:
    for line in log_file:
        log = re.search(regex, line, re.VERBOSE)
        if log:
            print("IP:", log.group('ip'))
            print("ID:", log.group('id'))
            print("Username:", log.group('username'))
            print("Date and timezone:", log.group('date'))
            print("Request:", log.group('req'))
            print("Code status:", log.group('status'))
            print("Size:", log.group('size'))
            print("\n")


# Exercise 3: Date format validation
