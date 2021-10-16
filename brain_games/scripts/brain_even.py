#!/usr/bin/env python
from brain_games.cli import welcome_user
from brain_games.game_even import run_game

ATTEMPTS = 3


def main():
    name = welcome_user()
    run_game(ATTEMPTS, name)


if __name__ == '__main__':
    main()
