# implement a function that takes the highest of three variables
# returns the largest of three without using max() function
# Use variables and ifs statements

def highest_num():
    print('Give me three numbers')
    first = int(input())
    second = int(input())
    third = int(input())
    highest = first
    if second > highest:
        highest = second
    if third > highest:
        highest = third
    print('The highest number is {}'.format(highest))

highest_num()