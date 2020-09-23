
import re
def PasswordChecker(word):
    test1 = re.compile(r'[A-Z]')
    test2 = re.compile(r'[a-z]')
    test3 = re.compile(r'[0-9]')
    if int(len(word)) < 9:
        print('Password needs to be 8 characters long')
    elif test1.search(word) == None:
        print('Password needs to have an uppercase letter')
    elif test2.search(word) == None:
        print('Password needs to have an lowercase letter')
    elif test3.search(word) == None:
        print('Password needs to have one digit')
    else :
        print('Password accepted')

Password = input()
PasswordChecker(Password)