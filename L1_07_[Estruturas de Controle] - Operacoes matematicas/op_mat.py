# Funções
def soma(a,b):
    return a+b

def subtracao(a,b):
    return a-b

def multiplicacao(a,b):
    return a*b

def divisao(a,b):
    if b==0:
        return 'Erro: divisão por zero'
    return round(a/b,3)

def potencia(a,b):
    if (a,b)==(0,0):
        return 'Erro: base e expoente nulos'
    return a**b

# Função que reconhece operação e números
def reconhecer(linha):
    for i, c in enumerate(linha):
        if c in '+-*/^': 
            return linha[i], int(linha[0:i]), int(linha[i+1:len(linha)])

# Função que executa a entrada
def executar_op(linha):
    operacoes = {
                '+':soma,
                '-':subtracao,
                '*':multiplicacao,
                '/':divisao,
                '^':potencia
    }
    op, num1, num2 = reconhecer(linha) 
    return operacoes.get(op)(num1,num2)

# Algoritmo
print(executar_op(input()))