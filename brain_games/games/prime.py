from random import randint
from brain_games.games.game_types import Game

rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n) -> bool:
    """
    Returns `True` if `num` is a prime number:

    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(17)
    True
    >>> is_prime(22)
    False
    """
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def create_game() -> Game:
    n = randint(1, 101)
    return str(n), "yes" if is_prime(n) else "no"
