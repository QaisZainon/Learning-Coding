'''
Take a list, print out all the elements that are less than 5
Extras:
1. instead of printing, make a new list, then only print it out
2. Write this in one line of Python
3. Ask the user for a number and return a list with only elements 
form the original list that are smaller than the number given  
'''

question_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def list_checker(list):
    num = int(input('Give me a number to check\n'))
    new_list = []
    for q in list:
        if q < num:
            new_list.append(q)
    return print(new_list)

list_checker(question_list)
