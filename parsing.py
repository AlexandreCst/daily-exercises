"""Exercises to manipulate files and how to parse them."""

import csv

from pathlib import Path



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
path = Path("month-1-python-tools/exercises/weeks/server.log")

with path.open(mode='r') as log_file:
    logs = log_file.readlines()
    logs_split = [replace_char(log, ['"', '[', ']', '\n'], '').split(' ') for log in logs]

    #logs_list = []
    result = parsing_log(logs_split)


# Exercise 2: Extract IPs, dates and status codes

logs_infos = log_infos(result)
for log in logs_infos:
    print(log)


# Exercise 3: Handle a non formated csv to return a formated file

path = Path("month-1-python-tools/exercises/weeks/unformated_csv.csv")
new_path = Path("month-1-python-tools/exercises/weeks/formated_csv.csv")

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
        
        



    



   

