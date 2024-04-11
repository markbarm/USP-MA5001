from datetime import datetime

def days(birthday,today):
    # input: data de aniversário e data atual
    # output: dias de idade depois do último aniversário de mês
    
    # data do último aniversário de mês
    if birthday[0] <= today[0]:
        # mês atual
        t1 = datetime(today[2],today[1],birthday[0])
    else:
        # mês anterior
        t1 = datetime(today[2],today[1]-1,birthday[0])
    
    # data atual
    t2 = datetime(today[2],today[1],today[0])

    # dias depois do último aniversário de mês
    t3 = (t2-t1).days + 1
    return t3

def months(birthday,today):
    # input: data de aniversário e data atual
    # output: meses de idade depois do último aniversário

    if birthday[0] <= today[0]:
        return (12 + today[1] - birthday[1])%12
    else:
        return (11 + today[1] - birthday[1])%12
    
def years(birthday,today):
    # input: data de aniversário e data atual
    # output: anos de idade
    if birthday[0] <= today[0] and birthday[1] <= today[1]:
        return today[2] - birthday[2]
    else:
        return today[2] - birthday[2]-1
    


# INICIO DO ALGORITMO
hoje = [4, 4, 2024]

# ENTRADA DA DATA DE NASCIMENTO
aniversario = list(map(int,input().split('/')))

# CALCULO DA IDADE
idade = []
idade.append(days(aniversario,hoje))
idade.append(months(aniversario,hoje))
idade.append(years(aniversario,hoje))

# Imprime a idade em anos, meses e dias.
if idade[1]==1:
    print (f'{idade[2]} anos, {idade[1]} mes e {idade[0]} dias')
else:
    print (f'{idade[2]} anos, {idade[1]} meses e {idade[0]} dias')
