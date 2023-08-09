from funcoes_auxiliares import *
from imagem import pre_processa_imagem
from resposta import calcula_total
import cv2
from tkinter import *
from tkinter import ttk
from dataframes import *
import os
from imutils.perspective import four_point_transform
from imutils import contours
import imutils
import numpy as np
import pytesseract





def criar_gabarito():

    def executar_comando():


        area = str(caixa_materias.get())
        turma = str(caixa_turmas.get())
        semestre = str(caixa_semestre.get())
        tipo = str(caixa_tipo.get())
        nome_gabarito = str(imput.get())

        for caixa in caixa_questoes:
            questoes_marcadas.append(caixa.get())

        for peso in pesos:
            peso_questoes.append(peso.get())



        print(questoes_marcadas) 
        criar_dataframe(nome_gabarito, questoes_marcadas,
                         peso_questoes, area,
                         turma, semestre, tipo)


    def obter_valores_da_tabela():

        imput.delete(0, END)
        caixa_materias.delete(0, END)
        caixa_semestre.delete(0, END)
        caixa_turmas.delete(0, END)
        caixa_tipo.delete(0, END)

        for caixa in caixa_questoes:
            caixa.delete(0, END)


        data_frame = tv.selection()[0]
        values = tv.item(data_frame, 'values')
        questoes, pesos = obter_dataframe(f'bancodedados/{values[2]}/{values[3]}/{values[1]}.xlsx')

        retirar = values[1][values[1].find('[')::]
        gabarito = values[1].replace(retirar,'')
        imput.insert(0, gabarito)

        limite_inferior = values[1].find('[')
        limite_superior = values[1].find(',')
        turma = values[1][values[1].find(',')+1:
                        values[1].find('2')+6]
        semestre = values[1][values[1].find('semestre'):
                            values[1].find('semestre')+10]
        tipo = values[1][values[1].find('semestre')+11:
                            values[1].find(']')]
        
        materia = values[1][limite_inferior+1:limite_superior]
        caixa_materias.insert(0, materia)
        caixa_turmas.insert(0, turma)
        caixa_semestre.insert(0, semestre)
        caixa_tipo.insert(0, tipo)
    


        for i in range(len(caixa_questoes)):
            caixa_questoes[i].insert(0,f'{questoes[i]}')
       

    window = Tk()
    window.config(padx=50, pady=50, bg='WHITE')
    pesos = []
    questoes = []
    caixa_questoes = []
    materias = ['Mátematica', 'Ciências Humanas', 'Ciências da Natureza', 'Linguagens']
    turmas = ['1° Ano', '2° Ano', '3° Ano']
    semestre = ['semestre 1', 'semestre 2']
    tipo = ['semestral', 'Recuperação']
    alternativas = ['A', 'B', 'C', 'D', 'E']
    questoes_marcadas = []
    peso_questoes = []

    
    frame_areas_turmas = Frame(window, bg='WHITE')
    frame_areas_turmas.pack(side='left')

    nome_do_gabarito = Label(window, text='Nome do Gabarito', anchor=W, bg='WHITE')
    nome_do_gabarito.pack()
    imput = Entry(window, width = 45)
    imput.pack()

    frame_infos = Frame(window, bg="WHITE")
    frame_infos.pack()

    frame_areas_turmas = Frame(frame_infos, bg='WHITE')
    frame_areas_turmas.pack(side='left')


    label_materias = Label(frame_areas_turmas, text='Areas', bg='WHITE')
    label_materias.pack(side = 'top')
    caixa_materias = ttk.Combobox(frame_areas_turmas, value=materias)
    caixa_materias.pack()

    label_turmas = Label(frame_areas_turmas, text='Turmas', bg='WHITE')
    label_turmas.pack(side = 'top')
    caixa_turmas = ttk.Combobox(frame_areas_turmas, value=turmas)
    caixa_turmas.pack()

    frame_semestre_tipo = Frame(frame_infos, bg='WHITE')
    frame_semestre_tipo.pack(side='left')

    label_semestre = Label(frame_semestre_tipo, text='semestre', bg='WHITE')
    label_semestre.pack(side = 'top')
    caixa_semestre = ttk.Combobox(frame_semestre_tipo, value=semestre)
    caixa_semestre.pack()

    label_tipo = Label(frame_semestre_tipo, text='Tipo', bg='WHITE')
    label_tipo.pack(side = 'top')
    caixa_tipo = ttk.Combobox(frame_semestre_tipo, value=tipo)
    caixa_tipo.pack()


    alternativas = ['A', 'B', 'C', 'D', 'E']


    def criar_frame_questao(parent, questao, iterador):
        frame_questao = Frame(parent, bg='WHITE')
        frame_questao.pack(side = 'left', padx = 30)
        label_questao = Label(frame_questao, text=f'Questão {questao + iterador}', bg='WHITE')
        label_questao.pack(side = 'top')
        caixa_questao = ttk.Combobox(frame_questao, value=alternativas)
        caixa_questao.pack(side = 'left'),
        peso = Entry(frame_questao, width=5)
        peso.insert(0, 'Peso'),
        peso.pack()

        return label_questao, caixa_questao, peso

    caixa_questoes = []
    pesos = []
    frame_top = Frame(window, bg='WHITE')
    frame_top.pack(side = 'top')
    for questao in range(1, 6):
        label_questao, caixa_questao, peso = criar_frame_questao(frame_top, questao, 0)
        caixa_questoes.append(caixa_questao)
        pesos.append(peso)

  
    frame_top2 = Frame(window, bg='WHITE')
    frame_top2.pack(side = 'top')
    for questao in range(1, 6):
        label_questao, caixa_questao, peso = criar_frame_questao(frame_top2, questao, 5)
        caixa_questoes.append(caixa_questao)
        pesos.append(peso)


 
    frame_top3 = Frame(window, bg='WHITE')
    frame_top3.pack(side = 'top')
    for questao in range(1, 6):
        label_questao, caixa_questao, peso = criar_frame_questao(frame_top3, questao, 10)
        caixa_questoes.append(caixa_questao)
        pesos.append(peso)


    frame_top4 = Frame(window, bg='WHITE')
    frame_top4.pack(side = 'top')
    for questao in range(1, 6):
        label_questao, caixa_questao, peso = criar_frame_questao(frame_top4, questao, 15)
        caixa_questoes.append(caixa_questao)
        pesos.append(peso)

    salvar = Button(window, text='Salvar', command=executar_comando, width=20)
    salvar.pack(side = 'left', padx=10)

    obter = Button(window, text='Obter', command=obter_valores_da_tabela, width=20)
    obter.pack(side = 'left')


    frame_tabela = Frame(window, bg='WHITE')
    frame_tabela.pack(side = 'top', padx= 30, pady=30)



    gabaritos = lista_arquivos_subdiretorios('C:/Users/usuario/Desktop/visãoprovas/bancodedados')
    print(gabaritos)
    gabarito_corrigido =  []

    for i in range(len(gabaritos)):
        gabarito_corrigido.append(retira_extensao(gabaritos[i]))
    

    tv = ttk.Treeview(frame_tabela)
    tv['columns'] = ('numero', 'Gabarito', 'Turma', 'Semestre')
    tv.column('#0', width=0, stretch=NO)
    tv.column('numero', anchor=CENTER, width=80)
    tv.column('Gabarito',anchor=CENTER, width=300)
    tv.column('Turma',anchor=CENTER, width=80)
    tv.column('Semestre',anchor=CENTER, width=80)
    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('numero', text='Id', anchor=CENTER)
    tv.heading('Gabarito', text='Gabarito', anchor=N)
    tv.heading('Turma', text='Turma', anchor=N)
    tv.heading('Semestre', text='Semestre', anchor=N)

    for i in range(len(gabarito_corrigido)):
        ano_turma = gabarito_corrigido[i][gabarito_corrigido[i].find(',')+1:
                                          gabarito_corrigido[i].find('Ano')]
        semestre_numero = gabarito_corrigido[i][gabarito_corrigido[i].find('semestre')+8:
                                                gabarito_corrigido[i].find('semestre')+10]

        tv.insert(parent='', index=i, iid=i, text='', values=(i, gabarito_corrigido[i],f'{ano_turma}Ano',f'semestre{semestre_numero}'))
    tv.pack()
    


    window.mainloop()


def corrigir_provas():
    webcam = cv2.VideoCapture(0)

    def selecionar_gabarito():

        nome_gabarito = str(caixa_gabaritos.get())
        ano_turma = nome_gabarito[nome_gabarito.find(',')+1:
                                          nome_gabarito.find('Ano')]
        semestre_numero = nome_gabarito[nome_gabarito.find('semestre')+8:
                                                nome_gabarito.find('semestre')+10]
        questoes, pesos = obter_dataframe(f'bancodedados/{ano_turma}Ano/semestre{semestre_numero}/{nome_gabarito}.xlsx')
        alternativas = trasnforma_letra_para_numero(questoes)
        for i in range(len(alternativas)):
            tv.insert(parent='', index=i, iid=i, text='', values=(f'Qestão{i+1}', questoes[i], pesos[i]))
        

            
    def processar_gabarito():
        nome_gabarito = str(caixa_gabaritos.get())
        ano_turma = nome_gabarito[nome_gabarito.find(',')+1:
                                          nome_gabarito.find('Ano')]
        semestre_numero = nome_gabarito[nome_gabarito.find('semestre')+8:
                                                nome_gabarito.find('semestre')+10]
        questoes, pesos = obter_dataframe(f'bancodedados/{ano_turma}Ano/semestre{semestre_numero}/{nome_gabarito}.xlsx')
        alternativas = trasnforma_letra_para_numero(questoes)

        frame = abre_camera()

        webcam.release()
        paper, corretas, pesos_corretas, posicao_corretas, texto_aluno = pre_processa_imagem(frame, alternativas, pesos)
        acertos = len(corretas)
        resultado = calcula_total(acertos, pesos_corretas)
        nota.insert(0, resultado)

        texto_aluno = texto_aluno[texto_aluno.find(':')+1::]
        nome_aluno.insert(0, texto_aluno)

        

        gabarito_aluno = np.zeros(20)
        for i in range(len(posicao_corretas)):
            gabarito_aluno[posicao_corretas[i]] = 1

        for i in range(len(gabarito_aluno)):
            if gabarito_aluno[i] == 0:
                tv2.insert(parent='', index=i, iid=i, text='', values=(f'Qestão{i+1}', questoes[i], 'Errado'))
            else:
                tv2.insert(parent='', index=i, iid=i, text='', values=(f'Qestão{i+1}', questoes[i], 'Certo'))

        gabarito = caixa_gabaritos.get()
        aluno = nome_aluno.get()
        gabarito = gabarito[::gabarito.find('[')]
        cv2.imwrite(f"{aluno}.png", paper)
        
        

    
    window = Tk()
    window.config(padx=100, pady=100)

    frame_tabela = Frame(window)
    frame_tabela.pack(side = 'left')
    gabaritos = lista_arquivos_subdiretorios('C:/Users/usuario/Desktop/visãoprovas/bancodedados')
    print(gabaritos)
    gabarito_corrigido =  []

    for i in range(len(gabaritos)):
        gabarito_corrigido.append(retira_extensao(gabaritos[i]))
    
    caixa_gabaritos = ttk.Combobox(frame_tabela, value=gabarito_corrigido, width=45)
    caixa_gabaritos.pack(pady = 20)

    selecionar_gabarito = Button(frame_tabela, text='Selecionar Gabarito', command=selecionar_gabarito, width=20)
    selecionar_gabarito.pack(pady = 20)


    tv = ttk.Treeview(frame_tabela)
    tv['columns'] = ('numero', 'Gabarito', 'Peso')
    tv.column('#0', width=0, stretch=NO)
    tv.column('numero', anchor=CENTER, width=80)
    tv.column('Gabarito',anchor=CENTER, width=200)
    tv.column('Peso', anchor=CENTER, width=80)
    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('numero', text='Id', anchor=CENTER)
    tv.heading('Gabarito', text='Gabarito', anchor=CENTER)
    tv.heading('Peso',text='Peso',anchor=CENTER)
    tv.pack()

    frame_dados = Frame(window)
    frame_dados.pack(side = 'left', padx=50)


    camera = Button(frame_dados, text='Abrir câmera', command=processar_gabarito, width=20)
    camera.pack()

    label_aluno = Label(frame_dados, text='Nome do Aluno',  anchor=W)
    label_aluno.pack()
    nome_aluno = Entry(frame_dados, width=30)
    nome_aluno.pack()

    label_nota = Label(frame_dados, text='Nota do Aluno', anchor=W)
    label_nota.pack()
    nota = Entry(frame_dados, width=30)
    nota.pack()

    tv2 = ttk.Treeview(frame_dados)
    tv2['columns'] = ('numero', 'Gabarito', 'Resposta')
    tv2.column('#0', width=0, stretch=NO)
    tv2.column('numero', anchor=CENTER, width=80)
    tv2.column('Gabarito',anchor=CENTER, width=200)
    tv2.column('Resposta',anchor=CENTER, width=200)
    tv2.heading('#0', text='', anchor=CENTER)
    tv2.heading('numero', text='Id', anchor=CENTER)
    tv2.heading('Gabarito', text='Gabarito', anchor=CENTER)
    tv2.heading('Resposta', text='Gabarito', anchor=CENTER)
    tv2.pack()
    
    window.mainloop()

def dados():
    window = Tk()

    


    window.mainloop()






    









    












    
     
