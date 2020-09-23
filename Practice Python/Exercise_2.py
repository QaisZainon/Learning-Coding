'''
Ask the user for a number
Check for even or odd
Print out a message for the user
Extras:
1. If number is a multiple of 4, print a different message.
2. Ask the users for two numbers, check if it is divisible, then 
print message according to the answer.
'''

def even_odd():
    num = int(input('Enter a number\n'))
    if num % 4 == 0:
        print('This number is divisible by 4')
    if num % 2 == 0:
        print('This is an even number')
    elif num % 2 == 1:
        print('This is an odd number')
    print('Give me two numbers,the first to check and the second to divide')
    check = int(input('Check number'))
    divide = int(input('Divider'))
    if num / divide == check:
        print('Correct!')
    else:
        print('Incorrect!')

even_odd()