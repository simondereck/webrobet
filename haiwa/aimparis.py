from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from random import randint

from HwRobortRequest.HwRequest import HwRequest


class AimParis:
    def __init__(self):
        self.url = "https://www.amiparis.com/fr/sets/woman/new-womenswear-collection"
        # a) 女装全部产品
        # cette site juste utilise selenium

    def get_data(self):
        # hw_request = HwRequest()
        # hw_request.setUrl(self.url)
        # result = hw_request.getResult()
        # print(result)

        # step 1 get page by selenium
        # step 2 get get data div from selenium
        # step 3 get data
        # browser = webdriver.Firefox()
        browser = webdriver.Chrome()
        browser.implicitly_wait(60)
        browser.get(self.url)

        #laod more charge plus

        source = browser.page_source

        soup = BeautifulSoup(source, 'lxml')
        print(soup)


aim_paris = AimParis()
aim_paris.get_data()
