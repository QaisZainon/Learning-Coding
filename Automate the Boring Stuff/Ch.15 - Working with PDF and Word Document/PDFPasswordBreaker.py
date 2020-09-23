#! python3
# Password checker for a PDF File,
# on an assumption that the password is a single word
# and either full uppercase and lowercase
import PyPDF2
password = open('dictionary.txt', 'r')
password_txt = password.readlines()
pdfFile = open('abject_pw.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
for pw_index in range(len(password_txt)):
    pw_txt = password_txt[pw_index].replace('\n', '')
    pw_return1 = pdfReader.decrypt(pw_txt)
    pw_return2 = pdfReader.decrypt(pw_txt.lower())
    if pw_return1 == 1:
        print(pw_txt)
        break
    elif pw_return2 == 1:
        print(pw_txt.lower())
        break

