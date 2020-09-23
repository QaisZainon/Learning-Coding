'''
Write a password generator 
'''

import random, string
def password_creator():
    password = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(12)])
    return print(password)

password_creator()