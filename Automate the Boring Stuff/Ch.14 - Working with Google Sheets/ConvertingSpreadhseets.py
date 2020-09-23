import ezsheets
upload = ezsheets.upload(r'C:\Users\Dr. Wan Asna\Desktop\Python Projects\Automate the Boring Stuff\Ch.13 - Working with Excel Spreadsheets\example.xlsx')
upload.title = 'example.xlsx'
ss = ezsheets.Spreadsheet(upload.spreadsheetId)
ss.downloadAsODS('exampleODS.ods')
ss.downloadAsCSV('exampleCSV.csv')
ss.downloadAsPDF('examplePDF.pdf')
ss.downloadAsHTML('exampleHTML.html')