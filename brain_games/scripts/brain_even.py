#!/usr/bin/env python
from brain_games.cli import welcome_user
from brain_games.gameplay import run
from brain_games.games.even import rules, question, check_even


def main():
    name = welcome_user()
    run(rules, question, check_even, name)


if __name__ == '__main__':
    main()
