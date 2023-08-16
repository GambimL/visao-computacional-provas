import pandas as pd
import os

def criar_dataframe(nome, questoes, pesos, area, turma, semestre, tipo):
    provas = pd.DataFrame({'Questões': questoes, 
                        'Peso': pesos }, 
                        columns = ['Questões', 'Peso'])

    
    os.makedirs('C:/Users/usuario/Desktop/visãoprovas/bancodedados', exist_ok=True)
    provas.to_excel(f'C:/Users/usuario/Desktop/visãoprovas/bancodedados/{turma}/{semestre}/{nome}[{area},{turma},{semestre},{tipo}].xlsx')
 


def obter_dataframe(dataframename):
    planilhas =  pd.read_excel(dataframename)
    questoes = []
    pesos = []
    
    for i in range(20):
        questoes.append(planilhas.loc[i, 'Questões'])
        pesos.append(planilhas.loc[i, 'Peso'])

    return questoes, pesos

def atualizar_dataframe(dataframename, questoesnovas, pesosnovos):
    planilhas =  pd.read_excel(f'bancodedados/{dataframename}')

    for i in range(20):
        planilhas.loc[i, 'Questões'] = questoesnovas[i]
        planilhas.loc[i, 'Peso'] = pesosnovos[i]

    os.makedirs('C:/Users/usuario/Desktop/visãoprovas/bancodedados', exist_ok=True)
    planilhas.to_excel(f'C:/Users/usuario/Desktop/visãoprovas/bancodedados/{dataframename}')

def criar_dataframe_generico(nome, export, coluna_inicial, nome_coluna_inicial, colunas, informacoes_colunas):

    dataframe = pd.DataFrame({
        nome_coluna_inicial : coluna_inicial
    })
    for i in range(len(colunas)):
        for g in range(len(informacoes_colunas[i])):
            dataframe[colunas[i]] = informacoes_colunas[i]
    

    os.makedirs(f'{export}', exist_ok=True)
    dataframe.to_excel(f'{export}/{nome}')



    


    
