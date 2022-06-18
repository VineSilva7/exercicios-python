from time import sleep


def contador(inicio, fim, passo):
    print('-' * 40)
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'A contagem de {inicio} até o {fim} de {passo} em {passo}: ')
    if fim > inicio:
        for c in range(inicio, fim+1, passo):
            print(f'{c} ', end='')
            sleep(0.5)
    else:
        for c in range(inicio, fim-1, -passo):
            print(f'{c} ', end='')
            sleep(0.5)
    print('fim')
    print('-' * 40)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem')
ini = int(input('Inicio: '))
fi = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fi, pas)
