#Função recursiva
def harmonica(n):
    #input: um número natural 'n'
    #output: série harmonica de 'n' termos
    if n == 1:
        return 1
    else:
        return 1/n + harmonica(n-1)

#Algoritmo
print(round(harmonica(int(input())),3))