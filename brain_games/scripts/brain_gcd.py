#!/usr/bin/env python
from brain_games.cli import welcome_user
from brain_games.gameplay import run
from brain_games.games.gcd import rules, question, get_gcd


def main():
    name = welcome_user()
    run(rules, question, get_gcd, name)


if __name__ == '__main__':
    main()
