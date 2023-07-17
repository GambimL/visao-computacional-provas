from imagem import imagem
import cv2
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

def main():
    webcam = cv2.VideoCapture(0)
    janela = Tk()
    def generate_frames():
        while True:
            validation, frame = webcam.read()
            if not validation:
                break
            else:
                cv2.imshow("Video da Webcam", frame)
                cv2.waitKey(5)

    label_widget = Label(janela, generate_frames)
    label_widget.pack()
    button1 = Button(janela, text="Open Camera", command=generate_frames)
    button1.pack()      

    janela.title('corretor de provas')

    janela.mainloop()
    
    
    webcam = cv2.VideoCapture(0)


    
    label_widget = Label(janela, )


    ANSWER_KEY = [{0: 0, 1: 0, 2: 0, 3: 3, 4: 1, 5: 3, 6: 3, 7: 2, 8: 2, 9: 2}, 
                  {0: 1, 1: 0, 2: 0, 3: 3, 4: 1, 5: 3, 6: 3, 7: 2, 8: 2, 9: 2}]
    
    img = cv2.imread('IMG_6841 (1).JPG')
    image = imagem(img)
    processadas, papers = image.pre_processa_imagem()
    pontuação, papers = image.processa_imagem(ANSWER_KEY, processadas, papers)
    imagem_pronta = cv2.hconcat(papers)
    cv2.imshow('', imagem_pronta)
    cv2.waitKey(0)


if(__name__ == "__main__"):
    main()