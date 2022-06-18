tabela = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco',
          'Chapecoense', 'Atletico Mineiro', 'Botafogo', 'Athetico Paranaense', 'Bahia', 'São Paulo',
          'Fuminense', 'Sport', 'Vitoria', 'Coritiba', 'Avai', 'Ponte Preta', 'Atlético Goianiense')

print(f'Os 5 primeiros colocados do Campeonato Brasileiro são: {tabela[0:5]}')
print('-'*30)
print(f'Os 4 últimos colocados do Campeonato Brasileiro são: {tabela[-4:]}')
print('-'*30)
print(f'A ordem alfabética dos times: {sorted(tabela)}')
print('-'*30)
print(f'A posição da Chapecoense é {(tabela.index("Chapecoense")+1)}')
