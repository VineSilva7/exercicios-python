print('Cadastro de Produtos')
gasto = caro = menor = cont = 0
barato = ''
while True:
    print('-'*30)
    produto = str(input('Nome do Produto: ')).strip()
    valor = float(input('Valor do Produto: R$'))
    cont += 1
    gasto += valor
    if valor > 1000:
        caro += 1
    if cont == 1 or valor < menor:
        menor = valor
        barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-'*30)
print(f'Foi gasto R${gasto:.2f}')
print(f'Produtos que custam mais que R$1000.00: {caro}')
print(f'Produto que custa mais barato: {barato} com o valor {menor:.2f}')
