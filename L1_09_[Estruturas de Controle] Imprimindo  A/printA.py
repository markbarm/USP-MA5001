for i in range(7):
    linha = ''
    for j in range(7):
        if i in (0,3) and j in (2,3,4):
            linha += '*'
        elif i in range(1,7) and j in (1,5):
            linha += '*'
        else:    
            linha += ' '
    print(linha)
