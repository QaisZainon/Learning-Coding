import ezsheets
ss = ezsheets.upload(r'C:\Users\Dr. Wan Asna\Desktop\Python Projects\Automate the Boring Stuff\Ch.13 - Working with Excel Spreadsheets\produceSales.xlsx')
sheet = ss[0]

print(sheet.getRow(1))
print(sheet.getRow(2))

print(sheet.getColumn(1))
print(sheet.getColumn('A'))

print(sheet.getRows(3))
sheet.updateRow(3, ['Pumpkin', '11.50', '20', '230'])
print(sheet.getRows(3))

columnOne = sheet.getColumn(1)
for i, value in enumerate(columnOne):
    # Make the Python list contain uppercase strings:
    columnOne[i] = value.upper()
sheet.updateColumn(1, columnOne)  # Update the entire column in one request
