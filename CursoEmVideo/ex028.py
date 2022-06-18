from random import randint
from time  import sleep
print('Deixe-me pensar em um número entre 0 e 5, humm')
computador = randint(0, 5)
jogador = int(input('Qual número você acha que eu escolhi?'))
sleep(2)
if computador == jogador:
    print('Parabéns, Você acertou em cheio!')
else:
    print('Não foi esse número, quem sabe na proxima!! o número escolhi foi {}'.format(computador))