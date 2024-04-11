def is_perfect(n):
    # input: número natural
    # output: 'True' se for perfeito ou 'False' se não for perfeito
    soma = 0 
    test = True
    for i in range(1,n):
        if n%i == 0:
            soma += i
    if soma != n:
        test = False
    return test 


# Correção de bug na entrada 1 do runcodes
input=input()
if '  ' in input:
    input=input.replace('  ', ' ')

# Entrada
min, max = map(int,input.split(' '))

# Números perfeitos entre mín e máx
perfect=[]
for n in range(min, max+1):
    if is_perfect(n):
        perfect.append(n)

# Imprime a saída
if len(perfect)>0:
    [print(perfect[i]) for i in range(len(perfect))]
else:
    print('Não foi encontrado número perfeito')
