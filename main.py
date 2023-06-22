from imagem import imagem
import cv2

def main():
    

    img = cv2.imread('Respostas.png')
    image = imagem(img)
    image.pre_processa_imagem()
    image.processa_imagem()


if(__name__ == "__main__"):
    main()