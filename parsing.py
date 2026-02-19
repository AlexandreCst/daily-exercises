"""Exercises to manipulate files and how to parse them."""

def replace_char(text: str, char: list[str]) -> str:
    """Replace all charcaters contain in char to text"""
    for c in char:
        text = text.replace(c, '')
    return text


from pathlib import Path

# Exercise 1 : Parse basic logs server
path = Path("")

with path.open(mode='r') as log_file:
    logs = log_file.readlines()
    logs_split = [replace_char(log, ['"', '[', ']', '\n']).split(' ') for log in logs]

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


    
