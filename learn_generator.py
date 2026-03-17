"""Exercises to learn decorators"""

import tracemalloc

from pathlib import Path

# =================================
# Exercise 1: Fibonacci generator
# =================================

def fibonacci():
    """Fibonacci infinite generator"""
    n, m = 0, 1 # Initialization
    while True: # Create infinite loop
        yield n # Lazy evaluation
        n, m = m, n + m
        print(n, m)


# =========================================
# Exercise 2: Read file by line generator
# =========================================

def file_by_line(path="docs/pipeline.log"): # Generator read the file line by line
    """Generator to read a file line by line and save RAM use"""
    path = Path(path) # Define path
    
    with path.open(mode="r") as file:
        for line in file:
            yield line # Line lazy evaluation

def file_readlines(path="docs/pipeline.log"): # Load the data directly in Memory
    """Function that load the entire file in RAM to compare with the generator"""
    path = Path(path) # Define path
    with path.open(mode="r") as file:
        lines = file.readlines() # Get all line in the file
        return lines


# ===================================
# TESTS
# ===================================

if __name__ == "__main__":

    # Exercise 1
    gen = fibonacci() # Generator declaration

    for i in range(10): # Print the first number of the Fibonacci sequence
        print(next(gen))

    # Exercise 2
    tracemalloc.start() # Start tracing memory allocation
    file = file_readlines() # Run classic function
    func_snapshot = tracemalloc.take_snapshot()
    fun_size = tracemalloc.get_traced_memory()
    tracemalloc.stop() # Stop memory tracing


    tracemalloc.start() # Start tracing memory
    for line in file_by_line(): # Run generator
        print(line)
    gen_snapshot = tracemalloc.take_snapshot()
    gen_size = tracemalloc.get_traced_memory()
    tracemalloc.stop() # Stop memory tracing

    print(f"Function memory allocation: {fun_size}")
    print(f"Generator memory allocation: {gen_size}")

    
