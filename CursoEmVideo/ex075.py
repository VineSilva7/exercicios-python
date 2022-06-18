lista = (int(input('Primeiro Número: ')), int(input('Segundo Número: ')),
         int(input('Terceiro Número: ')), int(input('Quarto Número: ')))
print(f'Foi digitado os seguintes números: {lista}')
print(f'O valor 9 apareceu {lista.count(9)} vezes')
if 3 in lista:
    print(f'O valor 3 esta na {lista.index(3)+1}ª posição')
else:
    print(f'O valor 3 não apareceu na lista')
print(f'Foram digitados os seguintes números pares:', end=' ')
for numero in lista:
    if numero % 2 == 0:
        print(numero, end=" ")
