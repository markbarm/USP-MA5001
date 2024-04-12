def is_prime(n):
    # input: número natural
    # output: 'True' se for primo ou 'False' se não for primo
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

# Entrada
min, max = map(int,input().split(' '))

# Números primos entre as entradas mínimo e máximo
primes=[]
for n in range(min, max+1):
    if is_prime(n):
        primes.append(n)

# Imprime a saída
if len(primes)>0:
    print(*primes)
else:
    print('Não há números primos')
