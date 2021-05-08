from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2
})

# 1. Khai bao bien browser
browser  = webdriver.Chrome(chrome_options=option, executable_path="C:/Users/nguye/Downloads/chromedriver_win32/chromedriver.exe")

# 2. Mở thử một trang web
browser.get("http://facebook.com")

# 2a. Điền thông tin vào ô user và pass

txtUser = browser.find_element_by_id("email")
txtUser.send_keys("ashluke329@gmail.com") # <---  Điền username thật của các bạn vào đây

txtPass = browser.find_element_by_id("pass")
txtPass.send_keys("1122334455")

# 2b. Submit form

txtPass.send_keys(Keys.ENTER)

sleep(3)

browser.get("https://www.facebook.com/asteri.theprom/photos/a.107675510963937/286668263064660")

sleep(4)

emotion = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div/div[1]/div/div[1]/div/span/div/span[1]/span/span")
emotion.click()

sleep(5)

user_list = browser.find_elements_by_xpath("//div[@data-visualcompletion='ignore-dynamic']")

#emotion_list = browser.find_elements_by_class_name('ue3kfks5 pw54ja7n uo3d90p7 l82x9zwi a8c37x1j')

for user in user_list:
    print("user: ", user)
    poster = user.find_element_by_class_name("a.oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p")
    #print(poster.text)

print("####################################")
print("Emotion:" , user_list)
print("Count: ", user_list.length)
