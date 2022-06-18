from operator import itemgetter
from random import randint
from time import sleep
jogo = dict()
ranking = list()
for c in range(1, 5):
    jogo[f'jogador{c}'] = randint(1, 6)
print('Valores Sorteados')
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado. ')
    sleep(1)
print('-'*30)
print(f'{"== RANKING DOS JOGADORES ==":^30}')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'O {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
