'''
Take the shell from exercise 17, put it all into a text file
Ask the user to specify the file name
'''
from bs4 import BeautifulSoup 
import requests

name = input('Write the file name\n') + '.txt'
open_file = open(name, 'w')
url = 'https://www.nytimes.com/'
r = requests.get(url)
r.raise_for_status()
soup = BeautifulSoup(r.text, 'html.parser')
title2 = soup.findAll('h2')
title3 = soup.findAll('h3')
for item in title2:
    a = item.text.strip() + '\n'
    open_file.write(a)
for item in title3:
    a = item.text.strip() + '\n'
    open_file.write(a)
open_file.close()