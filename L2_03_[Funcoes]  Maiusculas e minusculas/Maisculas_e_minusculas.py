#Função
def contador(texto):
    #Input: string
    #Output: número de caracteres Maiúsculas e minúsculas
    maiusculo = 0
    minusculo = 0
    for c in texto:
        if c.isupper(): maiusculo += 1
        if c.islower(): minusculo += 1
    return print(f'Maiúsculas: {maiusculo}\nMinúsculas: {minusculo}')

#Algoritmo
contador(input())