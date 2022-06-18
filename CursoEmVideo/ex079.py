lista = []
while True:
    valor = (int(input('Digite um valor: ')))
    if valor in lista:
        print('Valor duplicado, não adicionado')
    if valor not in lista:
        lista.append(valor)
        print('Adicionado com sucesso ')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if continuar in 'N':
        break
print(sorted(lista))
