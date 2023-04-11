"""
Student name: Lea Grohmann
Date: 10/12/2022

Brief program overview (2-3 sentences)
MasterMind is a game that creates a secret four letter code where each letter represents a color
(color options: 'R' = red, 'G' = green, 'B' = blue, 'Y' = yellow, 'O' = orange, 'W' = white). Prompts
the player to guess the secret code and prints an evaluation of how close the guess was to the secret
code (evaluation: 'b' = correct letter in correct position, 'w' = correct letter in wrong position,
'-' = incorrect letter). The game finishes when the player guesses the secret code correctly
(i.e. when the result is 'bbbb')."""


import random


def make_random_code():
    """
    creates a secret four letter code that is a random combination of the
    letters 'R', 'G', 'B', 'Y', 'O', 'W'

    Arguments: none

    Returns:
        (string) - four letter code"""

    colors = ['R', 'G', 'B', 'Y', 'O', 'W']
    code = ''

    for i in range(4):
        code += random.choice(colors)

    return code


def count_exact_matches(string1, string2):
    """
    counts how many letters are exact matches between two strings, i.e. how many letters are the same letter and
    in the same position in both both strings

    Arguments:
        `string1` (string) - four letter string
        `string2` (string) - four letter string to be compared to string1
    
    Returns:
        (integer) - number of exact matches between string1 and string2"""
    
    exact_matches = 0

    for i in range(4):
        if string1[i] == string2[i]:
            exact_matches += 1

    return exact_matches


def count_letter_matches(string1, string2):
    """
    counts the letter matches between two strings, i.e. how many letters in the two strings are
    the same no matter the position of the letters

    Arguments:
        `string1` (string) - four letter string
        `string2` (string) - four letter string to be compared to string1
    
    Return:
        (integer) - letter matches between string1 and string2"""

    letter_matches = 0
    list1 = list(string1)
    list2 = list(string2)

    for letter in list1:
        if letter in list2:
            letter_matches += 1
            list2.remove(letter)

    return letter_matches


def compare_codes(code, guess):
    """
    evaluates the similarity of two four letter stings

    Arguments:
        `code` (string) - four letter string representing the secret code
        `guess` string) - four letter string representing the player's guess
    
    Returns:
        (string) contains four characters ('b' for every exact match, 'w'
                for every letter match, '-' for every non matching letter)"""
    
    black = count_exact_matches(code, guess)
    white = count_letter_matches(code, guess) - black
    blank = 4 - black - white
    
    return ('b' * black) + ('w' * white) + ('-' * blank)


def run_game():
    """
    starts and runs the Mastermind game, asking the player for their guess,
    prints the results, prints congratulations and stops the game when the player wins

    Arguments: none

    Returns: N/A"""

    print('New game.')
    code = make_random_code()
    moves = 0

    while True:
        guess = input('Enter your guess: ')
        result = compare_codes(code, guess)
        print('Result: ' + result)
        moves += 1

        if result == 'bbbb':
            print('Congratulations! You cracked the code in {} moves!'.format(moves))
            break
    

if __name__ == '__main__':
    run_game()

