import pyautogui
import pyperclip
import time 
import os
import pandas as pd

pyautogui.PAUSE = 1

#abre o navegador
os.system("start msedge.exe")
time.sleep(5)

#digita o endereço e entra no drive
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(6)

#navega até o local do relatório e entra na pasta Exportar
pyautogui.click(x=367, y=321, clicks=2) #coordenadas encontradas a partir do comando pyautogui.position()
time.sleep(1)

#faz o donwload do relatório
pyautogui.click(x=367, y=321)
time.sleep(1)
pyautogui.click(x=496, y=219)
time.sleep(6)

tabela = pd.read_excel(r"C://Users/berna/Downloads/Vendas - Dez.xlsx")
print(tabela)
faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()

#entra no email
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(8)

#enviar por email o resultado
pyautogui.click(x=90, y=171)
time.sleep(2)
pyautogui.write("pythonimpressionador+diretoria@gmail.com")
pyautogui.press("enter")
pyautogui.press("tab")
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v") 
pyautogui.press("tab")
texto = f"Prezados, bom dia!\nO faturamento de ontem foi de: R$ {faturamento:,.2f}\nA quantidade de produtos foi de: {quantidade:,.0f}\n\nAtt.,\nBernardo Duarte"
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ctrl", "enter")
