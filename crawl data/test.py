from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyautogui, sys
from win32api import GetSystemMetrics
import pandas as pd
import getpass
import stdiomask
import xlrd

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

soAccConLai = 9999

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

browser.get("https://www.facebook.com/")
sleep(2)


txtUser = browser.find_element_by_id("email")
txtUser.send_keys(tk)

txtPass = browser.find_element_by_id("pass")
txtPass.send_keys(password)

# 2b. Submit form

txtPass.send_keys(Keys.ENTER)

sleep(2)

browser.get(urlFb[0])

window = Tk()
window.title("Check clone")
window.geometry("200x150")

# Thêm label
'''
lbl = tkinter.Label(window, text="Hello Mì AI", fg="red", font=("Arial", 50))
lbl.grid(column=0, row=0)

# Thêm textbox
txt = Entry(window, width=20)
txt.grid(column=0, row=1)
'''

id = 0

def saveAndStopButton():
    global id
    Data = {'Name': nameFb,
        'Facebook link': urlFb,
        'Type': typeAccount,
        'Check': check
        }
    df = pd.DataFrame(Data, columns = ['Name', 'Facebook link', 'Type' , 'Check'])
    fileName = 'C:/Users/nguye/Desktop/' + str(sbd) + '.xlsx'
    df.to_excel (fileName, index = False, header=True)
    browser.close()

def cloneButton():
    global id
    check[id] = 1
    typeAccount[id] = 'Clone'
    if id == len(urlFb) - 1: 
        lbl = tkinter.Label(window , text = "Hết rồi !!" ,fg="red", font = ("Arial" , 30))
        lbl.place(x = 70 , y = 150)
        sleep(2)
        saveAndStopButton()
        

def realButton():
    global id
    check[id] = 1
    typeAccount[id] = 'Real'
    if id == len(urlFb) - 1: 
        lbl = tkinter.Label(window , text = "Hết rồi !!" ,fg="red", font = ("Arial" , 30))
        lbl.place(x = 70 , y = 150)
        sleep(2)
        saveAndStopButton()

def nextAccButton():
    global id
    id += 1
    url = urlFb[id]
    browser.get(url)

def preAccButton():
    global id
    id -= 1
    url = urlFb[id]
    browser.get(url)


# Thêm button
clone = Button(window, text="Clone", command=cloneButton)
real = Button(window, text="Real", command=realButton)
saveAndStop = Button(window, text="Save and stop", command=saveAndStopButton)
nextAcc = Button(window , text = "Next account" , command=  nextAccButton)
preAcc = Button(window , text = "Previous account", command= preAccButton)

clone.place(x = 20 , y = 20)
real.place(x = 150 , y = 20)
saveAndStop.place(x =  100, y = 100)
nextAcc.place(x = 20 , y = 60)
preAcc.place(x = 120 , y = 60)

window.mainloop()
