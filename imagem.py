from imutils.perspective import four_point_transform
from imutils import contours
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
                    break

        warped = four_point_transform(gray, doCnt.reshape(4, 2))
        cv2.drawContours(image, warped, 0, 255, 0)
        warped = cv2.resize(warped, dsize=(650, 700))
        
        

        warped1 = warped[60:700, 20:300]
        warped2 = warped[60:685, 300:620]
        imagens_cortadas = [warped1, warped2]

        imagens_pre_processadas = []
        for imagem in imagens_cortadas:
            thresh = cv2.threshold(imagem, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
            kernel = np.ones((4,4),np.uint8)
            thresh = cv2.dilate(thresh,kernel,iterations = 1)
            imagens_pre_processadas.append(thresh)
            cv2.imshow('', thresh)
            cv2.waitKey(0)


        paper = four_point_transform(image, doCnt.reshape(4, 2))
        paper = cv2.resize(paper, dsize=(650, 700))
        paper2 = paper[60:685, 300:620]
        paper1 = paper[60:700, 20:300]
        papers = [paper1, paper2]

        return imagens_pre_processadas, papers, warped
        
    
    def processa_imagem(self, ANSWER_KEY, processadas, papers):
       
        for l in range(len(processadas)):
            cnts = cv2.findContours(processadas[l].copy(), cv2.RETR_EXTERNAL, 
            cv2.CHAIN_APPROX_SIMPLE)
            ctns = imutils.grab_contours(cnts)
            questionsCnts = []

            for c in ctns:  
                x, y, w, h = cv2.boundingRect(c)
                ar = w / float(h)
                if w >= 35 and h >= 35 and ar >= 0.9 and ar <= 1.1:
                    questionsCnts.append(c)
        
            questionCnts = contours.sort_contours(questionsCnts, method = "top-to-bottom")[0]
            correct = 0 
            for (q, i) in enumerate(np.arange(0, len(questionCnts), 5)):
                cnts = contours.sort_contours(questionCnts[i:i + 5])[0]
                bubbled = None

                for (j, c) in enumerate(cnts):
                    mask = np.zeros(processadas[l].shape, dtype="uint8")
                    cv2.drawContours(mask, [c], -1, 255, -1)
                    mask = cv2.bitwise_and(processadas[l], processadas[l], mask=mask)
                    total = cv2.countNonZero(mask)


                    if bubbled is None or total > bubbled[0]:
                        bubbled = (total, j)
    
                cor = (0, 0, 255)
                k = ANSWER_KEY[l][q]

                if k == bubbled[1]:
                    cor = (0, 255, 0)
                    correct += 1

                cv2.drawContours(papers[l], [cnts[k]], -1, cor, 2)

        return correct, papers[l]
        
    def set_imagem(self, img):
        self.imagem = img









 