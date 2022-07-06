from time import sleep
from bs4 import BeautifulSoup
import json

from selenium.webdriver import ActionChains

from HwHelper.HwMySqlConnection import MySqlConnection
from HwModels.NeufModel import NeufModel
from selenium import webdriver


def arrayToTxt():
    pass

def getVinciItems():
    conn = MySqlConnection()
    model = NeufModel()
    sql = model.getAll()
    print(sql)
    items = conn.all(sql)
    urlPrefix = "https://www.vinci-immobilier.com"

    browser = webdriver.Firefox()
    # items = items[2:]
    for item in items:
        # try:
            itemModel = NeufModel()
            itemModel.id = item[0]

            print(urlPrefix + item[3])
            browser.get(urlPrefix + item[3])
            browser.implicitly_wait(60)

            try:
                browser.find_element_by_id('popin_tc_privacy_button_3')
                browser.find_element_by_id('popin_tc_privacy_button_3').click()
            except:
                print("new link")

            lis = browser.find_elements_by_class_name("ProgramSidebar_item__2lW45")

            if lis:
                lis[0].click()
                flag = True
                imagesContent = []

                while flag == True:
                    # try:
                        source = browser.page_source
                        soup = BeautifulSoup(source, 'lxml')
                        scrollDiv = soup.find("div",{"class":"GallerySlider_mini__3ssUM"})
                        imgs = scrollDiv.findAll("img")
                        for img in imgs:
                            imagesContent.append(img["src"])

                        print("size of images",len(imagesContent))
                        # 图片
                        itemModel.images = json.dumps(imagesContent)

                        try:
                            closeImage = browser.find_element_by_class_name("GalleryModal_close__3AEME")
                            browser.implicitly_wait(60)
                            ActionChains(browser).move_to_element(closeImage)
                            closeImage.click()
                        except Exception:
                            print("close error")
                            browser.refresh()
                            # browser.get(urlPrefix + item[3])
                            browser.implicitly_wait(60)

                        # print("closeImageItem",len(closeImage))
                        # for closeItem in closeImage:
                        #     closeItem.click()

                        addressDiv = soup.find("div",{"class":"ProgramBanner_address__2gHCb"})
                        addressInfo = addressDiv.find("address").find_all("div")

                        # 详细地址
                        itemModel.address_full = addressInfo[0].text


                        descButton = browser.find_element_by_class_name("ProgramAbout_readMore__2d-by")
                        ActionChains(browser).move_to_element(descButton).click(descButton)

                        desc = soup.find("div", {"class": "ProgramAbout_text__3b2QA"}).find("p").text

                        # 详情
                        itemModel.description = desc
                        print(desc)


                        updateSql = itemModel.updateDetail()
                        print(updateSql)
                        conn.update(updateSql)
                        # 获取房子
                        # tables = soup.find("table",{"class":"LotsByRooms_availableItems__3jvT9"})
                        #
                        # print(tables)
                        # tbodys = tables.findAll("tbody",{"class":"LotsByRooms_availableItem__ZZdM0"})


                        # houses = browser.find_elements_by_class_name("LotsByRooms_availableItemHeader__3jUE0")

                        # tbodys = browser.find_elements_by_class_name("LotsByRooms_availableItemContent__3CFjw")
                        # for item in tbodys:
                        #     print("item",item)
                        #     houses = item.find_elements_by_name("tr")
                        #     print("houses",houses)
                        #     for house in houses:
                        #         print("nnnn")
                        #         hosueButton = house.find_element_by_class_name("Button_border__1ZKsW")
                        #         ActionChains(browser).move_to_element(hosueButton).click(hosueButton)
                        #         # break
                        #     # break
                        #     pass

                        houseTypes = browser.find_elements_by_class_name("LotsByRooms_availableItemToggle__3fg2u")

                        if houseTypes:
                            for type in houseTypes:
                                print(123)
                                ActionChains(browser).move_to_element(type).click(type)
                                # pass
                                sleep(30)
                                break
                        else:
                            print("no data")


                        flag = False
                    # except Exception:
                    #     print(Exception)
                    #     print("something wrong here")
                    #     sleep(2)
                    #     browser.implicitly_wait(60)
                    #     pass
            # break

        # except Exception:
        #     print(Exception)
        #     pass

    browser.close()





if __name__ == '__main__':
    getVinciItems()
    pass