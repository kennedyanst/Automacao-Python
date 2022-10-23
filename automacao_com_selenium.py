# INTENSIVÃO DE PYTHON (AULA 3)

# - AUTOMAÇÃO WEB E BUSCA DE INFORMAÇÕES COM PYTHON.

# Arquivo inicial e produtos na mesma pasta!


# PASSO 1: Entrar no google
# PASSO 2: Pesquisar a cotação do dolar
# PASSO 3: Pegar a cotação do dólar
# PASSO 4: Pegar a cotação do euro
# PASSO 5: Pegar a cotação do ouro
# PASSO 6: Atualizar a minha base de dados com novas cotações

# usar o selenium
# baixar webdriver

# !pip install selenium

# chrome webdriver: chromedriver
# verificar a versão do navegador para baixar o web driver.

# selenium funciona melhor no chrome ou firefox

# colocar o chromedrive na mesma pasta que está o python. (anaconda e pycharm)

# selenium espera o navegador ser criado e carregado para executar os comandos.

# Quando é uma automação 100% internet vai para o selenium
# O que é offline usa o pyautogui

#PASSO 1:
from selenium import webdriver #criar o navegador
from selenium.webdriver.common.by import By # Localizar elementos (os intens de um site)
from selenium.webdriver.common.keys import Keys #Permite clicar teclas no teclado

navegador = webdriver.Chrome()

navegador.get("https://www.google.com/")


#PASSO 2:
navegador.find_element(By.XPATH,
                       '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys{"Cotação dólar"}

navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

#PASSO 3:
cotacao_dolar = navegador.find_element(By.XPATH,
                                       '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attributed('data-value')

print(cotacao_dolar)


#PASSO 4:
navegador.get("https://www.google.com/")


navegador.find_element(By.XPATH,
                       '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys{"Cotação euro"}

navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_euro = navegador.find_element(By.XPATH,
                                       '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attributed('data-value')

print(cotacao_euro)


#PASSO 5:
navegador.get("https://www.melhorcambio.com/ouro-hoje")
cotacao_ouro = navegador.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(",",".")
print(cotacao_ouro)


#PASSO 6:
import pandas as pd

tabela = pd.read_excel("Produtos.xlsx")
display/print(tabela)
#tabela.loc["linha","coluna"]
#atualizar a cotação de acordo com a moeda correspondente.
#DOLAR
#as linhas onde a coluna moeda é igual a "dolar"
tabela.loc[tabela["Moeda"] == "Dólar","Cotação"] = float(cotacao_dolar)

#EURO
tabela.loc[tabela["Moeda"] == "Euro","Cotação"] = float(cotacao_euro)

#OURO
tabela.loc[tabela["Moeda"] == "Ouro","Cotação"] = float(cotacao_ouro)


#atualizar preço de compra = preço original * cotação.
tabela["Preço de Compra"] = tebela["Preço Original"] * tabela["Cotação"]


#atualizar preço de venda = preço de compra * margem.
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem*]
                                
print(tabela)

tabela ["Preço de vendas Atualizado"] = tabela["Preço de Compra"] * tabela["Margem"]


tabela.to_excel("Produtos Novos.xlsx", index=False)
navegador.quit()                                                              











