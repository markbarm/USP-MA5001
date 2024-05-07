from math import ceil, sqrt

def is_prime(n):
    # input: número natural
    # output: 'True' se for primo ou 'False' se não for primo
    for i in range(2,ceil(sqrt(n))):
        if n%i == 0:
            return False
    return True

# Algoritmo
min, max = map(int,input().split(' '))

primes=[n for n in range(min, max+1) if is_prime(n)]

print(*primes) if len(primes)>0 else print('Não há números primos')
