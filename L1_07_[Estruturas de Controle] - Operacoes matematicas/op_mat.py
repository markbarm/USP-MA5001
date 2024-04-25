# Dicionário com caracteres que representarão operaçõe
operacoes = {'+':'soma',
             '-':'subtracao',
             '*':'multiplicacao',
             '/':'divisao',
             '^':'potencia'}

# Função que reconhece operação e números
def reconhecer(linha):
    for i in range(1,len(linha)):
        if linha[i] in operacoes: return linha[i], int(linha[0:i]), int(linha[i+1:len(linha)])

# Funções
def soma(a,b):
    return a+b

def subtracao(a,b):
    return a-b

def multiplicacao(a,b):
    return a*b

def divisao(a,b):
    if b==0:
        return print('Erro: divisão por zero')
    return round(a/b,3)

def potencia(a,b):
    if (a,b)==(0,0):
        return print('Erro: base e expoente nulos')
    return a**b

# INÍCIO DO ALGORITMO
input= input()
# Identifica a operação e números
operacao, num1, num2 = reconhecer(input)
# imprime o resultado
print(eval(operacoes[operacao])(num1,num2))