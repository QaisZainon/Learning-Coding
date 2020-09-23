# Asks the user to enter a name, returns the birthday 

def birthday():
    birthday_dict = {
        'Albert Einstein' : '14/03/1879',
        'Benjamin Franklin' : '17/01/1706',
        'Ada Lovelace' : '10/12/1815'
        }
    print('Welcome to the birthsay dictionary. We know the birthdays of :')
    for i in birthday_dict:
        print(i)
    input_ = input('Who\'s birthday do you want to look up?\n')
    print('{}\'s birthday is {}'.format(input_, birthday_dict[input_]))

birthday()