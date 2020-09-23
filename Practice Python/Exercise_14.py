'''
Write a function that returns a new list and contains all elements
of the first list minus all the duplicates
Extras:
1. Write two different functions - one using loop constructing a list, another using sets
2. Go back and do Exercise 5 using sets, write the solution using functions
'''
a = [1, 2, 6, 9, 2, 9]

def remover_loop(list):
    b = []
    for i in list:
        if i in b:
            break
        b.append(i)
    return print(b)

def remover_set(list):
    b = set(list)
    return print(b)

remover_loop(a)
remover_set(a)