jogador = {}
gols = []
jogador['nome'] = str(input('Qual o nome do jogador? '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-' * 60)
print(jogador)
print('-' * 60)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-' * 60)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'  ==> Na partida {i+1}, faz {v} gols')
print(f'Foi um total de {jogador["total"]} gols')
