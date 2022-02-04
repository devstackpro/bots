import time
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options  
from webdriver_manager.chrome import ChromeDriverManager 

#Instanciando as options para o webdriver

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:/Users/Promoda/AppData/Local/Google/Chrome/User Data") 
options.add_argument("--profile-directory=Default")

driver = webdriver.Chrome(options=options,executable_path='X:/DEV/bots/whatsappEnvioDeArquivos_py/chromedriver.exe')

driver.get('https://web.whatsapp.com/') #abre o site Whatsapp Web - Não pode haver janelas do chrome abertas
time.sleep(15) #da um sleep de 15 segundos, tempo para scannear o QRCODE

contatos = ['Teste']

#Mensagem - Mensagem que sera enviada

mensagem = 'Bom dia '
mensagem2 = ' '
mensagem3 = ' Segue estoque atualizado. Boas vendas! <3'

#Midia = imagem, pdf, documento, video (caminho do arquivo, lembrando que mesmo no windows o caminho deve ser passado com barra invertida */* ) 

Arquivo1 = "x:/DEV/bots/whatsappEstoqueRepresentantes/Arquivo 1.png"
Arquivo2 = "x:/DEV/bots/whatsappEstoqueRepresentantes/Arquivo 2.png"
Arquivo3 = "x:/DEV/bots/whatsappEstoqueRepresentantes/Arquivo 3.png"
Arquivo4 = "x:/DEV/bots/whatsappEstoqueRepresentantes/Arquivo 4.png"
Arquivo5 = "x:/DEV/bots/whatsappEstoqueRepresentantes/Arquivo 5.png"
Arquivo6 = "x:/DEV/bots/whatsappEstoqueRepresentantes/Arquivo 6.png"

#Funcao que pesquisa o Contato/Grupo

def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(1)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

#Funcao que envia a mensagem

def enviar_mensagem(mensagem,mensagem2):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(str(mensagem) + str(mensagem2))
    campo_mensagem[1].send_keys(Keys.ENTER)
    campo_mensagem[1].send_keys(str(mensagem2) + str(mensagem3))
    campo_mensagem[1].send_keys(Keys.ENTER)

#Funcao que envia midia como mensagem

def enviar_midia(Arquivo1):
    driver.find_element_by_css_selector("span[data-icon='clip']").click()
    attach = driver.find_element_by_css_selector("input[type='file']")
    attach.send_keys(Arquivo1)
    time.sleep(3)
    send = driver.find_element_by_css_selector("span[data-icon='send']")
    send.click()   

def enviar_midia2(Arquivo2):
    driver.find_element_by_css_selector("span[data-icon='clip']").click()
    attach = driver.find_element_by_css_selector("input[type='file']")
    attach.send_keys(Arquivo2)
    time.sleep(3)
    send = driver.find_element_by_css_selector("span[data-icon='send']")
    send.click()   

def enviar_midia3(Arquivo3):
    driver.find_element_by_css_selector("span[data-icon='clip']").click()
    attach = driver.find_element_by_css_selector("input[type='file']")
    attach.send_keys(Arquivo3)
    time.sleep(3)
    send = driver.find_element_by_css_selector("span[data-icon='send']")
    send.click()   

def enviar_midia4(Arquivo4):
    driver.find_element_by_css_selector("span[data-icon='clip']").click()
    attach = driver.find_element_by_css_selector("input[type='file']")
    attach.send_keys(Arquivo4)
    time.sleep(3)
    send = driver.find_element_by_css_selector("span[data-icon='send']")
    send.click()   

def enviar_midia5(Arquivo5):
    driver.find_element_by_css_selector("span[data-icon='clip']").click()
    attach = driver.find_element_by_css_selector("input[type='file']")
    attach.send_keys(Arquivo5)
    time.sleep(3)
    send = driver.find_element_by_css_selector("span[data-icon='send']")
    send.click()   

def enviar_midia6(Arquivo6):
    driver.find_element_by_css_selector("span[data-icon='clip']").click()
    attach = driver.find_element_by_css_selector("input[type='file']")
    attach.send_keys(Arquivo6)
    time.sleep(3)
    send = driver.find_element_by_css_selector("span[data-icon='send']")
    send.click()   

#Percorre todos os contatos/Grupos e envia as mensagens

for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem,mensagem2)       
    enviar_midia(Arquivo1)
    time.sleep(1)
    enviar_midia2(Arquivo2)
    time.sleep(1)
    enviar_midia3(Arquivo3)
    time.sleep(1)
    enviar_midia4(Arquivo4)
    time.sleep(1)
    enviar_midia5(Arquivo5)
    time.sleep(1)
    enviar_midia3(Arquivo6)
    time.sleep(2)
    driver.quit()
    



