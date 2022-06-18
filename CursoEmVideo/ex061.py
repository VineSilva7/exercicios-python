print(f'{" 10 TERMOS DE UMA PA ":^40}')
print('-'*40)
primeiro = int(input('PRIMEIRO TERMO: '))
razao = int(input('RAZÂO: '))
termo = primeiro
contador = 1
while contador <= 10:
    print(termo, end=' ')
    termo += razao
    contador += 1
