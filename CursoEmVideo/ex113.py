def leiaInt (msg):
    while True:
        try:
            num = int(input(msg))
        except (KeyboardInterrupt):
            print('\033[31mO USUARIO PREFERIU NÃO DIGITAR ESSE NÚMERO. \033[m')
            return 0
        except(ValueError, TypeError):
            print('\033[0;31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO.\033[m')
        else:
            break
    return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (KeyboardInterrupt):
            print('\033[31mO USUARIO PREFERIU NÃO DIGITAR ESSE NÚMERO. \033[m')
            return 0
        except(ValueError, TypeError):
            print('\033[0;31mErro! DIGITE UM NÚMERO REAL VÁLIDO.\033[m')
        else:
            break
    return num


n1 = leiaInt('Digite um numero inteiro: ')
n2 = leiaFloat('Digite um numero real: ')
print(f'O valor inteiro digitado foi {n1} e o valor real digitado foi {n2}')
