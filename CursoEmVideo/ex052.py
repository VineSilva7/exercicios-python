numero = int(input('Digite um número: '))
tot = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[0;32m', end=' ')
        tot += 1
    else:
        print('\033[0;31m', end=' ')
    print(c, end=" ")
print('\n\033[mO numero {} foi divisivel {} vezes'.format(numero, tot))
if tot == 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÂO É PRIMO')
