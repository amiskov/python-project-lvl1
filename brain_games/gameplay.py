import prompt
from typing import Callable
from brain_games.games.game_types import Game

ATTEMPTS = 3


def run(rules: str,
        create_game: Callable[[], Game],
        name: str) -> None:
    print(rules)

    def game(attempts):
        if attempts == 0:
            return print(f"Congratulations, {name}!")

        question, correct_answer = create_game()
        print(f"Question: {question}")

        answer = prompt.string("Your answer: ")

        if answer == correct_answer:
            print("Correct!")
            return game(attempts - 1)
        else:
            print(f"'{answer}' is wrong answer ;(.",
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")

    return game(ATTEMPTS)
