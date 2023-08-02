import numpy as np

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
    

    array_metade_1 = array[:len(array)//2]
    array_metade_2 = array[len(array)//2:]
    print(len(array_metade_1))
    arrays = [(array_metade_1), (array_metade_2)]
    for q in range(1, 2):
        for i in range(0, 4):
            if i % 2 == 0:
                array_corrigido[(q*i)+10] = arrays[q][i]
            else:
                array_corrigido[q*i] = arrays[q][i]
    print(array_corrigido)
    return array_corrigido
