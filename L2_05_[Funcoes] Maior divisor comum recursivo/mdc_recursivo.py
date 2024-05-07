#Função Recursiva
def mdc(p,q):
    #input: recebe dois números inteiros
    #output: máximo divisor comum dos números
    m,n = max(p,q),min(p,q)
    return n if m%n==0 else mdc (n,m%n)
    

#Algoritmo
a,b = map(int,input().split(' '))
print(mdc(a,b))