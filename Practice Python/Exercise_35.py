# load the JSON file from the disk
# extract the months of all the birthdays
# count how many scientist have birthdays in each month
import json
from collections import Counter
def date_extracter():
    with open('Practice Python/Birthdaynames.json','r') as f:
        birthday_dict = json.load(f)
    month = ['January', 'Febuary', 'March', 'April', 'May', 'June',
    'July', 'August','September', 'October', 'November', 'December']
    birthday_counter = []
    for i in birthday_dict:
        load = birthday_dict[i].split('/')
        birthday_counter.append(month[int(load[1]) - 1])
    print(Counter(birthday_counter))
date_extracter()