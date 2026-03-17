"""Exercises to learn decorators"""

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


# ===================================
# TESTS
# ===================================

if __name__ == "__main__":

    # Exercise 1
    gen = fibonacci() # Generator declaration

    for i in range(10): # Print the first number of the Fibonacci sequence
        print(next(gen))