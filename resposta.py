
def calcula_total(acertos, peso):
    total = 0
    for i in range(len(peso)):
        resultado = peso[i] * acertos
        total = total+resultado
    
    return total
