# função
def contador(texto):
    maiusculo = 0
    minusculo = 0
    for c in texto:
        if c.isupper(): maiusculo += 1
        if c.islower(): minusculo += 1
    return print(f'Maiúsculas: {maiusculo}\nMinúsculas: {minusculo}')

#algoritmo
contador(input())