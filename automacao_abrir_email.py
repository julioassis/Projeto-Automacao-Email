import pyautogui
import time
#abrindo o navegador
pyautogui.PAUSE = 1
pyautogui.hotkey("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(4)

#abrindo a caixa de amail
pyautogui.write("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
pyautogui.press("enter")
time.sleep(8)
pyautogui.click(x=28, y=194)

time.sleep(4)
pyautogui.write("jhulyo_@outlook.com")
time.sleep(4)
pyautogui.press("tab")
pyautogui.press("tab")

#escrevendo o assunto do email
pyautogui.write("Fechamento do dia")
pyautogui.press("tab")

#escrevendo o corpo do email
texto = """Prezados, segue o fechamento dos valores de vendas
do dia, de acordo com a ID de cada colaborador.
Abrs
Julianyson Assis"""
pyautogui.write(texto)

#anexando arquivo
pyautogui.click(x=1427, y=1004)
time.sleep(2)
pyautogui.write("vendas")
time.sleep(1.5)
pyautogui.press("enter")
time.sleep(2)

#enviando email
time.sleep(3)
pyautogui.click(x=1304, y=1014)


#time.sleep(17)
#print(pyautogui.position())

