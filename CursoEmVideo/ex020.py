from random import shuffle
a1 = str(input('Aluno 01: '))
a2 = str(input('Aluno 02: '))
a3 = str(input('aluno 03: '))
a4 = str(input('Aluno 04: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação é: {}'.format(lista))