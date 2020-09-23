import ezsheets
ss = ezsheets.Spreadsheet('13yWHAM906aCkUFceCDXOOmXifihnadVeYnoTwfess-c') #  Change ID to specific ID
sheets = ss.sheets[0]
email = sheets.getColumn(2)
while('' in email):
    email.remove('')
print(email)
