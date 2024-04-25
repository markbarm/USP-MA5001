from datetime import date

def days(birthday,today):
    # input: data de aniversário e data atual
    # output: dias de idade depois do último aniversário de mês

    # data do último aniversário de mês
    if birthday[0] <= today[0]:
        # mês atual
        t1 = date(today[2],today[1],birthday[0])
    else:
        # mês anterior
        if today[1]>1:    
            t1 = date(today[2],today[1]-1,birthday[0])
        else:
            t1 = date(today[2]-1,12,birthday[0])
    # data atual
    t2 = date(today[2],today[1],today[0])
    return (t2-t1).days + 1

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

    age = today[2] - birthday[2]
    
    #correção se ainda não fez aniversário
    if birthday[1] > today[1]: return age - 1
    if birthday[1] == today[1] and birthday[0] > today[0]: return age - 1
    
    return age
    


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
