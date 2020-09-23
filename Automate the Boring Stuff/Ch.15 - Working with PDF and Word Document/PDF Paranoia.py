#! python3
# encrpyts PDF files in a folder
from pathlib import Path
import os, PyPDF2, shutil

def PDF_Encryption(folder, password):
    # Defining folder to move into for encrypted files
    directory = 'PDF_Encryption'
    path = os.path.join(Path.cwd(), directory)
    os.makedirs(path, exist_ok= True)
    # Goes through the folder specified
    for dirpath, dirnames, filenames in os.walk(folder):
        # Chooses only PDF files
        for filename in filenames:
            if filename.endswith('pdf'):
                print('Opening ' + filename + '...')
                pdfFileObj = open(dirpath + '\\' + filename, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
                pdfWriter = PyPDF2.PdfFileWriter()  # Opens empty shell for PDF
                # Copies the pdf into this shell
                for pageNum in range(pdfReader.numPages):
                    pageObj = pdfReader.getPage(pageNum)
                    pdfWriter.addPage(pageObj)
                # encrypting the PDF files
                print('Encrypting ' + filename + '...')
                pdfWriter.encrypt(password)
                # Changing the name of the file
                filename = filename.replace('.pdf', '')
                encryp_suffix = '_encrypted.pdf'
                filename = filename + encryp_suffix
                # Writing the shell into an actual PDF file
                pdfOutputFile = open(filename, 'wb')
                pdfWriter.write(pdfOutputFile)
                pdfOutputFile.close()
                pdfFileObj.close()
                # Move the encryption file into a folder
                print('Moving ' + filename + ' into ' + directory)
                movedfile = os.path.join(path, filename)
                shutil.move(filename, movedfile)

PDF_Encryption('PDF Paranoia', 'password')