'''
Create a game of 'cows and bulls' with the user
Generate 4 random numbers
make a counter of cows and bulls
return cows if right amount and location
return bull if right amount but wrong location
return counter after each guess 
'''

import random
def cow_and_bull():
    num = [random.randint(1,9) for i in range(4)]
    guess = 0
    answer = []
    print(num)
    while True:
        cows = 0
        bulls = 0
        a = input('Try to the guess the 4 random integers\n')
        answer = [int(a[i]) for i in range(4)]
        for i in range(4):
            if answer[i] == num[i]:
                cows += 1
            elif answer[i] in num:
                bulls += 1
        guess += 1
        if answer == num:
            print('Congratulations for guessing it correctly!It took you {} guess(es)'.format(guess))
            break
        print('Guesses taken {}. Cows:{} Bulls:{}'.format(guess, cows, bulls))


cow_and_bull()