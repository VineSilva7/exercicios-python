from random import randint
from time import sleep


def sorteio (nume):
    print(f'Sorteando os 5 valores da lista temos: ', end='')
    for c in range(0, 5):
        nume.append(randint(1, 10))
    for c in nume:
        print(f'{c} ', end='')
        sleep(0.4)
    print()


def somapar(nume):
    soma = 0
    for c in nume:
        if c % 2 == 0:
            soma += c
    print(f' Somando os valores de {nume} temos: {soma}')


numeros = list()
sorteio(numeros)
somapar(numeros)