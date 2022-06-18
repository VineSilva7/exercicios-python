print('Tabuada (Negativo para parar)')
c = 0
while True:
    print('-'*40)
    n = int(input('Digite um número para ver a tabuada: '))
    if n >= 0:
        for c in range(0, 11,):
            print(f'{c} X {n} = {c*n}')
    else:
        break
print('-'*40)
print('Tabuada Finalizada')
