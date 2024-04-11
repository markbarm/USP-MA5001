#Listas que serão usadas para armazenar as informações dos retângulos
retangulo_1 = []
retangulo_2 = []
retangulo_3 = []


# Leitura de informações do retângulo 1. 
teste = True
while teste:
    retangulo_1 = list(map(int,input().split()))
    if retangulo_1[2] >= 0 and retangulo_1[3] >= 0:
        teste = False

# Leitura de informações do retângulo 2
teste = True
while teste:
    retangulo_2 = list(map(int,input().split()))
    if retangulo_2[2] >= 0 and retangulo_2[3] >= 0:
        teste = False

# calcula dimensões da possível intersecção dos retângulos 
retangulo_3.append(max(retangulo_1[0] , retangulo_2[0]))
retangulo_3.append(max(retangulo_1[1] , retangulo_2[1]))
retangulo_3.append(min(retangulo_1[0] + retangulo_1[2],retangulo_2[0] + retangulo_2[2]) - retangulo_3[0])
retangulo_3.append(min(retangulo_1[1] + retangulo_1[3],retangulo_2[1] + retangulo_2[3]) - retangulo_3[1])

# Se ambos lados forem positivos então há intersecção
if retangulo_3[2] >= 0 and retangulo_3[3] >= 0:
    print(f'HIT: {retangulo_3[0]} {retangulo_3[1]} {retangulo_3[2]} {retangulo_3[3]}')
else:
    print('MISS')
