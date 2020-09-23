'''
Takes two lists, returns only elements that are common for both lists
without duplicates.
Extras:
1. Randomly generate two lists
2. Write in one line(bruh)
'''

import random

a = sorted(random.sample(range(100), k = (random.randint(8,12))))
b = sorted(random.sample(range(100), k = (random.randint(8,12))))

def common_list_maker(list_a, list_b):
    comm = []
    for i in list_a:
        if i in list_b:
            comm.append(i)
    return print(comm)

def common_set_maker(list_a, list_b):
    comm = set([])
    for i in list_a:
        if i in list_b:
            comm.add(i)
    return print(comm)

common_list_maker(a, b)
common_set_maker(a, b)