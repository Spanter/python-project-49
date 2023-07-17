#!/usr/bin/env python3
import random
import prompt

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 50


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ').capitalize()
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for answer in range(3):
        random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        print(f'Question: {random_number}')
        user_answer = prompt.string('Your answer: ').lower()
        answer = 'yes' if random_number % 2 == 0 else 'no'
        if answer == user_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was "
                  f"'{answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
