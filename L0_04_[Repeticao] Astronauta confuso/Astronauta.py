
# FUNÇÃO ANDAR
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

# FUNÇÃO POSIÇÃO FINAL
def pos_final(steps,number):
    x = 0                   #índice da linha
    y = -1                  #índice da coluna
    d = 0                   #definir uma direção: 0 -> direita, 1 -> esquerda, 2-> cima, 3-> baixo
    teste = True            #controle para fechar o loop
    while teste:
        if steps > number:
            x,y = andar(x,y,d,number)    
            steps -= number
            d += 1  
            number -= d%2 
        else:
            x,y = andar(x,y,d,steps)    
            teste = False  
    return x,y

# Entrada do número de posições por lado, e posição do astronauta
N,P = map(int,input().split())

# Número de lugares na fila
L = N*N 

if P>L:
    print(f"O astronauta ja saiu em missao ha {P-L} chamadas.")
else:    
    i,j = pos_final(P,N)
    if P<L:    
        print(f"O astronauta esta na posicao: {i} {j}\nAinda faltam {L-P} chamadas para a sua vez!")
    else:
        print(f"O astronauta esta na posicao: {i} {j}\nPreste atencao, astronauta, chegou a sua vez!")
        


    