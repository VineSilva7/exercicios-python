def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[0;31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO.\033[m')
        if ok:
            break
    return valor



n = leiaInt('Digite um numero: ')
print(f'Você acabou de digitar o número {n}')
