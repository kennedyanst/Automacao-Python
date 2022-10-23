#INTENSIVÃO DE PYTHON (AULA 1)
import time
import pyautogui
import pyperclip

#PASSO 1: Entrar no sistema da empresa.
pyautogui.PAUSE = 1
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

#PASSO 2: Navegar no sistema e encontrar a base de dados.
time.sleep(7)
pyautogui.click(x=322, y=290, clicks = 2)
time.sleep(3)

#PASSO 3: Fazer o Download da base de dados:
pyautogui.click(x=322, y=290, clicks = 1)
time.sleep(2)
pyautogui.click(x=1154, y=187, clicks = 1)
time.sleep(1)
pyautogui.click(x=926, y=625, clicks = 1)

#PASSO 4: Importar a base de dados para o python:
import pandas as pd
tabela = pd.read_excel(r'C:\Users\kenne\Downloads\Vendas - Dez.xlsx')

#PASSO 5: Calcular os indicadores:
faturamento = tabela['Valor Final'].sum()
quantidade = tabela['Quantidade'].sum()

#PASSO 6: Enviar um e-mail para o RESPONSAVEL com o relatório. 
pyautogui.hotkey('ctrl', 't')
pyautogui.write('gmail.com')
pyautogui.press('enter')
time.sleep(6)
pyautogui.click(x=60, y=207, clicks =1)
time.sleep(7)
pyperclip.copy('keke.218@gmail.com')
pyautogui.hotkey('ctrl', 'v')
time.sleep(3)
pyautogui.hotkey('tab')
time.sleep(3)
pyautogui.write('Resultados de planilha')# ASSUNTO
pyautogui.press('tab')
pyautogui.write(f"""Prezados, boa tarde!
Venho por meio deste e-mail compartilhar o resultado de faturamento
e quantidade de produtos vendidos. 

- FATURAMENTO: R$:{faturamento:,.2f}
- QUANTIDADE: {quantidade:,} Unidades.

Obrigado pela atenção. 

TE AMO, LAURA! Nem é tão dificil fazer sapoha. kkkk'
""")# TEXTO
pyautogui.hotkey('ctrl', 'enter')
