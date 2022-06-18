from random import randint
c = menor = maior = 0
print(f'Os valores sorteados foram:', end=' ')
for c in range (0, 5):
    lista = randint(0, 10)
    c += 1
    print(lista, end=' ')
    if c == 1:
        menor = maior = lista
    else:
        if lista > maior:
            maior = lista
        if lista < menor:
            menor = lista
print(f'\nMaior número: {maior}')
print(f'Menor número: {menor}')

print("-"*40)

numeros = (randint(0, 10), randint(0, 10), randint(0, 10),
          randint(0, 10), randint(0, 10), )
print(f'Os valores sorteados foram:', end=' ')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nMaior número: {max(numeros)}')
print(f'Menor número: {min(numeros)}')
