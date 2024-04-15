#FUNÇÃO QUE GIRA UM ROTOR
def girar(lista):
    tamanho = len(lista)
    aux=lista[0]
    for i in range(1,tamanho):
        lista[i-1]=lista[i]
    lista[tamanho-1]=aux
    return lista

#FUNÇÃO PARA DECRIPTOGRAFAR UM CARACTERE
def decriptogafar(i,r1,r2,r3,count):
    i=r3[r2[r1[i]]]
    r1 = girar(r1)
    count[0] += 1
    if count[0]//26 != count[1]:
        r2 = girar(r2)
        count[1] += 1
    if count[1]//26!=count[2]:    
        r3=girar(r3)
        count[2]+=1
    return i,r1,r2,r3,count


#INICIO DO ALGORITMO

contador = [0,0,0]


#RECEBE A LINHA: "ROTORES:"
input() 

#RECEBE INFORMAÇÃO DOS ROTORES
rotor_1 = list(map(int,input().split()))
rotor_2 = list(map(int,input().split()))
rotor_3 = list(map(int,input().split()))

input() #recebe linha em branco
input() #recebe linha: "MENSAGEM:"

while True:
    try:
        msg_decrip = ''
        line = input()
        for c in line:
            if ord(c) >= 65 and ord(c) <= 90: #caractere Maiúsculo
                index = ord(c)-65
                index,rotor_1,rotor_2,rotor_3,contador = decriptogafar(index,rotor_1,rotor_2,rotor_3,contador)       
                caractere = chr(index+65)
            elif ord(c)>=97 and ord(c)<=122: #caractere minúsculo               
                index = ord(c)-97
                index,rotor_1,rotor_2,rotor_3,contador = decriptogafar(index,rotor_1,rotor_2,rotor_3,contador)
                caractere = chr(index+97)
            else:
                caractere = c
            msg_decrip += caractere
        print(msg_decrip)
    except EOFError:
        break