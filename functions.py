"""Python Functions assignment """

from typing import Union
from functools import reduce
from datetime import datetime
"""
1. You need to write a function that will convert the specified number to the specified number system.
The function takes two arguments as input: a number and a number system.

Expected output:
    B13
    101100010011
"""


def convert_to(num: int, base: int) -> Union[str, int]:
    """Converts a number to its equivalent representation in the specified base."""
    if base == 10:
        return num
    elif base == 16:
        eq_num = hex(num)
    elif base == 2:
        eq_num = bin(num)
    elif base == 8:
        eq_num = oct(num)
    else:
        return f"{base} is unknown system number :(  !!"
    return eq_num[2:].upper()


print(convert_to(2835, 16))
print(convert_to(2835, 2))

##############################################################
print('----'*25)

"""
2. You need to write a function of recursion list sum.
The function takes a list as input.

Expected output:
    30
"""


def sum_recursive_list(data: list) -> int:
    """Recursively sums all integers in a nested list."""
    rec_sum = 0
    for item in data:
        if isinstance(item, int):
            rec_sum += item
        elif isinstance(item, list):
            rec_sum += sum_recursive_list(item)
    return rec_sum


print(sum_recursive_list([1, 2, [3, 4], [5, 6, [2, 3, 4]]]))

##############################################################
print('----'*25)

"""
3. You need to write a Python program to find the greatest common divisor (gcd) of two integers.
The function takes two integer values as input.

Expected output:
    2
    5
    25
"""


def calculate_gcd(first_number: int, second_number: int) -> int:
    """Calculates the greatest common divisor (GCD) of two numbers."""
    while second_number != 0:
        temp = second_number
        second_number = first_number % second_number
        first_number = temp
    return first_number


print(calculate_gcd(12, 14))
print(calculate_gcd(15, 25))
print(calculate_gcd(75, 25))

##############################################################
print('----'*25)

"""
4. You need to write a function that returns the first n rows of Pascal's triangle.
Each number is the two numbers above it added together.
The function takes the number of triangle rows.

Expected output:
    [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1],
    ]
"""


def get_pascal_triangle(rows):
    """Generates Pascal's triangle up to the specified number of rows."""
    triangle = [[1]]
    for _ in range(rows - 1):
        last_row = triangle[-1]
        new_row = [1] + [last_row[i] + last_row[i + 1] for i in range(len(last_row) - 1)] + [1]
        triangle.append(new_row)
    return triangle


print(get_pascal_triangle(6))

##############################################################
print('----'*25)

"""
5. You need to write a program to find whether a given string starts with a given character using Lambda.
The function takes a word and a letter as input.

Expected output:
    True
    False
"""

starts_with = lambda string, char: string.startswith(char)
print(starts_with('Python', 'P'))
print(starts_with('Java', 'P'))

##############################################################
print('----'*25)

"""
6. You need to write a program to create Fibonacci series up to n using Lambda and reduce. It's a hard task.
The function takes as input the number of Fibonacci numbers to be calculated.

Expected output:
    [0, 1, 1, 2, 3, 5]
"""

fib_series = lambda n: reduce(lambda a, b: a + [a[-1] + a[-2]], [i for i in range(n - 2)], [0, 1])

print(fib_series(6))

##############################################################
print('----'*25)

"""
7. You need to write a program to find intersection of two given arrays using Lambda and filter.
You are given two lists, the result will be a list-intersection of the given ones.

Expected output:
    [1, 2, 8, 9]
"""

first = [1, 2, 3, 5, 7, 8, 9, 10]
second = [1, 2, 4, 8, 9]
result = list(filter(lambda item_from_second: item_from_second in first, second))
print(result)

##############################################################
print('----'*25)

"""
8. You need write a program to find palindromes in a given list of strings using Lambda and filter.
According Wikipedia - A palindromic number or numeral palindrome is a number that remains the same
when its digits are reversed. Like 16461, for example, it is "symmetrical".

Expected output:
    ['php', 'sagas', 'repaper', 'madam', 'level']
"""

words = ["php", "sagas", "Python", "abcdefg", "Java", "repaper", "madam", "level"]
result = list(filter(lambda word: word == word[::-1], words))
print(result)

##############################################################
print('----'*25)

"""
9.  You need to write a Python program to add three given lists using Python map and lambda.
You are given three lists, the result will be a list with numbers that are the sum of 
the first values of the given lists, the second values, the third...

Expected output:
    [12, 15, 18]
"""

nums_1 = [1, 2, 3]
nums_2 = [4, 5, 6]
nums_3 = [7, 8, 9]

# Add corresponding elements from three lists
result = list(map(lambda num_1, num_2, num_3: num_1 + num_2 + num_3, nums_1, nums_2, nums_3))

# Alternative way utilizing zip, sum and list comprehension
result2 = [sum(numbers) for numbers in zip(nums_1, nums_2, nums_3)]

print(result)
print(result2)

##############################################################
print('----'*25)

"""
10. You need a program to make a chain of function decorators (bold, italic, underline etc.).
Apply the string formatting that is given as input to the function.

Expected output:
    <b><i><u>Hello world</u></i></b>
"""


def make_bold(func):
    """Decorator to add HTML bold tags to the return value of a function."""
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper


def make_italic(func):
    """Decorator to add HTML italic tags to the return value of a function."""
    def wrapper():
        return f"<i>{func()}</i>"

    return wrapper


def make_underline(func):
    """Decorator to add HTML underline tags to the return value of a function."""
    def wrapper():
        return f"<u>{func()}</u>"
    return wrapper


@make_bold
@make_italic
@make_underline
def hello():
    """Function to return the string 'Hello world'."""
    return "Hello world"


print(hello())

##############################################################
print('----'*25)

"""
11. You need to implement a decorator that calculates the execution time of the function.

Expected output:
    sum_linear_progression finished in 0:00:28.791659 (*here is your time)
    500000000500000000
    sum_constant_progression finished in 0:00:00
    500000000500000000
"""


def timeit(func):
    """Decorator to measure the execution time of a function."""
    def wrapper(*args):
        start = datetime.now()
        func_result = func(*args)
        end = datetime.now()
        time = end - start
        print(f"{func.__name__} finished in {time}")
        return func_result

    return wrapper


# OR

class Timeit:
    """Class-based decorator to measure the execution time of a function."""
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        start = datetime.now()
        func_result = self.func(*args)
        end = datetime.now()
        time = end - start
        print(f"{self.func.__name__} finished in {time}")
        return func_result


@timeit
def sum_linear_progression(limit):
    """Calculates the sum of integers up to 'limit' in a linear progression."""
    return sum(range(limit + 1))


@timeit
def sum_constant_progression(limit):
    """Calculates the sum of integers up to 'limit' in a constant progression."""
    return limit * (limit + 1) // 2

# or


@Timeit
def sum_linear_progression_v2(limit):
    """Calculates the sum of integers up to 'limit' in a linear progression."""
    return sum(range(limit + 1))


@Timeit
def sum_constant_progression_v2(limit):
    """Calculates the sum of integers up to 'limit' in a constant progression."""
    return limit * (limit + 1) // 2


print("Using function decorator ")
print(sum_linear_progression(100_000_000))
print(sum_constant_progression(100_000_000))

print('--' * 25)
print("Using class decorator ")
print(sum_linear_progression_v2(100_000_000))
print(sum_constant_progression_v2(100_000_000))
