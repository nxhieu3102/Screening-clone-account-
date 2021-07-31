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

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2
})

browser = webdriver.Chrome(chrome_options=option, executable_path="C:/Users/nguye/Downloads/chromedriver_win32/chromedriver.exe")

NameFb = []
UrlFb = []
TypeAccount = []
TypeClone = ['Real' , 'Clone']
check = []
id
Done = 1
Yet = 0

def openBrowserAndLogin():
    browser.get("http://facebook.com")
    sleep(5)

    UserName = input("Nhap tai khoan: ")
    PassWord = stdiomask.getpass()
    txtUserName = browser.find_element_by_id("email")
    txtUserName.send_keys(UserName)
    txtPassWord = browser.find_element_by_id("pass")
    txtPassWord.send_keys(PassWord)
    txtPassWord.send_keys(Keys.ENTER)

    sleep(5)

TotalAccountRemaing = 999;

def openAndLoadData():
    global id
    id = int(input('sbd :'))
    ExcelFileLocaiton = ('C:/Users/nguye/Desktop/' + str(id) + '.xlsx')
    WorkBook = xlrd.open_workbook(ExcelFileLocaiton)
    Sheet = WorkBook.Sheet_by_index(0)

    for i in range(1 , Sheet.nrows):
        NameFb.append(str(Sheet.cell_value(i, 0)))
        UrlFb.append(str(Sheet.cell_value(i, 1)))
        TypeAccount.append(str(Sheet.cell_value(i, 2)))

    if Sheet.ncols == 4:
        for i in range(1 , Sheet.nrows):
            check.append(Sheet.cell_value(i , 3))
            if check[i - 1] == Done : 
                TotalAccountRemaing = min(TotalAccountRemaing , i)
    else :
        for i in range(1 , Sheet.nrows):
            if TypeAccount[i - 1] == 'Real': 
                check.append(Done)
                TotalAccountRemaing = min(TotalAccountRemaing , i)
            else : check.append(0)

sleep(3)

TotalClone = 0

def processData():
    global TotalAccountRemaing, TotalClone
    for user in range(0 , len(UrlFb)):
        if check[user] == Done: break
        url = UrlFb[user]
        browser.get(url)

        print("0 : Real")
        print("1 : Clone")
        print("2 : stop and save")

        TypeAccountAfter = str(input("Type : "))
        
        while TypeAccountAfter != '1' and TypeAccountAfter != '2' and TypeAccountAfter != '0':
            print("0 : Real")
            print("1 : Clone")
            print("2 : stop and save") 
            TypeAccountAfter = str(input("Again: "))
        
        TypeAccountAfter = int(TypeAccountAfter)

        if TypeAccountAfter == 2: 
            break
        else : 
            TypeAccount[user] = TypeClone[TypeAccountAfter]
            check[user] = Done

        if TypeAccountAfter == Done:
            TotalClone += 1

        TotalAccountRemaing -= 1

        print("So acc con lai : " , TotalAccountRemaing)
        print("Tong acc clone : ", TotalClone)
    
def saveData():
    Data = {'Name': NameFb,
            'Facebook link': UrlFb,
            'Type': TypeAccount,
            'Check': check
            }

    df = pd.DataFrame(Data, columns = ['Name', 'Facebook link', 'Type' , 'Check'])
    ExcelFileLocaiton = ('C:/Users/nguye/Desktop/' + str(id) + '.xlsx')
    df.to_excel (ExcelFileLocaiton, index = False, header=True)

    sleep(2)

    print("So acc con lai : " , TotalAccountRemaing)

    print('Tong acc clone : ' , TotalClone)

    print('Ket Thuc !!')

    sleep(2)

    browser.close()

if __name__ == "__main__":
    openBrowserAndLogin()
    openAndLoadData()
    processData()
    saveData()
