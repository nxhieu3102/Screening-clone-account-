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
txtUser.send_keys(tk) # <---  Điền username thật của các bạn vào đây

txtPass = browser.find_element_by_id("pass")
txtPass.send_keys(password)

# 2b. Submit form

txtPass.send_keys(Keys.ENTER)

sleep(3)

linkPost = [
    "temp",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286676089730544/286671569730996",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286669693064517/286690639729089",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286676089730544/286671689730984",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286676089730544/286671233064363",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286669693064517/286668183064668",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286669693064517/286668343064652",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286669693064517/286755376389282",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286676089730544/286671373064349",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286676089730544/286671326397687",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286676089730544/286671499731003",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286676089730544/286671159731037",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286676089730544/286671179731035",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286669693064517/286668213064665",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286669693064517/286668289731324",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286669693064517/286668193064667",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286676089730544/286671473064339",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286669693064517/286668226397997",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286669693064517/286668349731318",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286676089730544/286671529731000",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286676089730544/286671583064328",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286676089730544/286671346397685",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286676089730544/286671513064335",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286669693064517/286668336397986",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286676089730544/286726856392134",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286676089730544/286671623064324",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286676089730544/286671649730988",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286669693064517/286668233064663",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286676089730544/286671683064318",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286676089730544/286671723064314",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286669693064517/286668263064660",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286676089730544/286671733064313",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286669693064517/286668413064645",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286676089730544/286671756397644",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286669693064517/286668429731310",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286669693064517/286668516397968",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286676089730544/286671823064304",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286669693064517/286668599731293",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286669693064517/286668479731305",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286669693064517/286826399715513",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286669693064517/286668476397972",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286669693064517/286668619731291",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286676089730544/286795356385284",
    "https://www.facebook.com/asteri.theprom/photos/pcb.286669693064517/286826876382132"    

]
browser.get(linkPost[sbd])

sleep(4)

emotion = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div/div[1]/div/div[1]/div/span/div/span[1]/span/span")
emotion.click()

sleep(5)

urlFb = []
nameFb = []


Width = GetSystemMetrics(0)
Height = GetSystemMetrics(1)

sleep(2)
pyautogui.moveTo(Width/2, Height/2)
sleep(0.5)

for i in range(0 , 35):
    pyautogui.scroll(-800)
    sleep(1.5)

for i in range(0 , 0):
    pyautogui.scroll(-800)
    sleep(3)

user_list = browser.find_elements_by_xpath("//div[@class='j83agx80 cbu4d94t ew0dbk1b irj2b8pg']")
user_list.pop(0)

typeAccount = []

id = 1

for user in user_list:
    if id == len(user_list) - 3:
        break
    
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


#print("Emotion:" , user_list)
#print("Count: ", user_list.length)