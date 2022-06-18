from random import randint
from time import sleep
print(f'{" JOKEMPÔ ":=^40}')
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('Escolha uma das opções a seguir:')
print('[0] - PEDRA')
print('[1] - PAPEL')
print('[2] - TESOURA')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('--' * 20)
print('Jogador escolheu {}'.format(itens[jogador]))
print('Computador escolheu {}'.format(itens[computador]))
print('--' * 20)
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2: # computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
