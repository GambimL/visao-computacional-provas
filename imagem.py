from imutils.perspective import four_point_transform
from imutils import contours
import imutils
import cv2
import numpy as np


        
    

def pre_processa_imagem(imagem):
    ANSWER_KEY = {0: 4, 1: 0, 2: 0, 3: 4, 4: 1, 5: 3, 6: 3, 7: 2, 8: 2, 9: 1, 10: 2, 11: 2, 12: 0, 13: 4, 14: 1, 15: 1, 16: 2, 17: 1, 18: 2, 19: 4}
    image = imagem
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 75, 200)
    kernel = np.ones((5,5), np.uint8)
    dilation = cv2.dilate(edged,kernel,iterations = 1)
    cnts = cv2.findContours(dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    cnts = cv2.findContours(dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    docCnt = None
    if len(cnts) > 0:
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
        for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            
            if len(approx) == 4:
                docCnt = approx
                break
    
    paper = four_point_transform(image, docCnt.reshape(4, 2))
    warped = four_point_transform(gray, docCnt.reshape(4, 2))
    warped = cv2.resize(warped, dsize=(650, 700))
    paper = cv2.resize(paper, dsize=(650, 700))
    warped = warped[20:695, 10:630]
    paper = paper[20:695, 10:630]
    thresh = cv2.threshold(warped, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    kernel = np.ones((4,4),np.uint8)
    thresh = cv2.dilate(thresh,kernel,iterations = 1)

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
    ctns = imutils.grab_contours(cnts)
    questionsCnts = []
    for c in ctns:
        x, y, w, h = cv2.boundingRect(c)
        ar = w / float(h)
        if w >= 35 and h >= 35 and ar >= 0.9 and ar <= 1.1:
            questionsCnts.append(c)
            

    
    cv2.imshow('foto gabarito', paper)
    questionCnts = contours.sort_contours(questionsCnts, method = "top-to-bottom")[0]
    correct = 0


    for (q, i) in enumerate(np.arange(0, len(questionsCnts), 5)):
        cnts = contours.sort_contours(questionsCnts[i:i + 5])[0]
        bubbled = None


        for (j, c) in enumerate(cnts):
            mask = np.zeros(thresh.shape, dtype="uint8")
            cv2.drawContours(mask, [c], -1, 255, -1)
            mask = cv2.bitwise_and(thresh, thresh, mask=mask)
            total = cv2.countNonZero(mask)


            if bubbled is None or total > bubbled[0]:
                bubbled = (total, j)

            cor = (0, 0, 255)
            k = ANSWER_KEY[q]

            if k == bubbled[1]:
                cor = (0, 255, 0)
                correct += 1

        cv2.drawContours(paper , [cnts[k]], -1, cor, 2)
    cv2.imshow('foto gabarito', paper)







 