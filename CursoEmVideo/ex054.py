from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Em que ano nasceu a {} pessoa? '.format(c)))
    anoatual = date.today().year
    idade = anoatual - ano
    if idade < 21:
        maior += 1
    elif idade >= 21:
        menor += 1
if maior == 1:
    print('{} pessoa nao atingiu a maioridade'.format(maior))
    print('E {} ja sao maiores'.format(menor))
elif maior > 1:
    print('{} pessoas nao atingiram a maioridade'.format(maior))
    print('E {} ja sao maiores'.format(menor))
else:
    print('Todos sao maiores')