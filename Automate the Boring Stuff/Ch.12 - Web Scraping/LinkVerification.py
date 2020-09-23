#! python3
import requests, bs4
import pyinputplus as pyip
#Takes a URL from user
prompt = 'Enter a URL\n'
URL = pyip.inputStr(prompt, allowRegexes=[('^https://' + '.*')], blockRegexes=[('.*', 'Incorrect!')])
#attempts to download every linked page
URLPage = requests.get(URL)
soup = bs4.BeautifulSoup(URLPage.text, 'html.parser')
for link in soup.select('a'):
    href = str(link.get('href'))
    if 'https://' in href:
        TestLink = href
    elif 'http://' in href:
        TestLink = href
    else:
        TestLink = URL + href
    #flag pages that have a 404 'Not Found'
    try:
        DLTLink = requests.get(TestLink)
        DLTLink.raise_for_status()
        print(TestLink + ' is downloadable')
    except:
        print(str(TestLink) + ' unable to download')
