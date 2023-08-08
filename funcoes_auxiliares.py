import numpy as np
import os
from itertools import chain

def trasnforma_letra_para_numero(dados):
        alternativas = []
        
        for dado in dados:
                dado = dado.replace(' ', '')
                if dado == 'A':
                    alternativas.append(0)
                elif dado == 'B':
                    alternativas.append(1)
                elif dado == 'C':
                    alternativas.append(2)
                elif dado == 'D':
                    alternativas.append(3)
                elif dado == 'E':
                    alternativas.append(4)
        return alternativas

def trnaforma_numero_para_letra(dados):
    alternativas = []
    for dado in dados:
            dado = dado.replace(' ', '')
            if dado == 'A':
                alternativas.append(0)
            elif dado == 'B':
                alternativas.append(1)
            elif dado == 'C':
                alternativas.append(2)
            elif dado == 'D':
                alternativas.append(3)
            elif dado == 'E':
                alternativas.append(4)
    return alternativas

def concerta_array(array):
    array_corrigido = np.zeros(20)
    for q in range(1, 2):
        for i in range(10):
            array_corrigido[2*i+1] = array[i]     
        for i in range(10):
            array_corrigido[2*i] = array[i+10]
    print(array_corrigido)
    return array_corrigido

def lista_arquivos_subdiretorios(diretorio):
    arquivos = []
    subdiretorios = os.listdir(diretorio)
    for i in range(len(subdiretorios)):
        subsubdiretorio1 = os.listdir(f'{diretorio}/{subdiretorios[i]}')
        for q in range(len(subsubdiretorio1)):
            arquivos.append(os.listdir(f'{diretorio}/{subdiretorios[i]}/{subsubdiretorio1[q]}'))

    arquivos = sum(arquivos, [])
    return arquivos

def retira_extensao(arquivo):
    retirar = arquivo[arquivo.find('.')::]
    arquivo = arquivo.replace(retirar, '')
    return arquivo
            

    
     


         
    
