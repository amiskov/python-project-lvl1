from math import gcd
from random import randint
from brain_games.games.game_types import Game

rules = "Find the greatest common divisor of given numbers."


def create_game() -> Game:
    a = randint(1, 101)
    b = randint(1, 101)
    return f"{a} {b}", str(gcd(a, b))
