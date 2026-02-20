"""Exercises to manipulate files and how to parse them."""

import csv

from pathlib import Path



def replace_char(text: str, char: list[str], new_char: str) -> str:
    """Replace all charcaters contain in char to text"""
    for c in char:
        text = text.replace(c, new_char)
    return text




# Exercise 1: Parse basic logs server
path = Path("")

with path.open(mode='r') as log_file:
    logs = log_file.readlines()
    logs_split = [replace_char(log, ['"', '[', ']', '\n'], '').split(' ') for log in logs]

    logs_list = []
    for log in logs_split:
        try:
            item = {
                'IP': log[0],
                'id': log[1],
                'username': log[2],
                'date': log[3],
                'UTC': log[4],
                'request': log[5],
                'path': log[6],
                'protocol': log[7],
                'status': log[8],
                'size': log[9],
                }
            logs_list.append(item)

        except IndexError:
            item = {
                'IP': log[0],
                'id': log[1],
                'username': log[2],
                'date': log[3],
                'UTC': log[4],
                'request': log[5],
                'path': log[6],
                'protocol': None,
                'status': log[7],
                'size': log[8],
                }
            logs_list.append(item)

# Exercise 2: Extract IPs, dates and status codes

ips_dates_codes = [
    (log.get("IP"), log.get("date"), log.get("status")) for log in logs_list
    ]
    
#for data in ips_dates_codes:
    #print(data)



# Exercise 3: Handle a non formated csv to return a formated file

path = Path("")
new_path = Path("")

with path.open(mode='r') as csv_file:
    data = [line.replace(';', ',') for line in csv_file]
    reader = csv.reader(data)
    next(reader)
    
    data_list = [d for d in reader]
    data_strip = [[value.strip()  for value in line] for line in data_list]


    with new_path.open(mode='w') as new_csv:
        fieldnames = ['name', 'age', 'city', 'salary']
        writer = csv.DictWriter(new_csv, fieldnames=fieldnames)
        writer.writeheader()
        data_result = []
        for line in data_strip:
            item = {
            'name': line[0],
            'age': line[1],
            'city': line[2],
            'salary': line[3],
            }
            data_result.append(item)
        writer.writerows(data_result)



    



   

