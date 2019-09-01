from selenium import webdriver
from PIL import Image


def create_url_screenshot(name, url):
    print('Create screenshot for {}'.format(url))
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.add_argument("--headless")
    driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=options)  
    #driver.set_window_size(1920, 1080, driver.window_handles[0])
    driver.set_window_size(1440, 900, driver.window_handles[0])

    driver.get(url)
    filename = 'static/screenshots/{}.png'.format(name.lower())
    driver.save_screenshot(filename)
    driver.close()
    print('Screenshot saves as {}'.format(filename))
    
    print('Generating thumbnail...')
    image = Image.open(filename)
    size = (288, 180)
    image.thumbnail(size, Image.ANTIALIAS)
    thumbnail_filename = 'static/screenshots/{}_tn.png'.format(name.lower())
    image.save(thumbnail_filename)
    print('Thumbnail {} created.'.format(thumbnail_filename))