import random
numberOfStreaks = 0
printloop = 0
printlist = []
heads = 0
tails = 0

for experimentNumber in range(10000):
    randomnumber = random.randint(0,1)
    # Code that creates a list of 100 'heads or 'tails' values.
    if printloop != 100:
        if randomnumber == 0:
            printlist.append('H')
        if randomnumber == 1:
            printlist.append('T')
        printloop += 1
    # Code that checks if there is a streak of 6 heads or tails in a row.   
    if randomnumber == 0:
        heads += 1
        tails = 0
    elif randomnumber == 1:
        tails += 1
        heads = 0
    if heads == 6 or tails == 6:
        numberOfStreaks += 1
    
print(printlist)
print('Chance of streak: %s%%'% (numberOfStreaks /100))
