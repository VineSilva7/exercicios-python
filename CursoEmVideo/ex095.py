lista = []
jogador = {}
gols = []
while True:
    jogador['nome'] = str(input('Nome do jogador? '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    lista.append(jogador.copy())
    gols.clear()
    jogador.clear()
    while True:
        cont = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if cont in 'SN':
            break
        else:
            print('ERRO! Responda apenas S ou N')
    if cont == 'N':
        break
print('-' * 60)
print(f'Cod. ', end='')
for c in lista[0]:
    print(f'{c:<20}', end='')
print()
print('-' * 60)
for c, k in enumerate(lista):
    print(f'{c:>3}  ', end='')
    for v in k.values():
        print(f'{str(v):<20}', end='')
    print()
print('-' * 60)
while True:
    dados = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    if dados == 999:
        break
    if dados <= len(lista)-1:
        print(f'Levantamento de dados do Jogador {lista[dados]["nome"]}')
        for c, v in enumerate(lista[dados]["gols"]):
            print(f'Na partida {c+1} ele fez {v} gols')
    else:
        print(f'ERRO! Não existe jogador com codigo {dados}')
    print('-' * 60)
print('<<< VOLTE SEMPRE >>>')