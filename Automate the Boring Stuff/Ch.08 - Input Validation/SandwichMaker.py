import pyinputplus as pyip 
choice = ''
sandwich = list('')
def callsandwich():
    price = 0
    choice = pyip.inputYesNo('Do you want a sandwich?\n')
    if choice == 'no':
        print('Oh, okay :( ')
        return False
    #Main Selection
    Main = {
        'Bread':{'wheat': 1,'white': 1.25,'sourdough': 2},
        'Protein':{'chicken': 3,'turkey': 3.25,'tofu': 1.50},
        'Cheese':{'cheddar': 1,'swiss': 1.50,'mozarella': 1.50}
        }
    MainKey = list(Main.keys())
    MainDict = list(Main.values())
    for k in range(int(len(Main))):
        MainDict2 = MainDict[k]
        MainType = list(MainDict2.keys())
        MainPrice = list(MainDict2.values())
        print('What ' + MainKey[k] + ' do you want?')
        choice = pyip.inputMenu( MainType, numbered=True)
        sandwich.append(choice)
        price += MainPrice[k]
    #Add Ons Selection
    AddOns = {'mayo': 1,'mustard': 1.50,'lettuce':1,'tomato':1}
    for k, v in AddOns.items():
        choice = pyip.inputYesNo('Do you want ' + k + '\n')
        if choice == 'yes':
            price += v
            sandwich.append(k)
    #Total price,sandwich composition and sandwich amount
    print(('Your sandwich consists of ' + ', '.join(sandwich)).upper())
    print('That\'ll be  $ ' + str(price) + ' per sandwich')
    choice = pyip.inputInt('How many sandwiches would you want?\n', min = 1 )
    print('your total would be $ ' + str(price*int(choice)) + '\nHope you enjoy your sandwich(s)!!')

callsandwich()