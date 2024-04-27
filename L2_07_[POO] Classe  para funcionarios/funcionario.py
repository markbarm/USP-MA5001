#Classe funcionário

class Funcionario(object):

    def __init__(self,nome,salario,dept):
        self.nome = nome
        self.salario = float(salario)
        self.dept = dept
    
    #método get_nome
    def get_nome(self):
        return self.nome
    
    #método set_salário
    def set_salario(self,horas):
        horas = int(horas)
        if horas > 50: self.salario *= horas/50

    #método set_departamento
    def set_departamento(self, dept):
        self.dept = dept
    
    #método __str__
    def __str__(self):
        return self.nome +' '+ format(self.salario,".1f") +' '+ self.dept
    
#Função 1. Recebe o nome e horas trabalhadas, retornando os dados do funcionário com o salário ajustado.
def ajuste_sal(lista,nome,horas):
    for f in lista:
        if f.nome == nome: 
            f.set_salario(horas)
            return print(f)
    return print('funcionario não encontrado')

#Função 2. 
def maior_sal(lista):
    maximo = 0
    for x in lista:
        if x.salario > maximo:
            f_maior = x
            maximo = x.salario
    return print(f_maior)

#Função 3. Recebe o nome e novo departamento do funcionário, retornando os dados atualizados.
def novo_dept(lista,nome, novo):
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

# Função Lê funcionário
def le_funcionario(linha):
    if '  ' in linha: linha = linha.replace('  ',' ')
    nome, sal, dept = linha.split(' ')
    return Funcionario(nome, sal, dept)

# Algoritmo

# Le dados da equipe de funcionarios
tam = int(input())

equipe = []
for i in range(tam):
    equipe.append(le_funcionario(input()))

opcao = int(input())

if opcao == 1:
    nome, horas = input().split(' ')
    ajuste_sal(equipe,nome,horas)
elif opcao == 2:
    maior_sal(equipe)
elif opcao == 3:
    nome, novo = input().split(' ')
    novo_dept(equipe,nome,novo)
else:
    media_sal(equipe)