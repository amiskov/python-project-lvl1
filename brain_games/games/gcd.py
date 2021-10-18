from math import gcd
from random import randint

rules = "Find the greatest common divisor of given numbers."


def question():
    a = randint(1, 101)
    b = randint(1, 101)
    return f"{a} {b}"


def get_gcd(nums: str) -> int:
    """
    Returns the Greatest Common Divisor for the given string of two numbers:

    >>> get_gcd("25 5")
    5
    """
    [a, b] = nums.split(" ")
    return gcd(int(a), int(b))
