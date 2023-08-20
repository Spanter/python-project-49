import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def generation_game():
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return question, correct_answer
