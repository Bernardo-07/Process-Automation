import pyautogui
import pyperclip
import time 
import os

pyautogui.PAUSE = 1

#abre o navegador
os.system("start msedge.exe")
time.sleep(2)

#digita o endereço e entra no drive
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(2)

#navega até o local do relatório e entra na pasta Exportar
pyautogui.click(x=171, y=270, clicks=2) #coordenadas encontradas a partir do comando pyautogui.position()
time.sleep(1)

#faz o donwload do relatório
pyautogui.click(x=171, y=270)
time.sleep(1)
pyautogui.click(x=1097, y=106)