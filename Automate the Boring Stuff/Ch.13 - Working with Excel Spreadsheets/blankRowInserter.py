#! python3
# Inserts an empty row based on input
import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.active
row = int(input('Which row would you want to insert space?\n'))
space = int(input('How many spaces?\n'))
for i in range(space):
    sheet.insert_rows(row)
wb.save('blankRow.xlsx')
