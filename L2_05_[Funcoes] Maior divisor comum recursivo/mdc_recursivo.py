#Função Recursiva
def mdc(p,q):
    #input: recebe dois números inteiros
    #output: máximo divisor comum dos números
    m,n = max(p,q),min(p,q)
    if m%n == 0:
        return n
    else:
        return mdc(n,m%n)

#Algoritmo
a,b = map(int,input().split(' '))
print(mdc(a,b))