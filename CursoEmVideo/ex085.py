num = [[], []]
for cont in range(1, 8):
    valor = int(input(f'Digite o {cont} valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-'*60)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados são: {num[0]}')
print(f'Os valores impares digitados são: {num[1]}')
