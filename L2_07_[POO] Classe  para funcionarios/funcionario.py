#Classe funcionário

class Funcionario(object):

    def __init__(self,nome,salario,dept):
        self.nome = nome
        self.salario = salario
        self.dept = dept
    
    #método get_nome
    def get_nome(self):
        return self.nome
    
    #método set_salário
    def set_salario(self,horas):
        if horas > 50: self.salario *= horas/50

    #método set_departamento
    def set_departamento(self, dept):
        self.dept = dept
    
    #método __str__
    def __str__(self):
        return self.nome +' '+ self.salario +' '+ self.dept

#Função 1. Recebe o nome e horas trabalhadas, retornando os dados do funcionário com o salário ajustado.
def ajuste_sal(lista):
    nome,horas = input().split(' ')
    for f in lista:
        if f.nome == nome: 
            f.set_salario(horas)
            return print(f)
    return print('funcionario não encontrado')

#Função 2. Retorna o funcionário com maior salário

#Função 3. Recebe o nome e novo departamento do funcionário, retornando os dados atualizados.
def novo_dept(lista):
    nome, novo = input().split(' ')
    for f in lista:
        if f.nome == nome: 
            f.set_departamento(novo)
            return print(f)
    return print('funcionario não encontrado')

#Função 4. Retorna a média salarial da lista de funcionários
def media_sal(lista):
    media = 0
    for f in lista:
        media += f.salario/len(lista)
    return print('{0:.2f}'.format(media))

#dicionário com chave o número de função
opcoes = {'1':'ajuste_sal',
          '2':'maior_sal',
          '3':'novo_dept',
          '4':'media_sal'}

#Algoritmo
#recebe tamanho lista
tam = int(input())

#recebe lista de funcionários
equipe = []
for i in range(tam):
    nome, sal, dept = input().split(' ')
    equipe.append = Funcionario(nome,sal, dept)

#recebe solicitação
opcao = input()
#executa solicitação
eval(opcoes[opcao])(equipe)

    