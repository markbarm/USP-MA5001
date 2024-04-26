from math import factorial

# função iterativa - sen(x)
def sen(x,n):
    s = 0
    for i in range(n):
        s += ((-1)**i)*(x**(2*i+1))/(factorial(2*i+1)) #incremento do i-ésimo termo da série
    return s

# função recursiva - cos(x)
def cos(x,n):
    if n == 1: 
        return 1
    else: 
        c_n = ((-1)**(n-1))*(x**(2*(n-1)))/(factorial(2*(n-1))) #calculo do n-ésimo termo da série
        return c_n + cos(x,n-1)

# Algoritmo
x,n = input().split(' ')
x,n = float(x), int(n)
print('{0:.3f}\n{1:.3f}'.format(sen(x,n),cos(x,n)))
