#User inputs a number between 1,100, the program tries to guess it
#using binary search, returns the guesses taken by the program

#Binary search-ish??
def num_guesser():
    low = 0
    high = 100
    guess = high / 2
    counter = 1
    condition = int(input('Is this your guess {}? (0 means its too low, 1 means its correct and 2 means too high!)\n'.format(guess)))
    while condition != 1:
        counter += 1
        if condition == 0:
            low = guess + 1
        elif condition == 2:
            high = guess - 1
        guess = round((low + high) / 2)
        condition = int(input('Is this your guess {}? (0 means its too low, 1 means its correct and 2 means too high!)\n'.format(guess)))
    print('It took {} times to guess your number'.format(counter))

num_guesser()