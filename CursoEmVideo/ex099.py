from time import sleep


def maior(* num):
    mai = cont = 0
    print('-' * 50)
    print('Analisando os valores passados...')
    for c in num:
        print(f'{c} ', end='')
        sleep(0.5)
        if cont == 0:
            mai = c
        else:
            if c > mai:
                mai = c
        cont += 1
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi: {mai}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
