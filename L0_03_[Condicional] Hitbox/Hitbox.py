#Função que lê os dados de um retângulo
def le_rect():
    lista = []
    teste = True
    while teste:
        lista = list(map(int,input().split()))
        if (lista[2],lista[3]) >= (0,0):
            teste = False
    return lista

#Função que determina possível intersecção entre dois retângulos
def intersec(rect_1,rect_2):
    lista = []
    lista.append(max(rect_1[0] , rect_2[0]))
    lista.append(max(rect_1[1] , rect_2[1]))
    lista.append(min(rect_1[0] + rect_1[2],rect_2[0] + rect_2[2]) - lista[0])
    lista.append(min(rect_1[1] + rect_1[3],rect_2[1] + rect_2[3]) - lista[1])
    if (lista[2],lista[3]) >= (0,0):
        print(f'HIT: {lista[0]} {lista[1]} {lista[2]} {lista[3]}')
    else:
        print('MISS')


#Algoritmo
retangulo_1 = le_rect()
retangulo_2 = le_rect()
intersec(retangulo_1,retangulo_2)