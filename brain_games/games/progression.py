from random import randint

from brain_games.games.game_types import Game

rules = "What number is missing in the progression?"


def generate_progression(start, length, step):
    """
    Generates the sequence of numbers of a given `length`
    which begins from `start` increasing with the given `step`:

    >>> list(generate_progression(start=1, length=5, step=2))
    [1, 3, 5, 7, 9]
    """
    n = start
    count = 0
    while count < length:
        yield n
        n += step
        count += 1


def create_game() -> Game:
    start = randint(1, 101)
    length = randint(5, 11)
    step = randint(1, 11)
    absent_idx = randint(0, length - 1)
    p = list(map(str, generate_progression(start, length, step)))
    answer: str = p[absent_idx]
    p[absent_idx] = ".."
    return " ".join(p), answer
