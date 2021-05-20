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
tk = input("Nhap tai khoan: ")
password = stdiomask.getpass()
sbd = int(input("So bao danh: "))

browser  = webdriver.Chrome(chrome_options=option, executable_path="C:/Users/nguye/Downloads/chromedriver_win32/chromedriver.exe")

browser.get("http://facebook.com")

sleep(2)

# 2a. Điền thông tin vào ô user và pass

txtUser = browser.find_element_by_id("email")
txtUser.send_keys(tk)

txtPass = browser.find_element_by_id("pass")
txtPass.send_keys(password)

# 2b. Submit form

txtPass.send_keys(Keys.ENTER)

sleep(3)

linkPost = [
    "temp",
    "https://www.facebook.com/C3KT-PROM-NIGHT-756654841191844/photos/pcb.1549372048586782/1549361721921148",
    "https://www.facebook.com/C3KT-PROM-NIGHT-756654841191844/photos/pcb.1549372048586782/1549361828587804",
    "https://www.facebook.com/C3KT-PROM-NIGHT-756654841191844/photos/pcb.1549372048586782/1549362111921109",
    "https://www.facebook.com/C3KT-PROM-NIGHT-756654841191844/photos/pcb.1549372048586782/1549360701921250",
    "https://www.facebook.com/C3KT-PROM-NIGHT-756654841191844/photos/pcb.1549372048586782/1549360438587943",
    "https://www.facebook.com/C3KT-PROM-NIGHT-756654841191844/photos/pcb.1549372048586782/1549360411921279",
    "https://www.facebook.com/C3KT-PROM-NIGHT-756654841191844/photos/pcb.1549372048586782/1549360628587924",
    "https://www.facebook.com/C3KT-PROM-NIGHT-756654841191844/photos/pcb.1549372048586782/1549362748587712"
]
browser.get(linkPost[sbd])

sleep(4)

emotion = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div[1]/div/span/div/span[1]/span/span")
emotion.click()


urlFb = []
nameFb = []

fdasdf = input('Press ENTER to continute...')

user_list = browser.find_elements_by_xpath("//div[@class='ue3kfks5 pw54ja7n uo3d90p7 l82x9zwi a8c37x1j']")

print('Tong so like: ', len(user_list))
print('LOADING...')

typeAccount = []

id = 1

for user in user_list:
    user = user.find_elements_by_class_name('qzhwtbm6.knvmm38d')
    
    curUser = user[0]

    if(len(user) == 1): typeAccount.append('Clone')
    else: typeAccount.append('Real')

    xPath = "//div[@class='q5bimw55 rpm2j7zs k7i0oixp gvuykj2m j83agx80 cbu4d94t ni8dbmo4 eg9m0zos l9j0dhe7 du4w35lb ofs802cu pohlnb88 dkue75c7 mb9wzai9 l56l04vs r57mb794 kh7kg01d c3g1iek1 otl40fxz cxgpxx05 rz4wbd8a sj5x9vvc a8nywdso']/div[@class='j83agx80 cbu4d94t buofh1pr l9j0dhe7']/div[" + str(id) + "]//div[@class='q9uorilb']"
    test = curUser.find_element_by_xpath(xPath)
    element = test.find_element_by_tag_name('a')
    nameFb.append(curUser.text)
    urlFb.append(element.get_attribute('href'))

    id += 1

Data = {'Name': nameFb,
        'Facebook link': urlFb,
        'Real or Clone': typeAccount
        }
df = pd.DataFrame(Data, columns = ['Name', 'Facebook link', 'Real or Clone'])
fileName = 'C:/Users/nguye/Desktop/' + str(sbd) + '.xlsx'
df.to_excel (fileName, index = False, header=True)

print('DONE!!!')

sleep(3)

browser.close()
