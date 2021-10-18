from random import randint

rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def question():
    return randint(1, 101)


def check_even(n: int) -> str:
    if n % 2 == 0:
        return 'yes'
    else:
        return 'no'
