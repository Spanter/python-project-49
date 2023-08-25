import random
import math


DESCRIPTION = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER, MAX_NUMBER = 1, 100


def generate_round():
    first_num = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_num = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{first_num} {second_num}'
    correct_answer = math.gcd(first_num, second_num)
    return question, correct_answer
