#Função recursiva
def harmonica(n):
    #input: um número natural 'n'
    #output: série harmonica de 'n' termos
    return 1 if n == 1 else 1/n + harmonica(n-1)

#Algoritmo
print(round(harmonica(int(input())),3))