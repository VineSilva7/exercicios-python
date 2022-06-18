lista = []
maior = menor = 0
for cont in range(0, 5):
    lista.append(int(input(f'Digite um valor da posição {cont}: ')))
    if cont == 0:
        maior = menor = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        if lista[cont] < menor:
            menor = lista[cont]

print('-'*30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} na posição ', end='')
for posicao, valor in enumerate(lista):
    if valor == max(lista):
        print(f'{posicao}... ', end='')
print(f'\nO menor valor digitado foi {menor} na posicao ', end='')
for posicao, valor in enumerate(lista):
    if valor == min(lista):
        print(f'{posicao}... ', end='')
