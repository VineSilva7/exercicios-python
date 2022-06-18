def ficha(jogador ='<desconehcio>', gols = 0):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato')


n = str(input('Nome do Jogador ')).strip()
g = str(input('Número de gols: ')).strip()
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
