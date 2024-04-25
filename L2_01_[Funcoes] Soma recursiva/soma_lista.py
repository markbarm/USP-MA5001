def soma(list):
    if len(list)==0:
        return 0
    elif len(list)==1:
        return list.pop()
    else:
        return list.pop() + soma(list)
                 
#Algoritmo
print(soma(list(map(int,input().split(' ')))))