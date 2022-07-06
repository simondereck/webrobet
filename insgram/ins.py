import random
import instaloader

from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

url = "https://www.instagram.com"


browser = webdriver.Firefox()

browser.implicitly_wait(60)

browser.get(url)

buttons = browser.find_elements_by_class_name("bIiDR")

if len(buttons)>0:
    buttons[0].click()

sleep(4)

username = browser.find_element_by_name("username")
username.send_keys("0656759257")

password = browser.find_element_by_name("password")
password.send_keys("qq987654Z")

sleep(10)
loginButton = browser.find_elements_by_class_name("y3zKF")


if len(loginButton)>0:
    loginButton[0].click()

sleep(10)
comfirmButton = browser.find_elements_by_class_name("y3zKF")


if len(comfirmButton)>0:
    comfirmButton[0].click()
# fbs = browser.find_elements_by_class_name("sqdOP")

# if len(fbs)>0:
#     browser.execute_script("arguments[0].click();", fbs[0])

sleep(10)
confirmNotify = browser.find_element_by_class_name("HoLwm")
confirmNotify.click()

sleep(10)

search = browser.find_element_by_class_name("XTCLo")

search.send_keys("luxiaojunbarbell")

sleep(10)

linkShop = browser.find_element_by_class_name("-qQT3")

linkShop.click()

sleep(10)

linkShop = browser.find_elements_by_class_name("-nal3")

linkShop[1].click()


# scroll and get data
# isgrP
last_height = browser.execute_script("return document.getElementsByClassName('isgrP')[0].scrollHeight")

print(last_height)
i = 0
while i<10:
    sleep(10)
    browser.execute_script("document.getElementsByClassName('isgrP')[0].scrollTo(0, document.getElementsByClassName('isgrP')[0].scrollHeight);")
    new_height = browser.execute_script("return document.body.scrollHeight")
    # if new_height == last_height:
    #     break
    last_height = new_height
    i = i+1
    source = browser.page_source
    soup = BeautifulSoup(source, 'lxml')
    lis = soup.find_all("li",{"class":"wo9IH"})

#use instaloader to get username
print(len(lis))
L = instaloader.Instaloader()
profile = instaloader.Profile.from_username(L.context, 'profile1')