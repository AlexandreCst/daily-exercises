"""Some exercises to introduce regex"""

import re
from pathlib import Path


# =================================
# Exercise 1: Validate IP address
# =================================

ips = ["123.456.789.032", "0.0.0.0", "1.900..35", "hello", "95.123.21.687", "hello 95.123.21.687 world"]

regex = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"

for ip in ips:
    if re.search(regex, ip):
        print("This is a valid IP:", ip)


# ===================================================================================
# Exercise 2: parse IP, date, timezone, request, status code and size in server.log
# ===================================================================================

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


# ====================================
# Exercise 3: Date format validation
# ====================================

dates = [
    "15/Oct/2007:13:55:36 -0700",   # Apache format (ex: logs)
    "2022-02-02 09:45:23",          # ISO 8601 format (standard)
    "02/02/2022",                   # European format
    "Feb 2, 2022",                  # English format
    "20220202",                     # Compact format
]

regex = [
    r'^(?P<date>\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}\s[+-]\d{4})$',
    r'^(?P<iso>\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})$',
    r'^(?P<euro>\d{2}/\d{2}/\d{4})$',
    r'^(?P<english>\w{3}\s\d{0,2},\s\d{4})$',
    r'^(?P<compact>\w{8})$'
]

for date in dates:
    for r in regex:
        result = re.search(r, date)
        if result:
            print("Check formated date:", result.group())
            break


# ====================================
# Exercise 4: Clean data with re.sub
# ====================================

phones = [
    "+33 (0)6.12.34.56.75",
    "06-12-34-56-76",
    "06 12 34 56 77",
    "0612345678",
    "+33612345679",
]

phones_list = [re.sub(r'(\+33\s*\(0\)|\+33)',  '0', phone) for phone in phones]
raw_phones = [(''.join(re.findall(r'\d+', phone))) for phone in phones_list]

clean_phones = [
    re.sub(r'([0][6-7])(\d{2})(\d{2})(\d{2})(\d{2})', r'\1 \2 \3 \4 \5', phone) for phone in raw_phones
    ]

for phone in clean_phones:
    print("Phone number formatted:", phone)

        