from operator import mul, add, sub
from random import randint, choice

rules = 'What is the result of the expression?'
calc_operators = {"*": mul, "+": add, "-": sub}


def question():
    op_str, op_fn = choice(list(calc_operators.items()))
    a = randint(1, 101)
    b = randint(1, 101)
    return f"{a} {op_str} {b}"


def evaluate_str_expression(str_expression: str) -> int:
    """
    Returns the result of a given string-encoded expression:

    >>> evaluate_str_expression("12 + 3")
    15
    >>> evaluate_str_expression("15 - 5")
    10
    >>> evaluate_str_expression("5 * 5")
    25
    """
    [a, op_str, b] = str_expression.split(" ")
    op = calc_operators[op_str]
    return op(int(a), int(b))
