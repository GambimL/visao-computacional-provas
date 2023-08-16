import cv2
from tkinter import *
from tkinter import ttk
from Janelas import *
import os
from PIL import Image, ImageTk

def main():

    window = Tk()
    window.title('Corretor de Provas')
    window.config(padx=89, pady=89, bg='WHITE')

    logo = PhotoImage(file='imagens/fotologo.png')
    label_image = Label(window, image=logo, bg='WHITE')
    label_image.pack(pady=20)

    frame_botoes = Frame(window, width=300, height=200, bg='WHITE')
    frame_botoes.pack()

    gabarito = Button(frame_botoes, text = 'Criar Gabarito', 
                      width = 20 ,
                      command = criar_gabarito, 
                      bg='WHITE')

    gabarito.pack(side = 'left', padx=30)
    corrigir = Button(frame_botoes, text = 'corrigir provas', 
                      width = 20 ,
                      command = corrigir_provas, 
                      bg='WHITE')
    
    corrigir.pack(side = 'left')
    Dados = Button(frame_botoes, text = 'Dados', 
                      width = 20 ,
                      command = dados,
                      bg='WHITE')
    Dados.pack(side ='left', padx=30)


    frame_tabela = Frame(window)
    frame_tabela.pack(side = 'top', padx= 30, pady=30)


    window.mainloop()


if(__name__ == "__main__"):
    main()