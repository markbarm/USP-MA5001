from math import sin, cos

class Complexo_Polar(object):

    def __init__(self, modulo, fase):
        self.modulo = float(modulo)
        self.fase = float(fase)

    def __str__(self):
        return '{0:.2f}[({1:.2f})+i({2:.2f})]'.format(self.modulo,cos(self.fase),sin(self.fase))

    def __mul__(self,outro):
        return Complexo_Polar(self.modulo * outro.modulo , self.fase + outro.fase)
    
    def __truediv__(self,outro):
        if outro.modulo != 0:
            return  Complexo_Polar(self.modulo / outro.modulo , self.fase - outro.fase) 

    def __pow__(self,potencia):
        self.modulo**=potencia
        self.fase*=potencia
        return Complexo_Polar(self.modulo,self.fase)
    

def le_complexo(linha):
    modulo, fase = linha.split(',')
    return Complexo_Polar(modulo, fase)

# Algoritmo
ops =  list(input().split(' '))
a = le_complexo(input())
b = le_complexo(input())

for i,op in enumerate(ops):
    if op in '*/':
        print('{0}:{1}'.format(op,eval(f'a{op}b')))
    if op =='**':
        print('{0}:{1}\n{0}:{2}'.format(op,eval(f'a{op}{int(ops[i+1])}'),eval(f'b{op}{int(ops[i+1])}')))