
#função andar
def andar(x,y,direcao,passos):
    if direcao%4 == 0:      
        y += passos
    elif direcao%4 == 1:
        x += passos
    elif direcao%4 == 2:
        y -= passos
    else:
        x -= passos
    return x,y


N,P = map(int,input().split())
L = N*N # número de lugares na fila
if P>L:
    print(f"O astronauta ja saiu em missao ha {P-L} chamadas.")
else:    
    i = 0                   #índice da linha
    j = -1                  #índice da coluna
    P1 = P                  #contabiliza passos que irá dar para ocupar a posição P
    d = 0                   #definir uma direção: 0 -> direita, 1 -> esquerda, 2-> cima, 3-> baixo
    teste = True            #controle para fechar o loop
    while teste:
        if P1 <= N:
            i,j = andar(i,j,d,P1)    
            teste = False      
        else:
            i,j = andar(i,j,d,N)    
            P1 -= N
            d += 1  
            N -= d%2
    if P<L:    
        print(f"O astronauta esta na posicao: {i} {j}\nAinda faltam {L-P} chamadas para a sua vez!")
    else:
        print(f"O astronauta esta na posicao: {i} {j}\nPreste atencao, astronauta, chegou a sua vez!")
        


    