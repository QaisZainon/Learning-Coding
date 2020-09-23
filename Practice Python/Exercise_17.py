'''
Use BeatifulSoup and requests to print out a list of all the 
article titles on the New York Times homepage
'''
from bs4 import BeautifulSoup 
import requests

url = 'https://www.nytimes.com/'
r = requests.get(url)
r.raise_for_status()
soup = BeautifulSoup(r.text, 'html.parser')
title2 = soup.findAll('h2')
title3 = soup.findAll('h3')
for item in title2:
    print (item.text.strip())
for item in title3:
    print(item.text.strip())
