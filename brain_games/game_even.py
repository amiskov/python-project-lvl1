import prompt
from random import randint

YES_ANSWER = "yes"
NO_ANSWER = "no"


def is_even(n: int) -> bool:
    return n % 2 == 0


def is_answer_correct(n: int, answer: str) -> bool:
    if is_even(n) and answer == YES_ANSWER:
        return True
    elif not is_even(n) and answer == NO_ANSWER:
        return True
    else:
        return False


def run_game(attempts: int, name: str) -> None:
    print('Answer "yes" if the number is even, otherwise answer "no".')
    game(attempts, name)


def get_correct_answer(n: int) -> str:
    if n % 2 == 0:
        return YES_ANSWER
    else:
        return NO_ANSWER


def game(attempts: int, name: str) -> None:
    if attempts == 0:
        return print(f"Congratulations, {name}!")

    question = randint(0, 100)
    print(f"Question: {question}")
    answer = prompt.string("Your answer: ")

    if is_answer_correct(question, answer):
        print("Correct!")
        return game(attempts - 1, name)
    else:
        print(f"'{answer}' is wrong answer ;(.",
              f"Correct answer was '{get_correct_answer(question)}'.")
        print(f"Let's try again, {name}!")
