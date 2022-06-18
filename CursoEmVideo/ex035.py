a = float(input('Primeiro Comprimento: '))
b = float(input('Segundo Comprimento: '))
c = float(input('Terceiro Comprimento: '))
if ((abs( b -c )) < a < b + c) and ((abs( a -c )) < b < a + b) and ((abs( a - b )) < c < a + b):
    print('Esses dados PODEM FORMAR em triângulo')
else:
    print('Esses dados NÂO FORMAM um triãngulo')