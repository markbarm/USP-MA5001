
# FUNÇÃO ANDAR
def andar(x,y,direcao,passos):
    #direção: 0 -> direita, 1 -> esquerda, 2-> cima, 3-> baixo
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
    x,y,d = 0,-1,0       # parametros iniciais
    teste = True            
    while teste:
        if steps > number:
            x,y = andar(x,y,d,number)    
            steps -= number
            d += 1  
            number -= d%2 
        else:
            x,y = andar(x,y,d,steps)    
            teste = False  
    return print(f'O astronauta esta na posicao: {x} {y}')

# Algoritmo
N,P = map(int,input().split()) # Entrada do número de posições por lado, e posição do astronauta
L = N*N  # Número de lugares na fila

if P>L:
    print(f"O astronauta ja saiu em missao ha {P-L} chamadas.")
elif P<L:    
    pos_final(P,N)
    print(f"Ainda faltam {L-P} chamadas para a sua vez!")
else:
    pos_final(P,N)
    print(f"Preste atencao, astronauta, chegou a sua vez!")
        


    