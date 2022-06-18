print('-'*30)
print('{:^30}'.format('BANCO CEV'))
print('-'*30)
valor = int(input('Valor a sacar: R$'))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('-'*30)
print('Volte sempre ao BANCO CEV')




#valor = int(input('Valor a sacar: R$'))
#nota50 = valor // 50
#restante50 = valor % 50
#nota20 = restante50 // 20
#restante20 = restante50 % 20
#nota10 = restante20 // 10
#restante10 = restante20 % 10
#nota1 = restante10 // 1
#restante1 = restante10 % 1
#if nota50 != 0:
#    print(f'notas de R$50 : {nota50}')
#if nota20 != 0:
#    print(f'notas de R$20 : {nota20}')
#if nota10 != 0:
#    print(f'notas de R$10 : {nota10}')
#if nota1 != 0:
#    print(f'notas de R$1 : {nota1}')
