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
    