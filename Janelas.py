from imagem import imagem
import cv2
from tkinter import *
from tkinter import ttk
from dataframes import criar_dataframe




def criar_gabarito():
    window = Tk()
    window.config(padx=50, pady=50)
    pesos = []
    questoes = []
    materias= ['Mátematica', 'Ciências Humanas', 'Ciências da Natureza', 'Linguagens']


    nome_do_gabarito = Label(window, text='Nome do Gabarito', anchor=W)
    nome_do_gabarito.pack()
    imput = Entry(window, width = 45)
    imput.pack()

    label_materias = Label(window, text='Areas', )
    label_materias.pack()
    caixa_materias = ttk.Combobox(window, value=materias)
    caixa_materias.pack()

    
    frame_top = Frame(window)
    frame_top.pack(side= 'top')
    alternativas = ['A', 'B', 'C', 'D', 'E']


    frame_questao1 = Frame(frame_top)
    frame_questao1.pack(side = 'left', padx = 30)
    label_questao1 = Label(frame_questao1, text='Questão 1', anchor = W)
    label_questao1.pack(side = 'top')
    caixa_questao1 = ttk.Combobox(frame_questao1, value=alternativas)
    caixa_questao1.pack(side = 'left')
    peso1 = Entry(frame_questao1, width=5)
    peso1.insert(0, 'Peso')
    peso1.pack()


    frame_questao2 = Frame(frame_top)
    frame_questao2.pack(side = 'left', padx = 30)
    label_questao2 = Label(frame_questao2, text='Questão 2')
    label_questao2.pack(side = 'top')
    caixa_questao2 = ttk.Combobox(frame_questao2, value=alternativas)
    caixa_questao2.pack(side = 'left')
    peso1 = Entry(frame_questao2, width=5)
    peso1.insert(0, 'Peso')
    peso1.pack()


    frame_questao3 = Frame(frame_top)
    frame_questao3.pack(side = 'left', padx = 30)
    label_questao3 = Label(frame_questao3, text='Questão 3')
    label_questao3.pack(side = 'top')
    caixa_questao3 = ttk.Combobox(frame_questao3, value=alternativas)
    caixa_questao3.pack(side = 'left')
    peso1 = Entry(frame_questao3, width=5)
    peso1.insert(0, 'Peso')
    peso1.pack()


    frame_questao4 = Frame(frame_top)
    frame_questao4.pack(side = 'left', padx = 30)
    label_questao4 = Label(frame_questao4, text='Questão 4')
    label_questao4.pack(side = 'top')
    caixa_questao4 = ttk.Combobox(frame_questao4, value=alternativas)
    caixa_questao4.pack(side = 'left')
    peso1 = Entry(frame_questao4, width=5)
    peso1.insert(0, 'Peso')
    peso1.pack()

    frame_questao5 = Frame(frame_top)
    frame_questao5.pack(side = 'left', padx = 30)
    label_questao5 = Label(frame_questao5, text='Questão 5')
    label_questao5.pack(side = 'top')
    caixa_questao5 = ttk.Combobox(frame_questao5, value=alternativas)
    caixa_questao5.pack(side = 'left')
    peso1 = Entry(frame_questao5, width=5)
    peso1.insert(0, 'Peso')
    peso1.pack()


    frame_top2 = Frame(window)
    frame_top2.pack(side= 'top')

    frame_questao6 = Frame(frame_top2)
    frame_questao6.pack(side = 'left', padx = 30)
    label_questao6 = Label(frame_questao6, text='Questão 1', anchor = W)
    label_questao6.pack(side = 'top')
    caixa_questao6 = ttk.Combobox(frame_questao6, value=alternativas)
    caixa_questao6.pack(side = 'left')
    peso1 = Entry(frame_questao6, width=5)
    peso1.insert(0, 'Peso')
    peso1.pack()


    frame_questao7 = Frame(frame_top2)
    frame_questao7.pack(side = 'left', padx = 30)
    label_questao7 = Label(frame_questao7, text='Questão 7')
    label_questao7.pack(side = 'top')
    caixa_questao7 = ttk.Combobox(frame_questao7, value=alternativas)
    caixa_questao7.pack(side = 'left')
    peso1 = Entry(frame_questao7, width=5)
    peso1.insert(0, 'Peso')
    peso1.pack()


    frame_questao8 = Frame(frame_top2)
    frame_questao8.pack(side = 'left', padx = 30)
    label_questao8 = Label(frame_questao8, text='Questão 8')
    label_questao8.pack(side = 'top')
    caixa_questao8 = ttk.Combobox(frame_questao8, value=alternativas)
    caixa_questao8.pack(side = 'left')
    peso1 = Entry(frame_questao8, width=5)
    peso1.insert(0, 'Peso')
    peso1.pack()


    frame_questao9 = Frame(frame_top2)
    frame_questao9.pack(side = 'left', padx = 30)
    label_questao9 = Label(frame_questao9, text='Questão 9')
    label_questao9.pack(side = 'top')
    caixa_questao9 = ttk.Combobox(frame_questao9, value=alternativas)
    caixa_questao9.pack(side = 'left')
    peso1 = Entry(frame_questao9, width=5)
    peso1.insert(0, 'Peso')
    peso1.pack()

    frame_questao10 = Frame(frame_top2)
    frame_questao10.pack(side = 'left', padx = 30)
    label_questao10 = Label(frame_questao10, text='Questão 10')
    label_questao10.pack(side = 'top')
    caixa_questao10 = ttk.Combobox(frame_questao10, value=alternativas)
    caixa_questao10.pack(side = 'left')
    peso1 = Entry(frame_questao10, width=5)
    peso1.insert(0, 'Peso')
    peso1.pack()


    frame_top3 = Frame(window)
    frame_top3.pack(side= 'top')

    frame_questao11 = Frame(frame_top3)
    frame_questao11.pack(side = 'left', padx = 30)
    label_questao11 = Label(frame_questao11, text='Questão 1', anchor = W)
    label_questao11.pack(side = 'top')
    caixa_questao11 = ttk.Combobox(frame_questao11, value=alternativas)
    caixa_questao11.pack(side = 'left')
    peso1 = Entry(frame_questao11, width=5)
    peso1.insert(0, 'Peso')
    peso1.pack()


    frame_questao12 = Frame(frame_top3)
    frame_questao12.pack(side = 'left', padx = 30)
    label_questao12 = Label(frame_questao12, text='Questão 12')
    label_questao12.pack(side = 'top')
    caixa_questao12 = ttk.Combobox(frame_questao12, value=alternativas)
    caixa_questao12.pack(side = 'left')
    peso1 = Entry(frame_questao12, width=5)
    peso1.insert(0, 'Peso')
    peso1.pack()


    frame_questao13 = Frame(frame_top3)
    frame_questao13.pack(side = 'left', padx = 30)
    label_questao13 = Label(frame_questao13, text='Questão 13')
    label_questao13.pack(side = 'top')
    caixa_questao13 = ttk.Combobox(frame_questao13, value=alternativas)
    caixa_questao13.pack(side = 'left')
    peso1 = Entry(frame_questao13, width=5)
    peso1.insert(0, 'Peso')
    peso1.pack()


    frame_questao14 = Frame(frame_top3)
    frame_questao14.pack(side = 'left', padx = 30)
    label_questao14 = Label(frame_questao14, text='Questão 14')
    label_questao14.pack(side = 'top')
    caixa_questao14 = ttk.Combobox(frame_questao14, value=alternativas)
    caixa_questao14.pack(side = 'left')
    peso1 = Entry(frame_questao14, width=5)
    peso1.insert(0, 'Peso')
    peso1.pack()

    frame_questao15 = Frame(frame_top3)
    frame_questao15.pack(side = 'left', padx = 30)
    label_questao15 = Label(frame_questao15, text='Questão 15')
    label_questao15.pack(side = 'top')
    caixa_questao15 = ttk.Combobox(frame_questao15, value=alternativas)
    caixa_questao15.pack(side = 'left')
    peso1 = Entry(frame_questao15, width=5)
    peso1.insert(0, 'Peso')
    peso1.pack()


    frame_top3 = Frame(window)
    frame_top3.pack(side= 'top')

    frame_questao11 = Frame(frame_top3)
    frame_questao11.pack(side = 'left', padx = 30)
    label_questao11 = Label(frame_questao11, text='Questão 1', anchor = W)
    label_questao11.pack(side = 'top')
    caixa_questao11 = ttk.Combobox(frame_questao11, value=alternativas)
    caixa_questao11.pack(side = 'left')
    peso1 = Entry(frame_questao11, width=5)
    peso1.insert(0, 'Peso')
    peso1.pack()


    frame_questao12 = Frame(frame_top3)
    frame_questao12.pack(side = 'left', padx = 30)
    label_questao12 = Label(frame_questao12, text='Questão 12')
    label_questao12.pack(side = 'top')
    caixa_questao12 = ttk.Combobox(frame_questao12, value=alternativas)
    caixa_questao12.pack(side = 'left')
    peso1 = Entry(frame_questao12, width=5)
    peso1.insert(0, 'Peso')
    peso1.pack()


    frame_questao13 = Frame(frame_top3)
    frame_questao13.pack(side = 'left', padx = 30)
    label_questao13 = Label(frame_questao13, text='Questão 13')
    label_questao13.pack(side = 'top')
    caixa_questao13 = ttk.Combobox(frame_questao13, value=alternativas)
    caixa_questao13.pack(side = 'left')
    peso1 = Entry(frame_questao13, width=5)
    peso1.insert(0, 'Peso')
    peso1.pack()


    frame_questao14 = Frame(frame_top3)
    frame_questao14.pack(side = 'left', padx = 30)
    label_questao14 = Label(frame_questao14, text='Questão 14')
    label_questao14.pack(side = 'top')
    caixa_questao14 = ttk.Combobox(frame_questao14, value=alternativas)
    caixa_questao14.pack(side = 'left')
    peso1 = Entry(frame_questao14, width=5)
    peso1.insert(0, 'Peso')
    peso1.pack()

    frame_questao15 = Frame(frame_top3)
    frame_questao15.pack(side = 'left', padx = 30)
    label_questao15 = Label(frame_questao15, text='Questão 15')
    label_questao15.pack(side = 'top')
    caixa_questao15 = ttk.Combobox(frame_questao15, value=alternativas)
    caixa_questao15.pack(side = 'left')
    peso1 = Entry(frame_questao15, width=5)
    peso1.insert(0, 'Peso')
    peso1.pack()


    frame_top4 = Frame(window)
    frame_top4.pack(side= 'top')

    frame_questao16 = Frame(frame_top4)
    frame_questao16.pack(side = 'left', padx = 30)
    label_questao16 = Label(frame_questao16, text='Questão 16', anchor = W)
    label_questao16.pack(side = 'top')
    caixa_questao16 = ttk.Combobox(frame_questao16, value=alternativas)
    caixa_questao16.pack(side = 'left')
    peso1 = Entry(frame_questao16, width=5)
    peso1.insert(0, 'Peso')
    peso1.pack()


    frame_questao17 = Frame(frame_top4)
    frame_questao17.pack(side = 'left', padx = 30)
    label_questao17 = Label(frame_questao17, text='Questão 17')
    label_questao17.pack(side = 'top')
    caixa_questao17 = ttk.Combobox(frame_questao17, value=alternativas)
    caixa_questao17.pack(side = 'left')
    peso1 = Entry(frame_questao17, width=5)
    peso1.insert(0, 'Peso')
    peso1.pack()


    frame_questao18 = Frame(frame_top4)
    frame_questao18.pack(side = 'left', padx = 30)
    label_questao18 = Label(frame_questao18, text='Questão 18')
    label_questao18.pack(side = 'top')
    caixa_questao18 = ttk.Combobox(frame_questao18, value=alternativas)
    caixa_questao18.pack(side = 'left')
    peso1 = Entry(frame_questao18, width=5)
    peso1.insert(0, 'Peso')
    peso1.pack()


    frame_questao19 = Frame(frame_top4)
    frame_questao19.pack(side = 'left', padx = 30)
    label_questao19 = Label(frame_questao19, text='Questão 19')
    label_questao19.pack(side = 'top')
    caixa_questao19 = ttk.Combobox(frame_questao19, value=alternativas)
    caixa_questao19.pack(side = 'left')
    peso1 = Entry(frame_questao19, width=5)
    peso1.insert(0, 'Peso')
    peso1.pack()

    frame_questao20 = Frame(frame_top4)
    frame_questao20.pack(side = 'left', padx = 30)
    label_questao20 = Label(frame_questao20, text='Questão 20')
    label_questao20.pack(side = 'top')
    caixa_questao20 = ttk.Combobox(frame_questao20, value=alternativas)
    caixa_questao20.pack(side = 'left')
    peso1 = Entry(frame_questao20, width=5)
    peso1.insert(0, 'Peso')
    peso1.pack()


    salvar = Button(window, text='Salvar Gabarito', command=criar_dataframe)
    salvar.pack(pady=20)
    




    


    window.mainloop()


def corrigir_provas():
    window = Tk()

    


    window.mainloop()

def dados():
    window = Tk()

    


    window.mainloop()