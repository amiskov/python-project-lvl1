import prompt
from typing import Callable

ATTEMPTS = 3


def run(rules: str,
        generate_question: Callable,
        get_correct_answer: Callable,
        name: str) -> None:
    print(rules)

    def game(attempts):
        if attempts == 0:
            return print(f"Congratulations, {name}!")

        question = generate_question()
        print(f"Question: {question}")

        answer = prompt.string("Your answer: ")
        correct_answer = get_correct_answer(question)

        if answer == str(correct_answer):
            print("Correct!")
            return game(attempts - 1)
        else:
            print(f"'{answer}' is wrong answer ;(.",
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")

    return game(ATTEMPTS)
