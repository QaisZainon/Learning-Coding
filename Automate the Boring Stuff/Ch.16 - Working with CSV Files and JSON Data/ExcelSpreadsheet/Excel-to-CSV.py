#! python3
# Excel-to-CSV.py - Converts Excel files to CSVs
import os, csv, openpyxl
os.makedirs('CSV_files', exist_ok = True)
for excelFile in os.listdir('.'):
    # Skip non xlsx files, load the workbook object.
    if not excelFile.endswith('.xlsx'):
        continue  # skip non-xlsx files
    wb = openpyxl.load_workbook(excelFile)  # opens choosen excel files
    filename = excelFile.replace('.xlsx', '_')
    # Loop through every sheet in the workbook.
    for sheetName in wb.sheetnames:
        # Create the CSV filename from the Excel filename and sheet title.
        filename = filename + sheetName + '.csv'
        # Create the csv.writer object for this CSV file.
        csvFile = open(os.path.join('CSV_files', filename), 'w', newline = '')
        csvWriter = csv.writer(csvFile)
        # Loop through every row in the sheet.
        sheet = wb[sheetName]
        for rowNum in range(1, sheet.max_row + 1):
            rowData = []  # append each cell to this list
            # Loop through each cell in the row.
            for colNum in range(1, sheet.max_column + 1):
                # Append each cell's data to rowData.
                cell = sheet.cell(row = rowNum, column = colNum).value
                rowData.append(cell)
            # Write the rowData list to the CSV file.
            csvWriter.writerow(rowData)
        csvFile.close()