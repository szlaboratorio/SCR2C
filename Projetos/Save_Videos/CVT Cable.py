import cv2
import numpy as np
import time
from datetime import datetime
import os

video_ip_on = True
duracaoFilme = 10
fimGravacao= False

cap = cv2.VideoCapture()
cap.open(0)

caminho = r"/home/szlab/Desktop/Projetos"
destino = r"/home/szlab/Desktop/Projetos"

horaInicio = time.time()

now = datetime.now()
ano = int(now.strftime('%Y'))
mes = int(now.strftime('%m'))
dia = int(now.strftime('%d'))
hora = int(now.strftime('%H'))
minuto = int(now.strftime('%M'))
segundo = int(now.strftime('%S'))

nomeArquivo= 'vid_Dia%d' %dia
nomeArquivo += '_%d' %mes
nomeArquivo += '_%d' %ano
nomeArquivo += '_'
nomeArquivo += 'Hora_%d' % hora
nomeArquivo += '_%d' %minuto
nomeArquivo += '_%d' %segundo
nomeArquivo += ".avi"

largura = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
altura =  int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
dimensoes = (largura,altura)
    
saida = cv2.VideoWriter(nomeArquivo, cv2.VideoWriter_fourcc('M','J','P','G') , 19.0, dimensoes)  

while video_ip_on:
        try:
            validacao, frame = cap.read()
            cv2.imshow("Sz_Cloud", frame)
            saida.write(frame) #salvamos quadro a quadro
            if ord('l')==cv2.waitKey(1):
                video_ip_on = False
            horaAtual= time.time()           
            tempo_atual_do_filme =  (int(horaAtual - horaInicio))
            print(tempo_atual_do_filme)
            if tempo_atual_do_filme >= duracaoFilme:
                break 
        except:
            print("erro na captura")
            #video_ip_on = False
            
cap.release()
saida.release()
cv2.destroyAllWindows() 

lista_arquivos = os.listdir(caminho + '/Save_Videos')
for arquivo in lista_arquivos:
    if '.avi' in arquivo:
        os.rename(caminho + f"/Save_Videos/{arquivo}", destino + f"/Saves/{arquivo}")
        print(arquivo)