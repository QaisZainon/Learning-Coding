'''
Asks the user for a string with multiple words, return the string
backwards
'''

a = 'My name is John'
def backwards(string):
    string = string.split(' ')
    b = ' '.join(string[len(string): -len(string)-1: -1])
    return print(b)

backwards(a)