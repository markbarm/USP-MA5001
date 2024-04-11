#Importar biblioteca 
import codecs

#inteiro para hexadecimal
number_hex=format(int(input()),'x')

#corrige os casos em que a representação hexagesimal possuir um número ímpar de digitos.
if len(number_hex)%2!=0:            
    number_hex='0'+number_hex

#conversão para bytes
number_bytes=bytes.fromhex(number_hex)


#decodificando em utf-8
number_decoded=codecs.decode(number_bytes, 'utf-8',errors='replace')
print(number_decoded)

