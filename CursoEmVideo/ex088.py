from random import sample
from time import sleep
print('-'*40)
print(f'{"JOGO NA MEGA SENA":^40}')
print('-'*40)
quantidade = int(input('Quantos jogos você quer que eu sorteie: '))
print(f'{f" SORTEANDO {quantidade} JOGOS ":-^40}')
numeros = list(range(0, 61))
for c in range(0, quantidade):
    print(f'Jogo {c+1}: {sorted(sample(numeros, 6))}')
    sleep(1)
print(f'{f" BOA SORTE !!! ":-^40}')
