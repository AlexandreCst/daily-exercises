"""Exercises to learn decorators"""

from time import perf_counter

# ===================================
# Exercise 1: make @timer decorator
# ===================================

def timer(func): # Timer decorator
    def wrapper_timer(*args, **kwargs): # Wrapper of timer decorator
        start = perf_counter()
        value = func(*args, **kwargs)
        end = perf_counter()
        duration = end - start
        print(f"{func.__name__}() is executed in {duration:.6f}s")
        return value
    return wrapper_timer

@timer
def timer_test(n_iter):
    return sum([i**4 for i in range(n_iter)])

# ===================================
# TESTS
# ===================================

if __name__ == "__main__":

    # Exercise 1:
    timer_test(4)
    timer_test(400000)
