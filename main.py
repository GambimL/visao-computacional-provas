from imagem import imagem
import cv2

def main():
    img = cv2.imread('foto4.JPG')
    image = imagem(img)
    foto_processada = image.pre_processa_imagem()

    cv2.imshow('',foto_processada)
    cv2.waitKey(0)

if(__name__ == "__main__"):
    main()
