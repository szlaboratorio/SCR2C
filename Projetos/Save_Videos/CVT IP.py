import urllib.request
import cv2
import numpy as np
import time
from datetime import datetime
import os

video_ip_on = True
duracaoFilme = 15
fimGravacao= False

cap = cv2.VideoCapture()
url='http://192.168.5.154:8080/shot.jpg'
cap.open(url)

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
    
saida = cv2.VideoWriter(nomeArquivo, cv2.VideoWriter_fourcc('M','J','P','G') , 2.5, dimensoes)  

cv2.namedWindow('Sz_Cloud', cv2.WINDOW_NORMAL)
#cv2.setWindowProperty('Sz_Laboratorio_XVO', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while video_ip_on:
        try:
            
            imgResp=urllib.request.urlopen(url)
            imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
            img=cv2.imdecode(imgNp,-1)
            cv2.imshow('Sz_Cloud',img) # nome e frame
            saida.write(img) #salvamos quadro a quadro
            if ord('x')==cv2.waitKey(1):
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