from selenium import webdriver


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