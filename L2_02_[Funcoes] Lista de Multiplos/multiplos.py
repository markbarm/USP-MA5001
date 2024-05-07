def multiplos(m,M,i,j):
    lista = [str(n) for n in range(m, M+1) if n%(i*j) == 0]
    return print(','.join(lista))

# Algoritmo
min, max = map(int,input().split(','))
x, y = map(int,input().split(','))
multiplos(min, max,x,y)
