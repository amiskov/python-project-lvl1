from random import randint
from brain_games.games.game_types import Game

rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def create_game() -> Game:
    n = randint(1, 101)
    return str(n), 'yes' if n % 2 == 0 else 'no'
