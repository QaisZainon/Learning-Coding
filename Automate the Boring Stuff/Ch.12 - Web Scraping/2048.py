from selenium import webdriver
from selenium.webdriver.common.keys import Keys

Browser = webdriver.Firefox()
Browser.get('https://gabrielecirulli.github.io/2048/')
AutoPlay = Browser.find_element_by_tag_name('html')

while True:
    AutoPlay.send_keys(Keys.UP)
    AutoPlay.send_keys(Keys.RIGHT)
    AutoPlay.send_keys(Keys.DOWN)
    AutoPlay.send_keys(Keys.LEFT)
    try:
        TryAgain = AutoPlay.find_element_by_link_text('Try again')
        TryAgain.click()
    except:
        continue
