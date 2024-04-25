# Entrada
min, max = map(int,input().split(','))

# Números divisíveis por 5 e 7 entre as entradas mínimo e máximo
divisores=[]
for n in range(min, max+1):
    if n%35 == 0: divisores.append(str(n))
print(','.join(divisores))
