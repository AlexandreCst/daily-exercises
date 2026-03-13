"""Exercises to learn decorators"""

import logging
import functools

from time import perf_counter, sleep

# ===================================
# Exercise 1: make @timer decorator
# ===================================

def timer(func): # Timer decorator
    @functools.wraps(func)
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
        @functools.wraps(func)
        def wrapper_retry(*args, **kwargs):
            error = Exception()
            for _ in range(n):
                try:
                    value = func(*args, **kwargs)
                    return  value
                except Exception as e:
                    print("Error, retry...")
                    error = e
                    sleep(1)
            raise error
        return wrapper_retry
    return decorator_retry

count = 0

@retry(5)
def retry_test():
    global count
    while count < 2:
        count += 1
        raise ValueError
    return f"Success! Count = {count}"


# ======================================
# Exercise 3: make @log_call decorator
# ======================================

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")

console_handler = logging.StreamHandler()
console_handler.setLevel("DEBUG")
logger.addHandler(console_handler)

formatter = logging.Formatter(
    "{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M:%S"
)

console_handler.setFormatter(formatter)

def log_call(func):
    @functools.wraps(func)
    def wrapper_log_call(*args, **kwargs):
        value = func(*args, **kwargs)
        logger.debug(
            f"Positional argument(s): {args}, Keyword argument(s): {kwargs}, Return value: {value}"
            )
        return value
    return wrapper_log_call


@log_call
def test_my_call(*args, **kwargs):
    return args, kwargs


# ===================================
# TESTS
# ===================================

if __name__ == "__main__":

    # Exercise 1:
    print("Exercise 1:")
    timer_test(4)
    timer_test(400000)
    print(timer_test.__name__)
    print(timer_test.__doc__)

    # Exercise 2:
    print("\nExercise 2:")
    print(retry_test())
    print(retry_test.__name__)
    print(retry_test.__doc__)

    # Exercise 3:
    print("\nExercise 3:")
    test_my_call()
    test_my_call("Hello World!", "Decorator learning", formation="Python", semaine=4)
    print(test_my_call.__name__)
    print(test_my_call.__doc__)
