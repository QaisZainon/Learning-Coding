#! python3
# Finds an error in a spreadsheet 
import ezsheets
def Check_Error(ID_):
    print('Checking for Erros...')
    ss = ezsheets.Spreadsheet(ID_)
    sheet = ss[0]
    try:
        for int_ in range(2, len(sheet.getRows())):
            formula = int(sheet.getRow(int_)[0]) * int(sheet.getRow(int_)[1]) == int(sheet.getRow(int_)[2])
            if formula == False:
                print((sheet.getRow(int_)[0]) + ' * ' + (sheet.getRow(int_)[1]) + ' = ' + (sheet.getRow(int_)[2]))
    except:
        print('Finished!')

Check_Error('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')