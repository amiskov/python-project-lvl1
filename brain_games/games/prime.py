from random import randint
from brain_games.games.game_types import Game

rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num) -> bool:
    """
    Returns `True` if `num` is a prime number:

    >>> is_prime(1)
    False
    >>> is_prime(8)
    False
    >>> is_prime(2)
    True
    >>> is_prime(20)
    False
    >>> is_prime(17)
    True
    """
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num // 2):
            if num % i == 0:
                return False
            else:
                return True


def create_game() -> Game:
    n = randint(1, 101)
    return str(n), "yes" if is_prime(n) else "no"
