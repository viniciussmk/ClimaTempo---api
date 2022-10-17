from base64 import encode
from datetime import datetime
from encodings import utf_8
import yagmail 
import requests
import json
import encodings


iTOKEN = "d9bbc6a7572c24d2c14dd5f44299340a"
iCIDADE = "4235"

iTIPOCONSULTA = 1

#1=Tempo agora na cidade
if iTIPOCONSULTA == 1:
    iURL = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/" + iCIDADE + "/current?token=" + iTOKEN
    iRESPONSE = requests.request("GET", iURL)
    iRETORNO_REQ = json.loads(iRESPONSE.text)
    print("Chamando: ")

contatos = [('Vinicius', 'E-mail', '17/10')]
dataAtual = datetime.now().strftime('%d/%m')
emailServer = yagmail.SMTP('E-mail', 'Senha')

for nome in contatos:
        if nome[2] == dataAtual:
            emailServer.send(nome[1], subject= 'Clima de hoje (ALERT)', contents= ["Hoje o clima está: "] + [iRETORNO_REQ])
        else:
            print("Não está na data de hoje...")