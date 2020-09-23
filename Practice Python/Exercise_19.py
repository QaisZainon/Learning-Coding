'''
Using BS4 and requests to extract text form online news site
The news article has 4 pages
'''

from bs4 import BeautifulSoup
import requests

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r.raise_for_status()
soup = BeautifulSoup(r.text, 'html.parser')
text = soup.findAll('p')
for item in text:
    print(item.text.strip())