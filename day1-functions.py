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
# EXERCISE 3: Find a string
# ============================================

def count_substring(string: str, sub_string: str) -> int:
    """
    Count substring occurs in a given string
    
    :param string: Given string
    :param sub_string: Substring
    """
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count +=1
    return count

# ============================================
# EXERCISE 4: String validators
# ============================================

# Exercise + Test 
if __name__ == '__main__':
    s = 'qA2'
    print("Exercise 4 - String validators:")
    print(any(char.isalnum() for char in s)) # True
    print(any(char.isalpha() for char in s)) # True
    print(any(char.isdigit() for char in s)) # True
    print(any(char.islower() for char in s)) # True
    print(any(char.isupper() for char in s)) # True

# ============================================
# EXERCISE 5: Mutations
# ============================================

def mutate_string(string: str, position: int, character: str) -> str:
    """
    Mutate a string
    
    :param string: String
    :type string: str
    :param position: Position of character to mutate
    :type position: int
    :param character: Character to use
    :type character: str
    :return: New string
    :rtype: str
    """
    string_list = list(string)
    string_list[position] = character
    return ''.join(string_list)

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
    consecutive_numbers(5) # 12345

    # Test Exercise 3
    print("\n\nExercise 3 - Find a string:")
    string = "ABCDCDC".strip()
    sub_string = "CDC".strip()
    
    count = count_substring(string, sub_string) 
    print(count) # 2

    # Test Exercise 5
    print("\n\nExercise 5 - Find a string:")
    s = "abracadabra"
    i, c = 5, "k"
    s_new = mutate_string(s, int(i), c) 
    print(s_new) # abrackdabra

    
