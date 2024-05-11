def caracteres(lista):
    
    if len(lista)==1:
        if lista[0].isupper():
            return 'M' #Maiúsculo
        elif lista[0].islower():
            return 'm' #minúsculo
        elif lista[0].isdigit():
            return 'd' #dígito
        else:
            return '@' #não alfanumérico
    else: 
        return caracteres([lista.pop(0)]) + caracteres(lista)


#algoritmo
senha = input()
if len(senha) >= 8 and len(set(caracteres(list(senha)))) >= 4:
    print('Válida')
else:
    print('Inválida')