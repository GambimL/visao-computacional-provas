from imagem import imagem
import cv2
from tkinter import *
from tkinter import ttk
from Janelas import *
import os

def main():
    


    window = Tk()
    window.title('Corretor de Provas')
    window.config(padx=89, pady=89)

    frame_botoes = Frame(window, width=300, height=200, highlightbackground="black", highlightthickness=2)
    frame_botoes.pack()




    
    gabarito = Button(frame_botoes, text = 'Criar Gabarito', 
                      width = 20 ,
                      command = criar_gabarito)

    gabarito.pack(side = 'left', padx=30)
    corrigir = Button(frame_botoes, text = 'corrigir provas', 
                      width = 20 ,
                      command = corrigir_provas)
    
    corrigir.pack(side = 'left')
    Dados = Button(frame_botoes, text = 'Dados', 
                      width = 20 ,
                      command = dados)
    Dados.pack(side ='left', padx=30)


    frame_tabela = Frame(window)
    frame_tabela.pack(side = 'top', padx= 30, pady=30)

    gabaritos = os.listdir(path='C:/Users/usuario/Desktop/visãoprovas/bancodedados')
    tv = ttk.Treeview(frame_tabela)
    tv['columns'] = ('numero', 'Gabarito')
    tv.column('#0', width=0, stretch=NO)
    tv.column('numero', anchor=CENTER, width=80)
    tv.column('Gabarito',anchor=CENTER, width=200)
    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('numero', text='Id', anchor=CENTER)
    tv.heading('Gabarito', text='Gabarito', anchor=CENTER)
    for i in range(len(gabaritos)):
        tv.insert(parent='', index=i, iid=i, text='', values=(i, gabaritos[i]))
    tv.pack()  

    window.mainloop()


if(__name__ == "__main__"):
    main()