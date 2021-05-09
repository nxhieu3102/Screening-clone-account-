from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyautogui, sys
from win32api import GetSystemMetrics
import pandas as pd
import getpass
import stdiomask

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2
})

#Đăng nhập tài khoản
browser  = webdriver.Chrome(chrome_options=option, executable_path="C:/Users/nguye/Downloads/chromedriver_win32/chromedriver.exe")
browser.get("https://id.atpsoftware.vn/")

linkFb = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/div/div/div[2]/form/div/input")
linkFb.send_keys("https://www.facebook.com/khanhduykt") 
sleep(1)
linkFb.send_keys(Keys.ENTER)

uid = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/div/div/div[2]/textarea")
print(uid.text)