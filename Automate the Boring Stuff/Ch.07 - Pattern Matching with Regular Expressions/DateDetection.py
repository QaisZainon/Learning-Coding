
import re
def DateDetection(Input):
    Date = re.compile(r'(\d{2})-(\d{2})-(\d{4})')
    Year = int(Date.search(Input).group(3))
    Month = int(Date.search(Input).group(2))
    Days = int(Date.search(Input).group(1))
    Monthrange30 = ['01', '03', '05', '07', '08', '10', '12']
    #Filtering non-valid dates
    if Year < 999 or Year > 3000:
        print('Invalid Year')
        False
    if Month not in range(1,12):
        print('Invalid Month')
        False
    if Days >= 32:
        print('Invalid Days')
        False
    #Filtering invalid days for specific months
    if Month == Monthrange30:
        if Days > 31:
            print('Invalid Days for Month ' + Month)
            False
    #Accounting for leap years in Febraury
    if Month == 2:
        if Year % 4 == 0:
            if Days >= 30:
                print('Invalid Days for February')
                False
    if Year % 100 == 0 and Year % 400 == 0:
            if Days >= 30:
                print('Invalid Days for February')
                False
    else:
        if Days >= 29:
            print('Invalid Days for Febraury')
            False

a = input()
DateDetection(a)
