from imutils.perspective import four_point_transform
import imutils
import cv2
import numpy as np

def pre_processa_imagem(imagem):
        image = imagem
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

img = cv2.imread('foto4.JPG')
foto_processada = pre_processa_imagem(img)

cv2.imshow('', foto_processada)
cv2.waitKey(0)