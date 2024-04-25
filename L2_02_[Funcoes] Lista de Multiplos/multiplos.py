def multiplos(m,M,i,j):
    lista = []
    for n in range(m, M+1):
        if n%(x*y) == 0: lista.append(str(n))
    return print(','.join(lista))

# Algoritmo
min, max = map(int,input().split(','))
x, y = map(int,input().split(','))
multiplos(min, max,x,y)
