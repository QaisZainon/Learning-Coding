#! python3
# ScheduledComicDw.py - Checks for new comics then downloads it if it hasnt been downloaded
import requests, os, bs4, logging, re
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.disable(logging.CRITICAL)
# Checks the file latest file name/number
for root, dirs, files in os.walk(
    r'Automate the Boring Stuff\Ch.17 - Keeping Time, Scheduling Tasks, and Launching Programs\ExtraOrdinary'
    , topdown = False
    ):
    logging.debug(files)
    dw_image_num = files[-1]
    logging.debug(dw_image_num)
# Going through the url to check the picture
url = 'https://www.exocomics.com'
res = requests.get(url)
res.raise_for_status()
# Beatiful Soup filter getting the image url
soup = bs4.BeautifulSoup(res.text, 'html.parser')
comicElem = soup.select('.image-style-main-comic')
logging.debug(comicElem)
comicUrl = comicElem[0].get('src')
logging.debug(comicUrl)
# Checking if the image is new or old based on existing image names
regex = re.findall(r'\d*', comicUrl)
regex = list(filter(None, regex))
logging.debug(regex)
if regex[0] == dw_image_num:
    print('Image already downloaded')
# Downloading the new image
else:
    print('Downloading image on ' + comicUrl)
    imageFile = open(os.path.join(
        r'Automate the Boring Stuff\Ch.17 - Keeping Time, Scheduling Tasks, and Launching Programs\ExtraOrdinary',
        regex[0] + '.jpg'), 'wb')
    res = requests.get(comicUrl)
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
