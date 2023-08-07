import numpy as np
import os

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

def lista_arquivos_subdiretorios():
    arquivos = []
    subdiretorios = os.listdir('C:/Users/usuario/Desktop/visãoprovas/bancodedados')
    for subdiretorio in subdiretorios:
        subsubdiretorios1 = os.listdir(f'C:/Users/usuario/Desktop/visãoprovas/bancodedados/{subdiretorio}')
        for subsubdiretorio1 in subsubdiretorios1: 
            arquivos.append(os.listdir(f'C:/Users/usuario/Desktop/visãoprovas/bancodedados/{subdiretorio}/{subsubdiretorio1}'))
    
    return arquivos


         
    
