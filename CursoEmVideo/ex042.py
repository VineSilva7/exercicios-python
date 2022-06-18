a = float(input('Primeiro Comprimento: '))
b = float(input('Segundo Comprimento: '))
c = float(input('Terceiro Comprimento: '))
if ((abs( b -c )) < a < b + c) and ((abs( a -c )) < b < a + b) and ((abs( a - b )) < c < a + b):
    print('Esses dados PODEM FORMAR em triângulo')
    if a == b == c:
        print('Triângulo EQUILÁTERO')
    elif a == b or a == c or b == c:
        print('Triângulo ISÓSCELES')
    elif a != b != c != a:
        print('Triângulo ESCALENO')
else:
    print('Esses dados NÂO FORMAM um triãngulo')
