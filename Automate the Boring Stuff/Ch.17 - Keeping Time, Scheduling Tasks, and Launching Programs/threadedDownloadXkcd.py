#! python3
# threadedDownloadXkcd.py - Downloads XKCD comics using multiple threads.
# Major flaw for this program is that the URL denies entry due to =
# Failed to establish a new connection: [Errno 11001] getaddrinfo failed
import requests, os, bs4, threading, time
os.makedirs('xkcd', exist_ok = True)  # store comics in ./xkcd
def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page.
        print('Downloading page https://xkcd/%s...' % (urlNumber))
        res = requests.get('https://xkcd/%s' % (urlNumber))
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        # Find the URL of the comic image.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            # Download the image
            print('Downloading the image %s...' % (comicUrl))
            res = requests.get('https:' + comicUrl)
            res.raise_for_status()
            # Save the image to ./xkcd.
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
# Create and start the Thread objects
downloadThreads = []  # a list of all the Thread objects
for i in range(0, 140, 10):  # loops 14 times, creates 14 threads
    start = i
    end = i + 9
    if start == 0:
        start = 1  # There is no comic 0, set it to 1.
    downloadThread = threading.Thread(target = downloadXkcd, args = (start, end))
    downloadThreads.append(downloadThread)
    downloadThread.start()
# Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()  # forces the parent thread to stop and wait for other threads
print('Done.')