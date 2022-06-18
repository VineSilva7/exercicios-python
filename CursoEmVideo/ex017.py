from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = hypot(ca, co)
print('Hipotenusa é igual a {}'.format(h))
