import pyautogui
import pyperclip
import time 
import os

pyautogui.PAUSE = 1

#abre o navegador
os.system("start msedge.exe")
time.sleep(5)

#digita o endereço e entra no drive
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")