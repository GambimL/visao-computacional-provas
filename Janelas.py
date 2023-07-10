from imagem import imagem
import cv2
from tkinter import *
from tkinter import ttk
from dataframes import *
import os




def criar_gabarito():

    def executar_comando():
        nome_gabarito = str(imput.get())


        questoes_marcadas.append(caixa_questao1.get())
        peso_questoes.append(peso1.get())
        questoes_marcadas.append(caixa_questao2.get())
        peso_questoes.append(peso2.get())
        questoes_marcadas.append(caixa_questao3.get())
        peso_questoes.append(peso3.get())
        questoes_marcadas.append(caixa_questao4.get())
        peso_questoes.append(peso4.get())
        questoes_marcadas.append(caixa_questao5.get())
        peso_questoes.append(peso5.get())
        questoes_marcadas.append(caixa_questao6.get())
        peso_questoes.append(peso6.get())
        questoes_marcadas.append(caixa_questao7.get())
        peso_questoes.append(peso7.get())
        questoes_marcadas.append(caixa_questao8.get())
        peso_questoes.append(peso8.get())
        questoes_marcadas.append(caixa_questao9.get())
        peso_questoes.append(peso9.get())
        questoes_marcadas.append(caixa_questao10.get())
        peso_questoes.append(peso10.get())
        questoes_marcadas.append(caixa_questao11.get())
        peso_questoes.append(peso11.get())
        questoes_marcadas.append(caixa_questao12.get())
        peso_questoes.append(peso12.get())
        questoes_marcadas.append(caixa_questao13.get())
        peso_questoes.append(peso13.get())
        questoes_marcadas.append(caixa_questao14.get())
        peso_questoes.append(peso14.get())
        questoes_marcadas.append(caixa_questao15.get())
        peso_questoes.append(peso15.get())
        questoes_marcadas.append(caixa_questao16.get())
        peso_questoes.append(peso16.get())
        questoes_marcadas.append(caixa_questao17.get())
        peso_questoes.append(peso17.get())
        questoes_marcadas.append(caixa_questao18.get())
        peso_questoes.append(peso18.get())
        questoes_marcadas.append(caixa_questao19.get())
        peso_questoes.append(peso19.get())
        questoes_marcadas.append(caixa_questao20.get())
        peso_questoes.append(peso20.get())

        print(questoes_marcadas)

        criar_dataframe(nome_gabarito, questoes_marcadas, peso_questoes)







    window = Tk()
    window.config(padx=50, pady=50)
    pesos = []
    questoes = []
    caixa_questoes = []
    materias= ['Mátematica', 'Ciências Humanas', 'Ciências da Natureza', 'Linguagens']
    questoes_marcadas = []
    peso_questoes = []

    


    nome_do_gabarito = Label(window, text='Nome do Gabarito', anchor=W)
    nome_do_gabarito.pack()
    imput = Entry(window, width = 45)
    imput.pack()

    label_materias = Label(window, text='Areas')
    label_materias.pack()
    caixa_materias = ttk.Combobox(window, value=materias)
    caixa_materias.pack()

    
    #frame_top = Frame(window)
    #frame_top.pack(side= 'top')
    alternativas = ['A', 'B', 'C', 'D', 'E']



    frame_top = Frame(window)
    frame_top.pack(side = 'top')
    frame_questao1 = Frame(frame_top)
    frame_questao1.pack(side = 'left', padx = 30)
    label_questao1 = Label(frame_questao1, text='Questão 1')
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
    peso2 = Entry(frame_questao2, width=5)
    peso2.insert(0, 'Peso')
    peso2.pack()



    frame_questao3 = Frame(frame_top)
    frame_questao3.pack(side = 'left', padx = 30)
    label_questao3 = Label(frame_questao3, text='Questão 3')
    label_questao3.pack(side = 'top')
    caixa_questao3 = ttk.Combobox(frame_questao3, value=alternativas)
    caixa_questao3.pack(side = 'left')
    peso3 = Entry(frame_questao3, width=5)
    peso3.insert(0, 'Peso')
    peso3.pack()



    frame_questao4 = Frame(frame_top)
    frame_questao4.pack(side = 'left', padx = 30)
    label_questao4 = Label(frame_questao4, text='Questão 4')
    label_questao4.pack(side = 'top')
    caixa_questao4 = ttk.Combobox(frame_questao4, value=alternativas)
    caixa_questao4.pack(side = 'left')
    peso4 = Entry(frame_questao4, width=5)
    peso4.insert(0, 'Peso')
    peso4.pack()

    

    frame_questao5 = Frame(frame_top)
    frame_questao5.pack(side = 'left', padx = 30)
    label_questao5 = Label(frame_questao5, text='Questão 5')
    label_questao5.pack(side = 'top')
    caixa_questao5 = ttk.Combobox(frame_questao5, value=alternativas)
    caixa_questao5.pack(side = 'left')
    peso5 = Entry(frame_questao5, width=5)
    peso5.insert(0, 'Peso')
    peso5.pack()
    


    frame_top2 = Frame(window)
    frame_top2.pack(side= 'top')

    frame_questao6 = Frame(frame_top2)
    frame_questao6.pack(side = 'left', padx = 30)
    label_questao6 = Label(frame_questao6, text='Questão 1', anchor = W)
    label_questao6.pack(side = 'top')
    caixa_questao6 = ttk.Combobox(frame_questao6, value=alternativas)
    caixa_questao6.pack(side = 'left')
    peso6 = Entry(frame_questao6, width=5)
    peso6.insert(0, 'Peso')
    peso6.pack()
   


    frame_questao7 = Frame(frame_top2)
    frame_questao7.pack(side = 'left', padx = 30)
    label_questao7 = Label(frame_questao7, text='Questão 7')
    label_questao7.pack(side = 'top')
    caixa_questao7 = ttk.Combobox(frame_questao7, value=alternativas)
    caixa_questao7.pack(side = 'left')
    peso7 = Entry(frame_questao7, width=5)
    peso7.insert(0, 'Peso')
    peso7.pack()
   
    



    frame_questao8 = Frame(frame_top2)
    frame_questao8.pack(side = 'left', padx = 30)
    label_questao8 = Label(frame_questao8, text='Questão 8')
    label_questao8.pack(side = 'top')
    caixa_questao8 = ttk.Combobox(frame_questao8, value=alternativas)
    caixa_questao8.pack(side = 'left')
    peso8 = Entry(frame_questao8, width=5)
    peso8.insert(0, 'Peso')
    peso8.pack()



    frame_questao9 = Frame(frame_top2)
    frame_questao9.pack(side = 'left', padx = 30)
    label_questao9 = Label(frame_questao9, text='Questão 9')
    label_questao9.pack(side = 'top')
    caixa_questao9 = ttk.Combobox(frame_questao9, value=alternativas)
    caixa_questao9.pack(side = 'left')
    peso9 = Entry(frame_questao9, width=5)
    peso9.insert(0, 'Peso')
    peso9.pack()
 


    frame_questao10 = Frame(frame_top2)
    frame_questao10.pack(side = 'left', padx = 30)
    label_questao10 = Label(frame_questao10, text='Questão 10')
    label_questao10.pack(side = 'top')
    caixa_questao10 = ttk.Combobox(frame_questao10, value=alternativas)
    caixa_questao10.pack(side = 'left')
    peso10 = Entry(frame_questao10, width=5)
    peso10.insert(0, 'Peso')
    peso10.pack()
   

    frame_top3 = Frame(window)
    frame_top3.pack(side = 'top')

    frame_top3.pack(side= 'top')
    frame_questao11 = Frame(frame_top3)
    frame_questao11.pack(side = 'left', padx = 30)
    label_questao11 = Label(frame_questao11, text='Questão 1', anchor = W)
    label_questao11.pack(side = 'top')
    caixa_questao11 = ttk.Combobox(frame_questao11, value=alternativas)
    caixa_questao11.pack(side = 'left')
    peso11 = Entry(frame_questao11, width=5)
    peso11.insert(0, 'Peso')
    peso11.pack()
 

    frame_questao12 = Frame(frame_top3)
    frame_questao12.pack(side = 'left', padx = 30)
    label_questao12 = Label(frame_questao12, text='Questão 12')
    label_questao12.pack(side = 'top')
    caixa_questao12 = ttk.Combobox(frame_questao12, value=alternativas)
    caixa_questao12.pack(side = 'left')
    peso12 = Entry(frame_questao12, width=5)
    peso12.insert(0, 'Peso')
    peso12.pack()
 


    frame_questao13 = Frame(frame_top3)
    frame_questao13.pack(side = 'left', padx = 30)
    label_questao13 = Label(frame_questao13, text='Questão 13')
    label_questao13.pack(side = 'top')
    caixa_questao13 = ttk.Combobox(frame_questao13, value=alternativas)
    caixa_questao13.pack(side = 'left')
    peso13 = Entry(frame_questao13, width=5)
    peso13.insert(0, 'Peso')
    peso13.pack()



    frame_questao14 = Frame(frame_top3)
    frame_questao14.pack(side = 'left', padx = 30)
    label_questao14 = Label(frame_questao14, text='Questão 14')
    label_questao14.pack(side = 'top')
    caixa_questao14 = ttk.Combobox(frame_questao14, value=alternativas)
    caixa_questao14.pack(side = 'left')
    peso14 = Entry(frame_questao14, width=5)
    peso14.insert(0, 'Peso')
    peso14.pack()


    frame_questao15 = Frame(frame_top3)
    frame_questao15.pack(side = 'left', padx = 30)
    label_questao15 = Label(frame_questao15, text='Questão 15')
    label_questao15.pack(side = 'top')
    caixa_questao15 = ttk.Combobox(frame_questao15, value=alternativas)
    caixa_questao15.pack(side = 'left')
    peso15 = Entry(frame_questao15, width=5)
    peso15.insert(0, 'Peso')
    peso15.pack()



    frame_top4 = Frame(window)
    frame_top4.pack(side= 'top')

    frame_questao16 = Frame(frame_top4)
    frame_questao16.pack(side = 'left', padx = 30)
    label_questao16 = Label(frame_questao16, text='Questão 16', anchor = W)
    label_questao16.pack(side = 'top')
    caixa_questao16 = ttk.Combobox(frame_questao16, value=alternativas)
    caixa_questao16.pack(side = 'left')
    peso16 = Entry(frame_questao16, width=5)
    peso16.insert(0, 'Peso')
    peso16.pack()
   


    frame_questao17 = Frame(frame_top4)
    frame_questao17.pack(side = 'left', padx = 30)
    label_questao17 = Label(frame_questao17, text='Questão 17')
    label_questao17.pack(side = 'top')
    caixa_questao17 = ttk.Combobox(frame_questao17, value=alternativas)
    caixa_questao17.pack(side = 'left')
    peso17 = Entry(frame_questao17, width=5)
    peso17.insert(0, 'Peso')
    peso17.pack()
  


    frame_questao18 = Frame(frame_top4)
    frame_questao18.pack(side = 'left', padx = 30)
    label_questao18 = Label(frame_questao18, text='Questão 18')
    label_questao18.pack(side = 'top')
    caixa_questao18 = ttk.Combobox(frame_questao18, value=alternativas)
    caixa_questao18.pack(side = 'left')
    peso18 = Entry(frame_questao18, width=5)
    peso18.insert(0, 'Peso')
    peso18.pack()
    


    frame_questao19 = Frame(frame_top4)
    frame_questao19.pack(side = 'left', padx = 30)
    label_questao19 = Label(frame_questao19, text='Questão 19')
    label_questao19.pack(side = 'top')
    caixa_questao19 = ttk.Combobox(frame_questao19, value=alternativas)
    caixa_questao19.pack(side = 'left')
    peso19 = Entry(frame_questao19, width=5)
    peso19.insert(0, 'Peso')
    peso19.pack()
    

    frame_questao20 = Frame(frame_top4)
    frame_questao20.pack(side = 'left', padx = 30)
    label_questao20 = Label(frame_questao20, text='Questão 20')
    label_questao20.pack(side = 'top')
    caixa_questao20 = ttk.Combobox(frame_questao20, value=alternativas)
    caixa_questao20.pack(side = 'left')
    peso20 = Entry(frame_questao20, width=5)
    peso20.insert(0, 'Peso')
    peso20.pack()

    # frame_botoes = Frame(window)
    # frame_botoes.Pack()


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
    

    def obter_valores_da_tabela():
        data_frame = tv.selection()[0]
        values = tv.item(data_frame, 'values')
        questoes, pesos = obter_dataframe(f'bancodedados/{values[1]}')
        imput.insert(0,f'{values[1]}' )
        caixa_questao1.insert(0,f' {questoes[0]}')
        caixa_questao2.insert(0,f' {questoes[1]}')
        caixa_questao3.insert(0,f' {questoes[2]}')
        caixa_questao4.insert(0,f' {questoes[3]}')
        caixa_questao5.insert(0,f' {questoes[4]}')
        caixa_questao6.insert(0,f' {questoes[5]}')
        caixa_questao7.insert(0,f' {questoes[6]}')
        caixa_questao8.insert(0,f' {questoes[7]}')
        caixa_questao9.insert(0,f' {questoes[8]}')
        caixa_questao10.insert(0,f' {questoes[9]}')
        caixa_questao11.insert(0,f' {questoes[10]}')
        caixa_questao12.insert(0,f' {questoes[11]}')
        caixa_questao13.insert(0,f' {questoes[12]}')
        caixa_questao14.insert(0,f' {questoes[13]}')
        caixa_questao15.insert(0,f' {questoes[14]}')
        caixa_questao16.insert(0,f' {questoes[15]}')
        caixa_questao17.insert(0,f' {questoes[16]}')
        caixa_questao18.insert(0,f' {questoes[17]}')
        caixa_questao19.insert(0,f' {questoes[18]}')
        caixa_questao20.insert(0,f' {questoes[19]}')
        



    obter = Button(window, text='Obter', command=obter_valores_da_tabela)
    obter.pack(side = 'left')

    


    window.mainloop()


def corrigir_provas():
    window = Tk()

    


    window.mainloop()

def dados():
    window = Tk()

    


    window.mainloop()

def Atualizar():
    window = Tk()


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




    









    












    
     
