'''
Generate a random number
Asks the user to guess the number
tell them whether they guessed it too high, too low or exactly right
Extras:
1. keep going until user types exit
2. keep track of how many guesses taken until game ends
'''

import random

def guess_game():
    while True:
        rand_num = random.randint(1,9)
        guess = ''
        guess_counter = 0
        while guess != rand_num:
            print('Guesses taken : ', guess_counter)
            guess = int(input('Guess a number between 1 and 9\n'))
            guess_counter += 1
            if guess > rand_num:
                print('Your guess number is too high!')
            elif guess < rand_num:
                print('Your guess number is too low!')
        print('Correct! The random number is {}. It took you {} tries!'.format(rand_num, guess_counter))
        Exit = input('Type \'quit\' to exit from the game\n')
        if Exit == 'quit':
            break

guess_game()
