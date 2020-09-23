#! python3
#Searches a image website with a specfic input and downloads the images into a folder
import requests, bs4, os, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.disable(logging.CRITICAL)
#Goes to a website, Im too lazy to specify the html for different websites so its only Imgur
Imgur = 'https://imgur.com/search?q='
os.makedirs('Images', exist_ok=True)
#Searches input
Search = input('Search Input\n')
SearchImgur = requests.get(Imgur + Search)
SearchImgur.raise_for_status()
soup = bs4.BeautifulSoup(SearchImgur.text, 'html.parser')
Image = soup.select('.image-list-link img')
logging.debug(Image)
#Downloads the images
for IndImage in Image:
    ImageUrl = 'http:' + IndImage.get('src')
    print('Downloading ' + ImageUrl + '...')
    DLImage = requests.get(ImageUrl)
    DLImage.raise_for_status()
    ImageFile = open(os.path.join('Images',os.path.basename(ImageUrl)),'wb')
    for chunk in DLImage.iter_content(100000):
        ImageFile.write(chunk)
    ImageFile.close()
print('Done')