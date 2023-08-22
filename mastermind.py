import random


COLORS = ['B', 'G', 'R', 'Y', 'W', 'P']
TRIES = 10
CODE_LEN = 4

def generate_code():
    '''Generate a random 4-letter code from the COLORS list'''
    code = []
    for i in range(CODE_LEN):
        code.append(random.choice(COLORS))
    return code


def get_guess():
    '''Get a valid guess from the user'''

    while True:
        guess = input('What is your guess? Type 4 letters with a space in between: ').upper().split(' ')

        if len(guess) != CODE_LEN:
            print(f'Invalid guess. Guess {CODE_LEN} colors')
            continue

        for color in guess:
            if color not in COLORS:
                print(f'Invalid guess. Guess one of colors: {COLORS}')
                break
        else:
            break

    return guess


def check_code(guess, real_code):
    '''Compare the guess to the real code and return the number of correct'''

    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code: # count the number of each color in the real code
        if color not in color_counts:
            color_counts[color ] = 0
        color_counts[color] += 1
    
    for guess_color, real_color in zip(guess, real_code): # check for correct colors in correct positions
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1

    for guess_color, real_color in zip(guess, real_code): # check for correct colors in incorrect positions
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos

def game():
    print(f'Welcome to Mastermind! Guess the code in {TRIES} tries!')
    print(f'Possible colors: {COLORS}')

    code = generate_code()
    for attempts in range(1, TRIES +1):
        guess = get_guess()
        correct_pos, incorrect_pos = check_code(guess, code)
        
        if correct_pos == CODE_LEN:
            print('You win!')
            break
        
        print(f'Correct colors in correct positions: {correct_pos} | Correct colors in incorrect positions: {incorrect_pos}')

    else:
        print(f'You lose! The code was: {code}')


if __name__ == '__main__':
    game()