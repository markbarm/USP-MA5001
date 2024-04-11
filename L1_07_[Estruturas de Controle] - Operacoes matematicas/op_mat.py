import math

# dicionário com caracteres que representarão operaçõe
operacoes = {'+':'soma',
             '-':'subtracao',
             '*':'multiplicacao',
             '/':'divisao',
             '^':'potencia'
             }

# criar funções para cada operção: 
# Soma (+), subtração (-), multiplicação(*),  divisão(/) e potência (^)


def soma(a,b):
    return a+b
def subtracao(a,b):
    return a-b
def multiplicacao(a,b):
    return a*b
def divisao(a,b):
    if b==0:
        return 'Erro: divisão por zero'
    return math.trunc(a/b*1000)/1000
def potencia(a,b):
    if (a,b)==(0,0):
        return 'Erro: base e expoente nulos'
    return a**b

def aplicacao(func,a,b):
    return func(a,b)


# a entrada será do tipo string e usando um loop será o processo da identificação
for i in range(1,len(input_)):
    if input_[i] in '+-*/^':
        symbol=input_[i]
        num1=int(input_[0:i])
        num2=int(input_[i+1:len(input_)])
        break
aplicacao(eval(operacoes[symbol]),num1,num2)