# transforms the set into .json files
#import json 
#birthday_dict = {
#    'Albert Einstein' : '14/03/1879',
#    'Benjamin Franklin' : '17/01/1706',
#    'Ada Lovelace' : '10/12/1815'
#    }
#with open('Practice Python\Birthdaynames.json', 'w') as f:
#    json.dump(birthday_dict, f)

# do the exercise 33 but instead using json files
# make it so that you can add new names and birthdays
import json
def birthday():
    print('Welcome to the birthsay dictionary. We know the birthdays of :')
    with open('Practice Python/Birthdaynames.json','r') as f:
        birthday_dict = json.load(f)
    for i in birthday_dict:
        print(i)
    input_ = input('Who\'s birthday do you want to look up?\n')
    if input_ not in birthday_dict:
        ans = input('This name is not in the birthday dictionary. Do you want to add this into the dictionary? (y/n)\n')
        if ans == 'y':
            birthday = input('What is his/her birthday?\n')
            birthday_dict[input_] = birthday
            with open('Practice Python/Birthdaynames.json','w') as f:
                json.dump(birthday_dict, f)
            print('Disctionary updated!')
    else:
        print('{}\'s birthday is {}'.format(input_, birthday_dict[input_]))
birthday()