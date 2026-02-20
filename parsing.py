"""Exercises to manipulate files and how to parse them."""

import csv

from pathlib import Path
from datetime import datetime



def replace_char(text: str, char: list[str], new_char: str) -> str:
    """Replace all charcaters contain in char to text"""
    for c in char:
        text = text.replace(c, new_char)
    return text


# Exercise 4: Parsing functions (encapsulate ex 1, 2 and 3 inside functions)
def log_dict(log_list: list[str]) -> dict[str, str]:
    """Build a dictionary with a list"""
    
    try:
        log = {
            'IP': log_list[0],
            'id': log_list[1],
            'username': log_list[2],
            'date': log_list[3],
            'UTC': log_list[4],
            'request': log_list[5],
            'path': log_list[6],
            'protocol': log_list[7],
            'status': log_list[8],
            'size': log_list[9],
            }
    except IndexError:
        log = {
            'IP': log_list[0],
            'id': log_list[1],
            'username': log_list[2],
            'date': log_list[3],
            'UTC': log_list[4],
            'request': log_list[5],
            'path': log_list[6],
            'protocol': None,
            'status': log_list[7],
            'size': log_list[8],
            }
    return log

def parsing_log(log_list: list[list]) -> list[dict] :
    """Function to parse a log file, return a dict with parsing logs"""
    return [log_dict(log) for log in log_list]

def log_infos(parse_logs: list[dict]) -> list[tuple]:
    """Display a tuple with IP, date and status code for each dictionary in 
    the list in argument"""
    return [
    (log.get("IP"), log.get("date"), log.get("status")) for log in parse_logs
    ]

def clean_csv(csv_file) -> list[list]:
    """Clean and format an unformated CSV file"""
    data_list = [d for d in csv_file]
    data_strip = [[value.strip()  for value in line] for line in data_list]
    return data_strip

def write_clean_csv(row_list: list[list]) -> list[dict]:
    """Give list of dict with clean values"""
    data_result = [
        {
        'name': line[0],
        'age': line[1],
        'city': line[2],
        'salary': line[3],
        }
        for line in row_list]
    return data_result


# Exercise 1: Parse basic logs server
path = Path("")

with path.open(mode='r') as log_file:
    logs = log_file.readlines()
    logs_split = [
        replace_char(log, ['"', '[', ']', '\n'], '').split(' ') for log in logs
        ]

    #logs_list = []
    result = parsing_log(logs_split)


# Exercise 2: Extract IPs, dates and status codes

logs_infos = log_infos(result)
for log in logs_infos:
    print(log)


# Exercise 3: Handle a non formated csv to return a formated file

path = Path("")
new_path = Path("")

with path.open(mode='r') as csv_file:
    data = [line.replace(';', ',') for line in csv_file]
    reader = csv.reader(data)
    next(reader)
    data_list = clean_csv(reader)

    with new_path.open(mode='w') as new_csv:
        fieldnames = ['name', 'age', 'city', 'salary']
        writer = csv.DictWriter(new_csv, fieldnames=fieldnames)
        writer.writeheader()
        data_result = write_clean_csv(data_list)
        writer.writerows(data_result)


# Exercise 5: Handle different formated date

def check_format(date: str):
    """Check the date format"""
    formats = [
        "%d/%b/%Y:%H:%M:%S %z",
        "%Y-%m-%d %H:%M:%S",
        "%d/%m/%Y",
        "%b %d, %Y",
        "%Y%m%d",
    ]
    for format in formats:
        try:
            if datetime.strptime(date, format):
                return datetime.strptime(date, format)
        except ValueError:
            continue
    return None

def normalized_date(date: datetime) -> str:
    """Noramlisation of the date passed in argument"""
    return date.strftime("%Y-%m-%d %H:%M:%S")


dates = [
    "15/Oct/2007:13:55:36 -0700",   # Apache format (ex: logs)
    "2022-02-02 09:45:23",          # ISO 8601 format (standard)
    "02/02/2022",                   # European format
    "Feb 2, 2022",                  # English format
    "20220202",                     # Compact format
]

formated_dates = []
for element in dates:
    date_format = check_format(element)
    if date_format is None:
        print("Sorry, this format is not supported.")
    else:
        formated_dates.append(normalized_date(date_format))

for d in formated_dates:
    print(d)
    
        



    



   

