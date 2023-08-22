import random

DESCRIPTION = 'What number is missing in the progression?'
MIN_NUMBER, MAX_NUMBER = 1, 50
MIN_STEP, MAX_STEP = 1, 9
MIN_LENGTH, MAX_LENGTH = 5, 10


def create_progression(sequence, step, length):
    list_progression = []
    for element in range(0, length):
        list_progression.append(str(sequence + element * step))
    return list_progression


def generate_round():
    sequence = random.randint(MIN_NUMBER, MAX_NUMBER)
    step = random.randint(MIN_STEP, MAX_STEP)
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    question_list = create_progression(sequence, step, length)
    hide_index = random.randint(0, len(question_list) - 1)
    correct_answer = question_list[hide_index]
    question_list[hide_index] = '..'
    question = ' '.join(question_list)
    return question, correct_answer
