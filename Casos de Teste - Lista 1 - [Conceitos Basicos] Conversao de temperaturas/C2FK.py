celcius=input()
celcius=int(celcius[:len(celcius)-2])
if celcius%5==0:
    print(f'{9*celcius//5+32} F')
else:
    print(f'{9*celcius/5+32} F')
print(f'{celcius+273} K')