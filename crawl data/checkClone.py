# Reading an excel file using Python
import xlrd
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyautogui, sys
from win32api import GetSystemMetrics
import pandas as pd
import getpass
import stdiomask
import math
 
# Give the location of the file

tk = input("Nhap tai khoan: ")
password = stdiomask.getpass()
sbd = int(input('sbd :'))

loc = ('C:/Users/nguye/Desktop/' + str(sbd) + '.xlsx')
 
# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
 
# For row 0 and column 0

nameFb = []
urlFb = []
typeAccount = []
check = []

soAccConLai = 999

for i in range(1 , sheet.nrows):
    nameFb.append(str(sheet.cell_value(i, 0)))
    urlFb.append(str(sheet.cell_value(i, 1)))
    typeAccount.append(str(sheet.cell_value(i, 2)))
    
if sheet.ncols == 4:
    for i in range(1 , sheet.nrows):
        check.append(sheet.cell_value(i , 3))
        if check[i - 1] == 1 : 
            soAccConLai = min(soAccConLai , i)

else :
    for i in range(1 , sheet.nrows):
        if typeAccount[i - 1] == 'Real': 
            check.append(1)
            soAccConLai = min(soAccConLai , i)
        else : check.append(0)

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2
})


browser  = webdriver.Chrome(chrome_options=option, executable_path="C:/Users/nguye/Downloads/chromedriver_win32/chromedriver.exe")

browser.get("http://facebook.com")

sleep(2)

txtUser = browser.find_element_by_id("email")
txtUser.send_keys(tk)

txtPass = browser.find_element_by_id("pass")
txtPass.send_keys(password)

# 2b. Submit form

txtPass.send_keys(Keys.ENTER)

sleep(3)

typeClone = ['Real' , 'Clone']

totalClone = 0


for i in range(0 , len(urlFb)):
    if check[i] == 1: break
    url = urlFb[i]
    browser.get(url)

    print("0 : Real")
    print("1 : Clone")
    print("2 : stop and save")

    t = str(input("Type : "))
    
    while t != '1' and t != '2' and t != '0':
        print("0 : Real")
        print("1 : Clone")
        print("2 : stop and save") 
        t = str(input("Again: "))
    
    t = int(t)

    if t == 2: 
        break
    else : 
        typeAccount[i] = typeClone[t]
        check[i] = 1

    if t == 1:
        totalClone += 1

    soAccConLai -= 1

    print("So acc con lai : " , soAccConLai)
    print("Tong acc clone : ", totalClone)
    

Data = {'Name': nameFb,
        'Facebook link': urlFb,
        'Type': typeAccount,
        'Check': check
        }

df = pd.DataFrame(Data, columns = ['Name', 'Facebook link', 'Type' , 'Check'])
fileName = 'C:/Users/nguye/Desktop/' + str(sbd) + '.xlsx'
df.to_excel (fileName, index = False, header=True)

sleep(2)

print("So acc con lai : " , soAccConLai)

print('Tong acc clone : ' , totalClone)

print('Ket Thuc !!')

sleep(2)

browser.close()