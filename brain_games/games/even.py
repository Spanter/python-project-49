import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 50


def is_even(number):
    

def generation_game():
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return question, correct_answer
