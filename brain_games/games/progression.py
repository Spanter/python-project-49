import random

DESCRIPTION = 'What number is missing in the progression?'
MIN_NUMBER = 1
MAX_NUMBER = 50
MIN_STEP = 1
MAX_STEP = 9


def generation_game():
    sequence = random.randint(MIN_NUMBER, MAX_NUMBER)
    step = random.randint(MIN_STEP, MAX_STEP)
    generate_result = []
    for index in range(10):
        generate_result.append(str(sequence + index * step))
    hide_index = random.randint(0, 9)
    question_list = generate_result
    correct_answer = question_list[hide_index]
    question_list[hide_index] = '..'
    question = ' '.join(question_list)
    return question, correct_answer
