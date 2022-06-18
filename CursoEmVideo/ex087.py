par = coluna = linha = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor para [{l}] [{c}]: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if c == 2:
             coluna += matriz[l][c]
        if l == 1:
            if c == 0:
                linha = matriz[l][c]
            if matriz[l][c] > linha:
                linha = matriz[l][c]
print('-'*50)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-'*50)
print(f'A soma de todos os valores pares digitados é: {par}')
print(f'A soma dos valores da terceira coluna é: {coluna}')
print(f'O maior valor da segunda linha é: {linha}')
