import random

DESCRIPTION = 'What number is missing in the progression?'
MIN_NUMBER, MAX_NUMBER = 1, 50
MIN_STEP, MAX_STEP = 1, 9
MIN_LENGTH, MAX_LENGTH = 5, 10


def is_progression(sequence, step, length):
    generate_list = []
    for index in range(length):
        generate_list.append(str(sequence + index * step))
    return generate_list


def generation_game():
    sequence = random.randint(MIN_NUMBER, MAX_NUMBER)
    step = random.randint(MIN_STEP, MAX_STEP)
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    question_list = is_progression(sequence, step, length)
    hide_index = random.randint(0, len(question_list) - 1)
    correct_answer = question_list[hide_index]
    question_list[hide_index] = '..'
    question = ' '.join(question_list)
    return question, correct_answer
