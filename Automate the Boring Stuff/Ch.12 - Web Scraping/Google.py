import requests, sys, webbrowser, bs4, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
search_term = input('Enter what you want to search\n')
print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q={0}'.format(search_term), 'html.parser')
res.raise_for_status()
# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# Open a browser tab for each result.
a = 0
for i in soup.find_all('a'):
    webbrowser.open('http://google.com' + (i.get('href')))
    a += 1
    if a == 6:
        break