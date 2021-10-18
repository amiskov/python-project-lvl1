#!/usr/bin/env python
from brain_games.cli import welcome_user
from brain_games.gameplay import run
from brain_games.games.calc import rules, create_game, evaluate_str_expression


def main():
    name = welcome_user()
    run(rules, create_game, evaluate_str_expression, name)


if __name__ == '__main__':
    main()
