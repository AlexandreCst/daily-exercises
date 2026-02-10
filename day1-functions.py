"""
Week 2 - Day 1: Python Functions
HackerRank Exercises

Exercises:
1. Write a function (is_leap)
2. Print Function
3. Find a string
4. String Validators
5. Mutations
"""


# ============================================
# EXERCISE 1: Write a function
# ============================================

def is_leap(year: int) -> bool:
    """
    Determine if a year is a leap year.
    
    Args:
        year (int): The year to check
        
    Returns:
        bool: True if leap year, False otherwise
    """
    if year % 400 == 0:
        return True
    
    if year % 100 == 0:
        return False
    
    if year % 4 == 0:
        return True
    
    return False


# ============================================
# EXERCISE 2: Print Function
# ============================================

def consecutive_numbers(n: int):
    """
    Display n consecutive numbers in line
    
    :param n: number, int
    """
    for i in range(1, n+1):
        print(i, end='')


# ============================================
# TESTS
# ============================================

if __name__ == "__main__":
    # Test Exercise 1
    print("\nExercise 1 - Leap Year:")
    print(is_leap(2000))  # True
    print(is_leap(1900))  # False
    print(is_leap(2024))  # True

    

    # Test Exercise 2
    print("\nExercise 2 - Print function:")
    consecutive_numbers(5) #12345
    print("\n")

    
