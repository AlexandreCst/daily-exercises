"""
Week 2 - Day 2: Advanced Python Functions
HackerRank Exercises

Topics: *args, **kwargs, lambda, map(), filter(), reduce()

Exercises:
1. Map and Lambda Function
2. Reduce Function
3. Validating Email with Filter
4. Any or All
5. ginortS (sorting)
"""

from fractions import Fraction
from functools import reduce

# ============================================
# EXERCISE 1: Map and Lambda Function
# ============================================

cube = lambda x: x**3

def fibonacci(n: int) -> list[int]:
    """
    Docstring for fibonacci
    
    :param n: Description
    :type n: int
    :return: Description
    :rtype: list[int]
    """
    fibonaccis = [0, 1]
    if n == 0:
        return []
    if n == 1:
        return [0]
    for _ in range(2, n):
        fibonaccis.append(fibonaccis[-2] + fibonaccis[-1])
            
    return fibonaccis

# ============================================
# EXERCISE 2: Reduce Function
# ============================================

def product(fracs):
    """
    Calculate the product of n fractions and return the numerator and denominator
    """
    t = reduce(lambda x, y: x * y, fracs)
    return t.numerator, t.denominator

# ============================================
# TESTS
# ============================================


if __name__ == '__main__':
    # Test Exercise 1
    n = 5
    print("Exercise 1 - Fibonacci's cubes:")
    print(list(map(cube, fibonacci(n)))) # [0, 1, 1, 8, 27]

    # Test Exercise 2
    fracs = [Fraction(1, 2), Fraction(3, 4), Fraction(10, 6)]
    result = product(fracs)
    print("\nExercise 2 - reduce function:")
    print(*result)