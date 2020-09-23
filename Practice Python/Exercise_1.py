'''
Ask the user to enter their name and their age
Print out a message addressed to them, telling them they will turn
100 years old
Extras:
1. ask a number and print the amount copies of the previous message
2. print it on seperate lines
'''

def question():
    name = input('Enter your name\n')
    age = input('Enter your age (numerial)\n')
    num = input('Enter how many times the mssage should be repeated (numerical)\n')
    future = (100 - int(age)) + 2020
    for i in range(int(num)):
        print('Your name is {} at the age of {}.You will turn 100 years old in {} years'.format(name, age, future))

question()