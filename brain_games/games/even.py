import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER, MAX_NUMBER = 1, 50


def is_even(number):
    return True if number % 2 == 0 else False


def generate_round():
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_even(question) else 'no'
    return question, correct_answer
