from time import sleep
n1 = int(input('Digite o Primeiro numero: '))
n2 = int(input('Digite o Segundo numero: '))
r = 0
while r != 5:
    print('[1] SOMAR ')
    print('[2] MULTIPLICAR ')
    print('[3] MAIOR ')
    print('[4] NOVOS NUMEROS ')
    print('[5] SAIR DO PROGRAMA ')
    r = int(input('Escolha uma opção: '))
    if r == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif r == 2:
        multiplicar = n1 * n2
        print('A multiplicação entre {} x {} é {}'.format(n1, n2, multiplicar))
    elif r == 3:
        if n1 > n2:
            print('O valor {} que é o primeiro número é maior!'.format(n1))
        elif n1 <n2:
            print('O valor {} que é o segundo número é maior!'.format(n2))
        elif n1 == n2:
            print('Os dois valores são iguais')
    elif r == 4:
        print('Tente novamente com outros números: ')
        n1 = int(input('Digite o Primeiro numero: '))
        n2 = int(input('Digite o Segundo numero: '))
    elif r == 5:
        print('Finalizando.....')
    else:
        print('Número inválido, Tente Novamente')
    print('-' * 40)
    sleep(2)
print('Você encerrou o programa')
print('Volte sempre')



c = 1
while c < 10:
    print(c)
    c += 1
print('FIm')
print('-'*40)
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')
print('-'*40)
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r= str(input('Quer continuar? [S/N} ')).upper()
print('FIM')