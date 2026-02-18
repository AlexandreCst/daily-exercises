"""Exercises to manipulate files and how to parse them."""

from pathlib import Path

# Exercise 1 : Parse basic logs server
path = Path("")

with path.open(mode='r') as log:
    for line in log:
        l = str(line).split('"')
        print(l)

    
