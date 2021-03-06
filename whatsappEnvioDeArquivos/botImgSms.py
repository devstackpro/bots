import os 
import time
import emoji
from os import close
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options  
from webdriver_manager.chrome import ChromeDriverManager 

#Instanciando as options para o webdriver
options = webdriver.ChromeOptions()

#options para manter conta do google logada com usuario principal
options.add_argument("--user-data-dir=C:/Users/MV002/AppData/Local/Google/Chrome/User Data") 
options.add_argument("--profile-directory=Default")


#comando para executar o Chromedrive
driver = webdriver.Chrome(options=options,executable_path='X:/DEV/bots/whatsappEnvioDeArquivos/chromedriver.exe')

 #abre o site Whatsapp Web - Não pode haver janelas do chrome abertas
driver.get('https://web.whatsapp.com/')

#da um sleep de 15 segundos, tempo para scannear o QRCODE
time.sleep(15) 

#Comando para buscar contatos e grupos do wpp
contatosProducao = ['Rudimar repDgb','Adriano Promoda','Cel Itj repDgb','Alessandro repDgb','Tufic repDgb',
            'Tiago repDgb','Eduardo DGB','Ronaldo  repDgb','Abrantes repDgb','Carlos repDgb','Igor repDgb',
                'Jon Willa repDgb','Paganini repDgb','Rodrigo Gonçalves repD gb','Mara repDgb','Renato Spama repDgb',
                 'Monica repDgb','Rodrigo Porto repDgb', 'DEV HOMOLOGAÇÃO']

contatosHomologacao = ['DEV HOMOLOGAÇÃO']
contatosEx = ['DEV EX']

#Mensagem - Mensagem que sera enviada
mensagem = 'Bom dia'
mensagem2 = ' '
mensagem3 = ' Segue estoque atualizado. Boas vendas! ;-) '
mensagem4 = ' erro bot DGB estoque pronta entrega representantes '

#Midia = imagem, pdf, documento, video (caminho do arquivo, lembrando que mesmo no windows o caminho deve ser passado com barra invertida */* ) 
Arquivo1 = "X:/capturaDeTelas/Arquivo_1.png"
Arquivo2 = "X:/capturaDeTelas/Arquivo_2.png"
Arquivo3 = "X:/capturaDeTelas/Arquivo_3.png"
Arquivo4 = "X:/capturaDeTelas/Arquivo_4.png"
Arquivo5 = "X:/capturaDeTelas/Arquivo_5.png"
Arquivo6 = "X:/capturaDeTelas/Arquivo_6.png"
verificarSuccess = ""

#Funcao que pesquisa o Contato/Grupo
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(1)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

#Funcao que envia a mensagem
def enviar_mensagem(texto1,texto2):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(str(texto1) + str(''))
    campo_mensagem[1].send_keys(Keys.ENTER)
    campo_mensagem[1].send_keys(str('') + str(texto2))
    campo_mensagem[1].send_keys(Keys.ENTER)

#Funcao que envia midia como mensagem
def enviar_midia(Arquivo_1):
    driver.find_element_by_css_selector("span[data-icon='clip']").click()
    attach = driver.find_element_by_css_selector("input[type='file']")
    attach.send_keys(Arquivo_1)
    time.sleep(3)
    send = driver.find_element_by_css_selector("span[data-icon='send']")
    send.click()   

def enviar_midia2(Arquivo_2):
    driver.find_element_by_css_selector("span[data-icon='clip']").click()
    attach = driver.find_element_by_css_selector("input[type='file']")
    attach.send_keys(Arquivo_2)
    time.sleep(3)
    send = driver.find_element_by_css_selector("span[data-icon='send']")
    send.click()   

def enviar_midia3(Arquivo_3):
    driver.find_element_by_css_selector("span[data-icon='clip']").click()
    attach = driver.find_element_by_css_selector("input[type='file']")
    attach.send_keys(Arquivo_3)
    time.sleep(3)
    send = driver.find_element_by_css_selector("span[data-icon='send']")
    send.click()   

def enviar_midia4(Arquivo_4):
    driver.find_element_by_css_selector("span[data-icon='clip']").click()
    attach = driver.find_element_by_css_selector("input[type='file']")
    attach.send_keys(Arquivo_4)
    time.sleep(3)
    send = driver.find_element_by_css_selector("span[data-icon='send']")
    send.click()   

def enviar_midia5(Arquivo_5):
    driver.find_element_by_css_selector("span[data-icon='clip']").click()
    attach = driver.find_element_by_css_selector("input[type='file']")
    attach.send_keys(Arquivo_5)
    time.sleep(3)
    send = driver.find_element_by_css_selector("span[data-icon='send']")
    send.click()   

def enviar_midia6(Arquivo_6):
    driver.find_element_by_css_selector("span[data-icon='clip']").click()
    attach = driver.find_element_by_css_selector("input[type='file']")
    attach.send_keys(Arquivo_6)
    time.sleep(3)
    send = driver.find_element_by_css_selector("span[data-icon='send']")
    send.click()  

#Verificando arquivo success para envio das mensagens 
try:
    verificarSuccess = open('X:\capturaDeTelas\success.txt')     
    verificarSuccess.close()

#caso nao teja o arquivo succes sera acionado a mensagen de erro
except:
     log = 'ERRO: Arquivo success.txt nao existe'

if(verificarSuccess): 
    
#Percorre todos os contatos/Grupos e envia as mensagens e fotos
    for  contato in contatosHomologacao: 
        buscar_contato(contato)
        enviar_mensagem(mensagem,mensagem3) 
        time.sleep(2)      
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
        
#comando para mandar mensagens de erro caso os arquivos nao forem enviado   
else: 
    
    for  contato in contatosEx: 
        buscar_contato(contato)
        enviar_mensagem(mensagem4,log)

    print('success nao existe')
    driver.close()

#fechar google chorome 
driver.close()














