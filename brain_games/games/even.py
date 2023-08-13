import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 50


def generation_game():
    random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
    correct_answer = 'yes' if random_number % 2 == 0 else 'no'
    return random_number, correct_answer
