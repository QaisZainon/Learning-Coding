# make a hangman game?-ish
random_word = 'BALLISTOSPORES'
def hangman():
    print('Welcome to Hangman!')
    missing = ['_ ' for i in range(len(random_word))]
    while '_ ' in missing:
        print(''.join(missing))
        guess = input('Guess your letter: ').upper()
        # word checker and updater
        for i in range(len(random_word)):
            if random_word[i] == guess:
                missing[i] = guess + ' '
    print(''.join(missing))

hangman()