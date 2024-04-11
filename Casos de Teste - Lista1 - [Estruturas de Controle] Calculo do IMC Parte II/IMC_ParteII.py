import math

while True:
    try:
        altura, massa = map(float,input().split(","))
        imc = math.floor(100*massa/altura**2)/100
        if imc < 18.5:
            print('{0:.2f} Baixo peso'.format(imc))
        elif imc < 25.0:
            print('{0:.2f} Peso adequado'.format(imc))
        else:
            print('{0:.2f} Sobrepeso'.format(imc))
    except EOFError:
        break
