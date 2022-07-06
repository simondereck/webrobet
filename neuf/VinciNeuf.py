from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from random import randint
from time import sleep
from HwModels.NeufModel import NeufModel
from HwHelper.HwMySqlConnection import MySqlConnection

from HwRobortRequest.HwRequest import HwRequest


def getVilles():
    url = "https://www.vinci-immobilier.com/trouver-son-logement-neuf/toutes-les-villes"
    hwRequest = HwRequest()
    hwRequest.setUrl(url)
    result = hwRequest.getResult()
    soup = BeautifulSoup(result, 'lxml')
    links = soup.find_all("a", {"class": "CardLink_root__1f8GX CardLink_sticker__3OU3s"})

    with open('province.txt', 'a+') as f:
        for i in range(0, len(links)):
            href = links[i].attrs["href"]
            value = links[i].text
            f.writelines("%s\n" % href)
        f.close()


def getRegion():
    url = "https://www.vinci-immobilier.com/trouver-son-logement-neuf/toutes-les-regions"
    hwRequest = HwRequest()
    hwRequest.setUrl(url)
    result = hwRequest.getResult()
    soup = BeautifulSoup(result, 'lxml')
    links = soup.find_all("a", {"class": "CardLink_root__1f8GX CardLink_sticker__3OU3s"})

    with open('region.txt', 'a+') as f:
        for i in range(0, len(links)):
            href = links[i].attrs["href"]
            value = links[i].text
            f.writelines("%s %s\n" % (value, href))
        f.close()


def getProject():
    urlPrefix = "https://www.vinci-immobilier.com"
    conn = MySqlConnection()
    with open('region.txt', 'r') as f:
        lines = f.readlines()
        browser = webdriver.Firefox()
        for line in lines:
            print(urlPrefix + line)
            browser.implicitly_wait(60)
            browser.get(urlPrefix + line)
            try:
                browser.find_element_by_id('popin_tc_privacy_button_3').click()
            except Exception:
                print("new link")

            # pages = browser.find_elements_by_class_name("Pager_nb__24dYi")
            getItem(browser, conn)

            source = browser.page_source

            soup = BeautifulSoup(source, 'lxml')

            pages = soup.find_all("a", {"class": "Pager_nb__24dYi"})
            if pages:
                pages = pages[1:]
                for page in pages:
                    browser.get(urlPrefix + page["href"])
                    print("---- click page set ------")
                    getItem(browser, conn)

        f.close()


def getItem(browser: webdriver, conn: MySqlConnection):
    browser.implicitly_wait(60)
    SCROLL_PAUSE_TIME = 4

    # Get scroll height
    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # items = browser.find_element_by_class_name('ProgramGrid_ProgramGrid__34F1W').find_elements_by_class_name('ProgramCard_img__29vi5')
    # for item in items:
    #     item.click()
    #     # alink = item.find_elements_by_class_name("ProgramCard_link__2e-NJ")
    #     # print(alink)
    #     break

    flag = True
    while flag == True:
        try:
            source = browser.page_source

            soup = BeautifulSoup(source, 'lxml')
            grid = soup.find("div", {"class": "ProgramGrid_ProgramGrid__34F1W"})
            rows = grid.find_all("div", {"class": "ProgramCard_root__CBuEX"})
            links = grid.find_all("a", {"class": "ProgramCard_link__2e-NJ"})
            print(len(rows), "rows", len(links), "links")

            if len(rows) == len(links):
                flag = False
                for i in range(0, len(rows)):
                    try:
                        programe = {}
                        programe["name"] = rows[i].find("div", {"class": "ProgramCard_name__1t0JA"}).text
                        programe["location"] = rows[i].find("div", {"class": "ProgramCard_location__3Xaq8"}).text
                        programe["href"] = rows[i].find("a", {"class": "ProgramCard_link__2e-NJ"})["href"]
                        programe["style"] = rows[i].find("a", {"class": "ProgramCard_link__2e-NJ"})["style"]
                        programe["status"] = rows[i].find("div", {"class": "Pill_red__1TKZ9"}).text
                        programe["date"] = rows[i].find("span", {"class": "CommercialPhasePill_textSmall__3pUXY"}).text
                        neufModel = NeufModel()
                        neufModel.setModel(programe)
                        sql = neufModel.insertItem([])
                        print(sql)
                        conn.insert(sql)
                    except Exception:
                        print(i)
                        print(rows[i])
                        print(Exception)
        except:
            sleep(15)
            pass


def saveBuilding():
    pass


if __name__ == '__main__':
    # getVilles()
    # getRegion()
    getProject()
    pass
