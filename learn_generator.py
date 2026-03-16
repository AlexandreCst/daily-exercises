"""Exercises to learn decorators"""

# =================================
# Exercise 1: Fibonacci generator
# =================================

def fibonacci():
    """Fibonacci with infinite generator"""
    n, m = 0, 1 # Initialization
    while True: # Create infinite loop
        yield n 
        n, m = m, n + m 

gen = fibonacci()

for i in range(2, 10):
    print(next(gen))