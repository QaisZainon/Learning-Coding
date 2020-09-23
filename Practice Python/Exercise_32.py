# Copy code from part 1 and part 2
# add features:
# user can guess 6 times, tells the user how many left
# keep track of letter user guessed, if letter already guessed, let them guess again, dont penalize

import random
# Picks a random word from scrabble dictionary
guess_num = 0
def word_picker():
    with open('Practice Python\Exercise_30.txt', 'r') as f:
        line = f.readlines()
    random_word = line[random.randint(1, len(line))].strip('\n')
    hangman(random_word)
# Core structure of the game
def hangman(random_word):
    print('Welcome to Hangman!')
    missing = ['_ ' for i in range(len(random_word))]
    while '_ ' in missing:
        print(''.join(missing))
        input_checker(missing, random_word)
        # word checker and updater
    print(''.join(missing))
# Input Checker
def input_checker(missing, random_word):
    global guess_num
    guess = input('Wrong guess {}/6. Guess your letter: '.format(guess_num)).upper()
    if guess not in random_word:
        guess_num += 1
        if guess_num == 6:
            return print('\nYou used up all your tries\n')
        return print('\nWrong alphabet!\n')
    for i in range(len(random_word)):
        if guess == missing[i].strip(' '):
            return print('\nYou already guessed that word!\n')
        if random_word[i] == guess:
            missing[i] = guess + ' '

word_picker()