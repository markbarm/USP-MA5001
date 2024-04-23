# Dicionário com caracteres que representarão operaçõe
operacoes = {'+':'soma',
             '-':'subtracao',
             '*':'multiplicacao',
             '/':'divisao',
             '**':'potencia',
             '==':'igualdade'}

# Classe fração e métodos
class Fracao(object):

    def __init__(self, num,den):
       self.num = num
       self.den = den
       self.simplificar()

    def mdc(self):
        num = int(self.num)
        den = int(self.den)
        resto = num % den
        while(resto):
            num = den
            den=resto
            resto=num%den
        return den

    def simplificar(self):
        divisor= self.mdc()
        self.num=int(self.num/divisor)
        self.den=int(self.den/divisor)
    
    def soma(self,outro):
       somaDen=self.den*outro.den
       somaNum=outro.den*self.num + self.den*outro.num
       return Fracao(somaNum,somaDen)

    def subtracao(self,outro):
       subDen=self.den*outro.den
       subNum=outro.den*self.num - self.den*outro.num
       return Fracao(subNum,subDen)
    
    def multiplicacao(self,outro):
       multDen=self.den*outro.den
       multNum=self.num*outro.num
       return Fracao(multNum,multDen)
    
    def divisao(self,outro):
       divDen=self.den*outro.num
       divNum=self.num*outro.den
       return Fracao(divNum,divDen)

    def igualdade(self,outro):
       if(self.num/self.den==outro.num/outro.den):
           return True
       return False

    def __str__(self):
       return str(self.num)+'/'+str(self.den)

# Função que le a fração
def input_fracao():
    a, b = map(int, input().split('/'))
    return Fracao(a,b)




# Algoritmo 
f1 = input_fracao()
f2 = input_fracao()
operacao = input()

# Realiza a operação
print(eval(f'f1.{operacoes[operacao]}(f2)'))

