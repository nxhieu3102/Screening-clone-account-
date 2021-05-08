import pyautogui, sys
import time
from win32api import GetSystemMetrics


Width = GetSystemMetrics(0)
Height = GetSystemMetrics(1)

time.sleep(2)
pyautogui.moveTo(Width/2, Height/2)
time.sleep(0.5)

for i in range(0 , 100):
    pyautogui.scroll(-100000)
    time.sleep(0.5)
