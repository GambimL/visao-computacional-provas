import pandas as pd
import os

def criar_dataframe(nome, questoes, pesos):
    provas = pd.DataFrame({'Questões': questoes, 
                        'Peso': pesos }, 
                        columns = ['Questões', 'Peso'])
    
    os.makedirs('C:/Users/usuario/Desktop/visãoprovas/bancodedados', exist_ok=True)
    provas.to_excel(f'C:/Users/usuario/Desktop/visãoprovas/bancodedados/{nome}.xlsx')
 
