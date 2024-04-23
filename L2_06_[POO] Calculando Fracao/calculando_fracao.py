class Fracao(object):

   def __init__(self, num,den):
       self.num=num
       self.den=den
       self.simplificar()

   def __add__(self,outro):
       somaDen=self.den*outro.den
       somaNum=outro.den*self.num + self.den*outro.num
       if(somaNum%somaDen==0):
           somaNum=somaNum//somaDen
           somaDen=1
       return Fracao(somaNum,somaDen)

   def __eq__(self,outro):
       if(self.num/self.den==outro.num/outro.den):
           return True
       return False

   def mdc(self):
       num=int(self.num)
       den=int(self.den)
       resto = num % den
       while(resto):
        num=den
        den=resto
        resto=num%den
       return den

   def simplificar(self):
       divisor= self.mdc()
       self.num=int(self.num/divisor)
       self.den=int(self.den/divisor)


   def __str__(self):
       return str(self.num)+'/'+str(self.den)