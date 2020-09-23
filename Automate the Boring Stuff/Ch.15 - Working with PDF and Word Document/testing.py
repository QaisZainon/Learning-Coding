import PyPDF2

pdfFile = open('dummy.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()
for pageNum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
pdfOutputFile = open('abject_pw.pdf', 'wb')
pdfWriter.encrypt('abject')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdfFile.close()