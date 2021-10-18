from operator import mul, add, sub
from random import randint, choice
from brain_games.games.game_types import Game

rules = 'What is the result of the expression?'
calc_operators = {"*": mul, "+": add, "-": sub}


def create_game() -> Game:
    op_str, op_fn = choice(list(calc_operators.items()))
    a = randint(1, 101)
    b = randint(1, 101)
    return f"{a} {op_str} {b}", str(op_fn(a, b))
