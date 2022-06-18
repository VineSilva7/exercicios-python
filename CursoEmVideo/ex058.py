from random import randint
print('Deixe-me pensar em um número entre 0 e 10, humm')
computador = randint(0, 10)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite?'))
    palpites += 1
    if computador == jogador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez')
        elif jogador > computador:
            print('Menos... Tente mais uma vez')
print('Parabéns, Você acertou !')
print('E precisou de {} chances'.format(palpites))
