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
from conexão import *





def criar_gabarito():

    def conexao_com_banco_criar_gabarito(comando):
        conexao = conectar('localhost', 'root', '', 'gabaritos') 
        if comando == "inserir na tabela": 

            area = str(caixa_materias.get())
            turma = str(caixa_turmas.get())
            semestre = str(caixa_semestre.get())
            tipo = str(caixa_tipo.get())
            nome_gabarito = str(imput.get())

            valores_prova = (nome_gabarito, turma, tipo, semestre, area)
            inserir_tabela(conexao, 'provas', '(nome, turma, tipo, semestre, area)', '(%s, %s, %s, %s, %s)', valores_prova)

            for caixa in caixa_questoes:
                questoes_marcadas.append(caixa.get())
            for peso in pesos:
                peso_questoes.append(peso.get())
            for i in range(len(pesos)):
                valores_questoes = (f'questao {i+1}', questoes_marcadas[i], peso_questoes[i], nome_gabarito) 
                inserir_tabela(conexao, 'questoes','(questao, letracerta, peso, prova)', '(%s, %s, %s, %s)', valores_questoes)

        elif comando == "obter da tabela":  
            print("teste")
            imput.delete(0, END)
            caixa_materias.delete(0, END)
            caixa_semestre.delete(0, END)
            caixa_turmas.delete(0, END)
            caixa_tipo.delete(0, END)
            for i in range(len(caixa_questoes)):
                caixa_questoes[i].delete(0, END)
                pesos[i].delete(0, END)

            data_frame = tv.selection()[0]
            values = tv.item(data_frame, 'values')

            seletor_questoes = f"prova = '{values[1]}'"
            seletor_provas = f"nome = '{values[1]}'"
            print(values[1])

            dados_questoes = consultar_tabela(conexao, 'questoes', 'letracerta, peso', seletor_questoes)
            dados_provas = consultar_tabela(conexao, 'provas', 'nome , turma, tipo, semestre, area', seletor_provas)

            caixa_materias.insert(0, dados_provas[0][4])
            caixa_turmas.insert(0, dados_provas[0][1])
            caixa_semestre.insert(0, dados_provas[0][3])
            caixa_tipo.insert(0, dados_provas[0][2])
            imput.insert(0, dados_provas[0][0])

            for i in range(len(caixa_questoes)):
                caixa_questoes[i].insert(0,dados_questoes[i][0])
                pesos[i].insert(0, dados_questoes[i][1])
            
        elif comando == "atualizar tabela": 
            data_frame = tv.selection()[0]
            values_tabela = tv.item(data_frame, 'values')
            area = str(caixa_materias.get())
            turma = str(caixa_turmas.get())
            semestre = str(caixa_semestre.get())
            tipo = str(caixa_tipo.get())
            nome_gabarito = str(imput.get())

            for caixa in caixa_questoes:
                questoes_marcadas.append(caixa.get())

            for peso in pesos:
                peso_questoes.append(peso.get())

            values_provas = f"`nome` = '{nome_gabarito}', area = '{area}', semestre = '{semestre}', turma = '{turma}'"
            seletor_provas = f"nome = '{values_tabela[1]}'" 

            conexao = conectar('localhost', 'root', '', 'gabaritos')  
            atualiza_tabela(conexao, 'provas',values_provas, seletor_provas)
            
            for i in range(len(caixa_questoes)):
                seletor_questoes = f"prova = '{values_tabela[1]}' AND questao =  'questao {i+1}'"
                values_questoes = f"letracerta = '{questoes_marcadas[i]}',  prova = '{values_tabela[1]}', peso = '{peso_questoes[i]}'"
                atualiza_tabela(conexao, 'questoes',values_questoes, seletor_questoes)
            
        elif comando == "teste":
            print("TESTANDO A FUNÇÃO...")

        desconectar(conexao) 



    window = Tk()
    window.config(padx=50, pady=50, bg='WHITE')
    pesos = []
    questoes = []
    materias = ['Mátematica', 'Ciências Humanas', 'Ciências da Natureza', 'Linguagens']
    turmas = ['1° Ano', '2° Ano', '3° Ano']
    semestre = ['semestre 1', 'semestre 2']
    tipo = ['semestral', 'Recuperação']
    alternativas = ['A', 'B', 'C', 'D', 'E']
    questoes_marcadas = []
    peso_questoes = []
    caixa_questoes = []
    inputs_infos = []
    pesos = []

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
    

    nome_do_gabarito = Label(window, text='Nome do Gabarito', anchor=W, bg='WHITE')
    nome_do_gabarito.pack()
    imput = Entry(window, width = 45)
    imput.pack()

    frame_infos = Frame(window, bg="WHITE")
    frame_infos.pack()
    frame_areas_turmas = Frame(window, bg='RED')
    frame_areas_turmas.pack()

    label_materias = Label(frame_areas_turmas, text='Areas', bg='WHITE')
    label_materias.pack(side='top')
    caixa_materias = ttk.Combobox(frame_areas_turmas, value=materias)
    caixa_materias.pack(side='top')

    label_turmas = Label(frame_areas_turmas, text='Turmas', bg='WHITE')
    label_turmas.pack(side='top')
    caixa_turmas = ttk.Combobox(frame_areas_turmas, value=turmas)
    caixa_turmas.pack(side='right')

    label_semestre = Label(frame_areas_turmas, text='semestre', bg='WHITE')
    label_semestre.pack()
    caixa_semestre = ttk.Combobox(frame_areas_turmas, value=semestre)
    caixa_semestre.pack(side='top')

    label_tipo = Label(frame_areas_turmas, text='Tipo', bg='WHITE')
    label_tipo.pack()
    caixa_tipo = ttk.Combobox(frame_areas_turmas, value=tipo)
    caixa_tipo.pack(side='right')


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

    salvar = Button(window, text='Salvar', command=lambda: conexao_com_banco_criar_gabarito("inserir na tabela"), width=20)
    salvar.pack(side = 'left', padx=10)
    obter = Button(window, text='Obter', command=lambda: conexao_com_banco_criar_gabarito("obter da tabela"), width=20)
    obter.pack(side = 'left', padx=10)
    editar = Button(window, text='Editar', command=lambda: conexao_com_banco_criar_gabarito("atualizar tabela"), width=20)
    editar.pack(side = 'left')

    frame_tabela = Frame(window, bg='WHITE')
    frame_tabela.pack(side = 'top', padx= 30, pady=30)
    
    conexao = conectar('localhost', 'root', '', 'gabaritos')  
    dados = consultar_tabela(conexao, 'provas', 'nome, turma, semestre', 1)
    desconectar(conexao)

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

    for i in range(len(dados)):

        tv.insert(parent='', index=i, iid=i, text='', values=(i, dados[i][0], dados[i][1],dados[i][2]))
    tv.pack()

    window.mainloop()
    
dados_corrigidos = []
dados_alunos = []

def corrigir_provas():

    def conexao_com_banco_corrigir_provas(comando):
        conexao = conectar('localhost', 'root', '', 'gabaritos') 

        if comando == "obter na tabela provas":
           nomes_das_provas = consultar_tabela(conexao, 'provas', 'nome', 1)
           return nomes_das_provas
        
        if comando == "selecionar gabarito":
            pesos = 1
            letras = 0
            condicional_provas = f"prova = '{caixa_gabaritos.get()}'"
            gabarito_da_questao = consultar_tabela(conexao, 'questoes', 'prova, letracerta, peso', condicional_provas)
            for letra, peso in range(len(gabarito_da_questao)):
                tv.insert(parent='', index=letra, iid=letra, text='', values=(f'Qestão{letra+1}', gabarito_da_questao[letras][letra],
                                                                                    gabarito_da_questao[pesos][peso]))



        desconectar(conexao)
    webcam = cv2.VideoCapture(0)
        
    def processar_gabarito():
        nome_aluno.delete(0, END)
        nota.delete(0, END)
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

        resultado_gabarito = []

        for i in range(len(gabarito_aluno)):
            if gabarito_aluno[i] == 0:
                tv2.insert(parent='', index=i, iid=i, text='', values=(f'Qestão{i+1}', questoes[i], 'Errado'))
                resultado_gabarito.append('Errado')
            else:
                tv2.insert(parent='', index=i, iid=i, text='', values=(f'Qestão{i+1}', questoes[i], 'Certo'))
                resultado_gabarito.append('Certo')

        gabarito = caixa_gabaritos.get()
        aluno = nome_aluno.get()
        gabarito = gabarito[::gabarito.find('[')]
        texto_aluno = texto_aluno.replace(' ', '')
        texto_aluno = texto_aluno + ".png"
        cv2.imshow(texto_aluno, paper)
        salva_imagem(paper, 'imagens_gabaritos', texto_aluno )

        dados_corrigidos.append(resultado_gabarito)

    window = Tk()
    window.config(padx=100, pady=100)


    frame_tabela = Frame(window)
    frame_tabela.pack(side = 'left')
    nomes_das_provas = conexao_com_banco_corrigir_provas("obter na tabela provas")
    print(nomes_das_provas)
    
    caixa_gabaritos = ttk.Combobox(frame_tabela, value=nomes_das_provas, width=45)
    caixa_gabaritos.pack(pady = 20)

    selecionar_gabarito = Button(frame_tabela, text='Selecionar Gabarito', 
                                 command=lambda: conexao_com_banco_corrigir_provas("selecionar gabarito"), width=20)
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






    









    












    
     
