dados = list()
pessoas = list()
totpess = maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    totpess += 1
    if totpess == 1:
        maior = menor = pessoas[0][1]
    else:
        for p in pessoas:
            if p[1] > maior:
                maior = p[1]
            if p[1] < menor:
                menor = p[1]
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if cont in 'N':
        break
print('-'*40)
print(f'Foram cadastradas {totpess} pessoas')
print(f'O maior peso foi {maior}. Peso de: ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}, ', end='')
print(f'\nO menor peso foi {menor}. Peso de: ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}, ', end='')
