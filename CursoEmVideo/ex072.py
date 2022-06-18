numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
           'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
           'Doze', 'treze', 'Catorze', 'Quinze', 'Dezesseis',
           'Dezesete', 'Dezoito', 'Desenove', 'Vinte')
while True:
    escolha = int(input('Digite um número entre 0 e 20: '))
    while escolha > 20 or escolha < 0:
        escolha = int(input('Tente. Novamente. Digite um número entre 0 e 20: '))
    print(f'Voce escolheu número {numeros[escolha]}')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('QUer continuar [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
print('Operação Finalizada')
