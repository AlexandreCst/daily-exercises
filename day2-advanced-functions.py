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
# EXERCISE 3: Validating Email with Filter
# ============================================

def fun(s: str) -> bool:
    """
    Indicate if an adress mail is valid
    
    :param s: Adress to test
    :type s: str
    :return: True or False either the adress is valid or not
    :rtype: bool
    """
    # Check if there is an unique '@' in s
    if '@' not in s or s.count('@') != 1:
        return False
    
    # Split s in username and domaine + extension
    username, _, domain_and_ext = s.partition('@')
    
    # Check if username is not empty and if there is a point between the domain and the extension
    if not username or not '.' in domain_and_ext:
        return False
    
    # Split domain + extension in domain and extension
    domain, _, extension = domain_and_ext.partition('.')
    
    # Check if the domain is not empty and extension are valid (size and not empty)
    if not domain or not extension or len(extension) > 3:
        return False
    
    # Check if the format of the username is valid
    if any(c not in ['-', '_'] and not c.isalnum() for c in username):
        return False
    
    # Chek if the format of the domain is valid  
    if any(not c.isalnum() for c in domain):
        return False
    
    # Check if the format of the extension is valid
    if any(not c.isalpha() for c in extension):
        return False
        
    return True # return True if s is a valid email, else return False

def filter_mail(emails):
    return list(filter(fun, emails))


# ============================================
# EXERCISE 4: Any or All
# ============================================

# Look at the solution in test section

# ============================================
# EXERCISE 5: ginortS (sorting)
# ============================================

# Look at the solution in test section


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

    # Test Exercise 3
    emails = [
              "dheeraj-234@gmail.com", 
              "itsallcrap", 
              "harsh_1234@rediff.in",
              "kunal_shin@iop.az",
              "matt23@@india.in"
              ]
    
    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print("\nExercise 3 - valid email:")
    print(filtered_emails)

    # Test Exercise 4
    n = 5
    l = [12, 9, 61, 5, 14]
    print("\nExercise 4 - any palindromic integer?") # True -> 5
    print(all(i >= 0 for i in l) and any(str(x) == str(x)[::-1] for x in l))

    # Test Exercise 5
    s = 'Sorting1234'
    s_lower = sorted([c for c in s if c.islower()])
    s_upper = sorted([c for c in s if c.isupper()])
    s_odd = sorted([c for c in s if c.isdigit() and int(c) % 2 != 0])
    s_even = sorted([c for c in s if c.isdigit() and int(c) % 2 == 0])

    s_final = s_lower + s_upper + s_odd + s_even
    print("\nExercise 5 - Sorted list:")
    print(''.join(s_final))