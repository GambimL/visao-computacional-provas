import pandas as pd
import os

def criar_dataframe(nome, questoes, pesos, area):
    provas = pd.DataFrame({'Questões': questoes, 
                        'Peso': pesos }, 
                        columns = ['Questões', 'Peso'])

    
    os.makedirs('C:/Users/USER/Desktop/Visao_provas/bancodedados', exist_ok=True)
    provas.to_excel(f'C:/Users/USER/Desktop/Visao_provas/bancodedados{nome}[{area}].xlsx')
 


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

    os.makedirs('C:/Users/USER/Desktop/Visao_provas/bancodedados', exist_ok=True)
    planilhas.to_excel(f'C:/Users/USER/Desktop/Visao_provas/bancodedados{dataframename}')
    


    
