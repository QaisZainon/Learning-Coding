# Picks a random word from a list of words
import random
def word_picker():
    with open('Practice Python\Exercise_30.txt', 'r') as f:
        line = f.readlines()
    random_word = line[random.randint(1, len(line))].strip('\n')
    print(random_word)

word_picker()