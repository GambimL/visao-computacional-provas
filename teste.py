from imutils.perspective import four_point_transform
from imutils import contours
import imutils
import cv2
from imagem import imagem
import numpy as np
webcam = cv2.VideoCapture(0)

ANSWER_KEY = [{0: 0, 1: 0, 2: 0, 3: 3, 4: 1, 5: 3, 6: 3, 7: 2, 8: 2, 9: 2}, 
                  {0: 1, 1: 0, 2: 0, 3: 3, 4: 1, 5: 3, 6: 3, 7: 2, 8: 2, 9: 2}]

def generate_frames():
    while True:
        validation, frame = webcam.read()
        if not validation:
            break
        else:
            image = frame
            image = cv2.resize(image, dsize=(650, 700))
            image = image[200:600, 300:650]
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)
            edged = cv2.Canny(blurred, 75, 200)
            kernel = np.ones((3,3),np.uint8)
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
                        cv2.drawContours(image, [doCnt], 0, 255, 0)
                        break


            thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
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
            cv2.drawContours(image, questionsCnts, 0, 255, 0)

            cv2.imshow('thresold', thresh)
            cv2.imshow("Video da Webcam", image)
            key = cv2.waitKey(5)
            if key == 27: # ESC
                break
    cv2.imwrite("FotoLira.png", frame)

    webcam.release()
    cv2.destroyAllWindows()

generate_frames()
        