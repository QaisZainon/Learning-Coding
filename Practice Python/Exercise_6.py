'''
Ask the users for a string and print out whether it is a palindrome or not
'''

def palindrome_checker():
    string = input('Check if a sentence is a palindrome\n')
    string2 = string[len(string) :-len(string)-1 :-1]
    if string == string2:
        print('This is a palindrome')
    else:
        print('That aint no palindrome')

palindrome_checker()