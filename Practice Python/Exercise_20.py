'''
Takes an ordered list of numbers,(smallest to largest) and another number
Function decides whether or not the given number is inside the list and returns,
then returns a boolean
'''
import random
num_list = sorted([random.randint(1, 20) for i in range (12)])

def checker(list):
    num = int(input('Give me a number to check in the list\n'))
    if num in list:
        return True
    else:
        False

print(checker(num_list))

# Binary Search - answer given looks wack yo wtf
'''
def find(ordered_list, element_to_find):
    start_index = 1
    end_index = len(ordered_list) - 1

    while True:
        middle_index = int((end_index - start_index)/2)
        if middle_index < start_index or middle_index > end_index or middle_index < 0:
            return False
        
        middle_element = ordered_list[middle_index]
        if middle_element == element_to_find:
            return True
        elif middle_element < element_to_find:
            end_index = middle_index
        else:
            start_index = middle_index
    
find(num_list, 1)
'''