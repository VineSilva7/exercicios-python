from time import sleep
c = ('\033[m',
     '\033[0;97;41m',
     '\033[0;97;42m',
     '\033[0;97;43m',
     '\033[0;97;44m',
     '\033[0;97;45m',
     '\033[0;97;46m',
     '\033[0;97;47m',
     '\033[7;97m',
     )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[8], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    print(c[cor], end='')
    tam = (len(msg)) + 4
    print('-' * tam)
    print(f' {msg}')
    print('-' * tam)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou Biblioteca >"))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÈ LOGO', 1)
