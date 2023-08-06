import prompt


def get_start_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ').capitalize()
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)
    for correct_answer in range(3):
        question, correct_answer = game.generation_value()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ').lower()
        if correct_answer == user_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
