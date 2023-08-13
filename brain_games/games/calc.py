import random

DESCRIPTION = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 50
OPERATIONS = ('+', '-', '*')


def generation_game():
    first_num = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_num = random.randint(MIN_NUMBER, MAX_NUMBER)
    oper = random.choice(OPERATIONS)
    question = f'{first_num} {oper} {second_num}'
    match oper:
        case '+':
            correct_answer = first_num + second_num
            return str(question), str(correct_answer)
        case '-':
            correct_answer = first_num - second_num
            return str(question), str(correct_answer)
        case '*':
            correct_answer = first_num * second_num
            return str(question), str(correct_answer)
