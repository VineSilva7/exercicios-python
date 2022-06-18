lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
print('-'*35)
print(f'Voce digitou {len(lista)} valores')
lista.sort(reverse=True)
print(f'A lista em forma descrescente é: {lista}')
if 5 in lista:
    print('O valor 5 FOI adicionado na lista')
else:
    print('O valor 5 NÂO foi adiconado na lista')
