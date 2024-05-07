def soma(list):
    return list.pop() if len(list)==1 else list.pop() + soma(list)
                 
#Algoritmo
print(soma(list(map(int,input().split(' ')))))