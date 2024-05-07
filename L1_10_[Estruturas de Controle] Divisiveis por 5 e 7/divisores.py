# Entrada
min, max = map(int,input().split(','))

# Números divisíveis por 5 e 7 entre as entradas mínimo e máximo
divisores=[str(n) for n in range(min, max+1) if n%35 == 0]
print(','.join(divisores))
