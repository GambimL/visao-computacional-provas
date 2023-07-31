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
