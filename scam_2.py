import pyautogui
import time

time.sleep(5)
count=0
while count<=8:
    pyautogui.typewrite("jai shree ram"+str(count))

    pyautogui.press("enter")
    count=count+1