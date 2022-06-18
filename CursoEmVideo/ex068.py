from random import randint
print('Jogo do PAR ou IMPAR')
v = 0
while True:
    print('-' * 30)
    player = int(input('Escolha um número: '))
    computador = randint(0, 10)
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par OU Inpar [P/I}')).upper().strip()[0]
    resultado = player + computador
    print(f'Voce jogou {player} e o computador jogou {computador}, total {resultado}')
    print('DEU PAR' if resultado % 2 == 0 else 'DEU IMPAR')
    if resultado % 2 == 0:
        if escolha == 'P':
            print('Voce VENCEU')
            v += 1
        else:
            break
    else:
        if escolha == 'I':
            print('Voce Ganhou')
            v += 1
        else:
            break
print('-'*30)
print('Jogo Finalizado')
print(f'Voce ficou invicto {v} vezes')
