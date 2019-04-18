from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Driver:
    def __init__(self, is_headless):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        options = chrome_options if is_headless else None
        self.instance = webdriver.Chrome(options=options)
        self.instance.maximize_window()
    def navigate(self, url):
        if isinstance(url, str):
            self.instance.get(url)
        else:
            raise TypeError("URL must be a string")