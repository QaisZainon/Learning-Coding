#! python3
# Reads text files, put them into lists and then input into an excel file
import openpyxl, os
def TextToExcel(folder):
    wb = openpyxl.Workbook()
    sheet = wb.active
    num_column = 0
    # Going through the file
    for foldername, subfolders, filenames in os.walk(folder):
        for fl_int in range(len(filenames)):
            filename = list(filenames)
            file_ = open(foldername + '\\' + filename[fl_int],'r')
            # Acquiring the text form .txt
            text_ = file_.readlines()
            text_ = text_[0].split(' ')
            for num_row in range(len(text_)):
                sheet.cell(row = num_row + 1, column = num_column + 1).value = text_[num_row]
                print(text_[num_row])
            num_column += 1
    wb.save('TextToExcel.xlsx')

TextToExcel(r'C:\Users\Dr. Wan Asna\Desktop\Python Projects\Automate the Boring Stuff\Ch.13 - Working with Excel Spreadsheets\num')