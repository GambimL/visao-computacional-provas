from imutils.perspective import four_point_transform
import imutils
import cv2
import numpy as np


#Classe que faz o tratamento da imagem
class imagem:
    
    def __init__(self, imagem):
        self.imagem = imagem
    
    #este método aqui vai processar previamente a imagem até binarizar ela para que 
    #seja possivel extrair a informação das bolhas de opação de resposta de cada pergunta 
    #ele retorna a imagem binarizada 
    def pre_processa_imagem(self):
        image = self.imagem
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(blurred, 75, 200)

        cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        docCnt = None

        if len(cnts) > 0:
            cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
            for c in cnts:
                peri = cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, 0.02 * peri, True)

                if len(approx == 4):
                    doCnt = approx
                    break
        warped = four_point_transform(gray, doCnt.reshape(4, 2))
        thresh = cv2.threshold(warped, 
                0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        
        return thresh
    
    def processa_imagem(thresh):
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_TREE, 
        cv2.CHAIN_APPROX_SIMPLE)
        ctns = imutils.grab_contours(cnts)
        questionsCnts = []

        for c in ctns:  
            x, y, w, h = cv2.boundingRect(c)
            ar = w / float(h)
            if w >= 20 and h >= 20 and ar >= 0.9 and ar <= 1.1:
                questionsCnts.append(c)
        
    def set_imagem(self, img):
        self.imagem = img








 