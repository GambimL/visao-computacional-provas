import numpy as np
import os
from itertools import chain
import cv2
import imutils

def trasnforma_letra_para_numero(dados):
        alternativas = []
        
        for dado in dados:
                dado = dado.replace(' ', '')
                if dado == 'A':
                    alternativas.append(0)
                elif dado == 'B':
                    alternativas.append(1)
                elif dado == 'C':
                    alternativas.append(2)
                elif dado == 'D':
                    alternativas.append(3)
                elif dado == 'E':
                    alternativas.append(4)
        return alternativas

def trnaforma_numero_para_letra(dados):
    alternativas = []
    for dado in dados:
            dado = dado.replace(' ', '')
            if dado == 'A':
                alternativas.append(0)
            elif dado == 'B':
                alternativas.append(1)
            elif dado == 'C':
                alternativas.append(2)
            elif dado == 'D':
                alternativas.append(3)
            elif dado == 'E':
                alternativas.append(4)
    return alternativas

def concerta_array(array):
    array_corrigido = np.zeros(20)
    for q in range(1, 2):
        for i in range(10):
            array_corrigido[2*i+1] = array[i]     
        for i in range(10):
            array_corrigido[2*i] = array[i+10]
    print(array_corrigido)
    return array_corrigido

def lista_arquivos_subdiretorios(diretorio):
    arquivos = []
    subdiretorios = os.listdir(diretorio)
    for i in range(len(subdiretorios)):
        subsubdiretorio1 = os.listdir(f'{diretorio}/{subdiretorios[i]}')
        for q in range(len(subsubdiretorio1)):
            arquivos.append(os.listdir(f'{diretorio}/{subdiretorios[i]}/{subsubdiretorio1[q]}'))

    arquivos = sum(arquivos, [])
    return arquivos

def retira_extensao(arquivo):
    retirar = arquivo[arquivo.find('.')::]
    arquivo = arquivo.replace(retirar, '')
    return arquivo

def abre_camera():
    webcam = cv2.VideoCapture(0)
    if webcam.isOpened():
            validacao, frame = webcam.read()
            while validacao:
                    validacao, frame = webcam.read()
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
                    edged = cv2.Canny(blurred, 75, 200)
                    kernel = np.ones((2,2),np.uint8)
                    edged = cv2.dilate(edged,kernel,iterations = 1)


                    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                    cnts = imutils.grab_contours(cnts)
                    doCnt = None

                    if len(cnts) > 0:
                        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
                        for c in cnts:
                            peri = cv2.arcLength(c, True)
                            approx = cv2.approxPolyDP(c, 0.02 * peri, True)

                            if len(approx == 4):
                                doCnt = approx
                                cv2.drawContours(frame, [doCnt],-1, (0, 0, 255), 2)
                
                        

                    cv2.imshow("Video da Webcam", frame)
                    key = cv2.waitKey(5)
                    if key == 27: # ESC
                        break
                    
    return frame

def salva_imagem(imagem, diretorio, nome_de_saida):
    filename = 'imagens_gabaritos/' + str(nome_de_saida)
    print(filename)
    saida = cv2.imwrite(filename, imagem)
    print(f'imagem salva com socesso: {saida}')

            

    
     


         
    
