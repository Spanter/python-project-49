import random

DESCRIPTION = 'What is the result of the expression?'
MIN_NUMBER, MAX_NUMBER = 1, 50
OPERATIONS = ('+', '-', '*')


def generate_round():
    first_num = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_num = random.randint(MIN_NUMBER, MAX_NUMBER)
    operation = random.choice(OPERATIONS)
    question = f'{first_num} {operation} {second_num}'
    match operation:
        case '+':
            correct_answer = first_num + second_num
            return question, str(correct_answer)
        case '-':
            correct_answer = first_num - second_num
            return question, str(correct_answer)
        case '*':
            correct_answer = first_num * second_num
            return question, str(correct_answer)
