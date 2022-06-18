soma = 0
cont = 0
p1 = int(input('Primeiro número do intervalo: '))
p2 = int(input('Segundo número do intervalo: '))
for c in range(p1, p2+1, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('A soma de {} números será {}'.format(cont, soma))
