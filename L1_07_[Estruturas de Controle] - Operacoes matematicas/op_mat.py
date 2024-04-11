from math import trunc

# dicionário com caracteres que representarão operaçõe
operacoes = {'+':'soma',
             '-':'subtracao',
             '*':'multiplicacao',
             '/':'divisao',
             '^':'potencia'}

# Função que reconhece operação e números
def reconhecer(linha):
    for i in range(1,len(linha)):
        if linha[i] in '+-*/^':
            return linha[i], int(linha[0:i]), int(linha[i+1:len(linha)])

# Funções
def soma(a,b):
    return print(a+b)

def subtracao(a,b):
    return print(a-b)

def multiplicacao(a,b):
    return print(a*b)

def divisao(a,b):
    if b==0:
        return print('Erro: divisão por zero')
    return print(trunc(a/b*1000)/1000)

def potencia(a,b):
    if (a,b)==(0,0):
        return print('Erro: base e expoente nulos')
    return print(a**b)

# INÍCIO DO ALGORITMO
input= input()
# Identifica a operação e números
symbol, num1, num2 = reconhecer(input)
# imprime o resultado
eval(operacoes[symbol])(num1,num2)