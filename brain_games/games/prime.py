import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def generation_game():
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    counter = 1
    for i in range(2, question // 2 + 1):
        if question % i == 0:
            counter += 1
    correct_answer = 'yes' if counter <= 1 else 'no'
    return question, correct_answer
