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

# ======================================
# Exercise 2: make @retry(n) decorator
# ======================================

def retry(n):
    def decorator_retry(func):
        def wrapper_retry(*args, **kwargs):
            for _ in range(n):
                value = func(*args, **kwargs)
            return value
        return wrapper_retry
    return decorator_retry

@retry(3)
def retry_test():
    print("Retry test")

# ===================================
# TESTS
# ===================================

if __name__ == "__main__":

    # Exercise 1:
    print("Exercise 1:")
    timer_test(4)
    timer_test(400000)

    # Exercise 2:
    print("\nExercise 2:")
    retry_test()
