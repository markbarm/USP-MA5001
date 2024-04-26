from math import sqrt

#Crie uma classe para números complexos, ou seja, teremos um objeto x com parte real e imaginária: x.real e x.imag

class Complexo(object):

    def __init__(self,real,imag):
        self.real = float(real)
        self.imag = float(imag)
    
    def __str__(self):
        return format(self.real,'.2f') + "+" + format(self.imag,'.2f')+"i"
    
#Implemente as operações a seguir como métodos da classe complexo a ser criada: +, -, /, *, abs, ==.

    def __add__(self,other):
        resultado_real = self.real + other.real
        resultado_imag = self.imag + other.imag
        return Complexo(resultado_real,resultado_imag)

    def __sub__(self, other):
        resultado_real = self.real - other.real
        resultado_imag = self.imag - other.imag
        return Complexo(resultado_real,resultado_imag)
    
    def __mul__(self,other):
        resultado_real = self.real * other.real - self.imag * other.imag
        resultado_imag = self.real * other.imag + self.imag * other.real
        return Complexo(resultado_real,resultado_imag)
    
    def __abs__(self):
        return round(sqrt(self.real**2 + self.imag**2),2)
        
    def __truediv__(self,other):
        resultado_real = (self.real * other.real + self.imag * other.imag)/abs(other)
        resultado_imag = (-self.real * other.imag + self.imag * other.real)/abs(other)
        return Complexo(resultado_real,resultado_imag)

    def __eq__(self,other):
        if (self.real,self.imag)== (other.real,other.imag):
            return True
        else: 
            return False
            
def le_complexo(linha):
    real,imag = linha.split(',')
    return Complexo(real,imag)