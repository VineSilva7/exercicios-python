listaA = []
listaB = []
listaC = []
while True:
    valor = (int(input('Digite um valor: ')))
    if valor % 2 == 0:
        listaA.append(valor)
        listaB.append(valor)
    else:
        listaA.append(valor)
        listaC.append(valor)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
print('-'*50)
print(f'A lista A é: {listaA}')
print(f'A lista B que só contém pares é: {listaB}')
print(f'A lista C que só contém impares é: {listaC}')
print('-'*50)
lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-'*50)
print(f'A lista A é: {lista}')
print(f'A lista B que só contém pares é: {pares}')
print(f'A lista C que só contém impares é: {impares}')
