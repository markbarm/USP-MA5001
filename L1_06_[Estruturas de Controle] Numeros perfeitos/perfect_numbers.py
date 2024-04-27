def is_perfect(n):
    # input: número natural
    # output: 'True' se for perfeito ou 'False' se não for perfeito
    soma = 1 
    for i in range(2,n):
        if n%i == 0:
            soma += i
    if soma != n:
        return False
    return True


# Correção de bug na entrada 1 do runcodes
linha = input()
if '  ' in linha: linha = linha.replace('  ', ' ')

min, max = map(int,linha.split(' '))

perfect=[]
for n in range(min, max+1):
    if is_perfect(n): perfect.append(n)

[print(perfect[i]) for i in range(len(perfect))] if len(perfect)>0 else print('Não foi encontrado número perfeito')
