print(f'{" 10 TERMOS DE UMA PA ":^40}')
print('-'*40)
primeiro = int(input('PRIMEIRO TERMO: '))
razao = int(input('RAZÂO: '))
decimo = primeiro + (10) * razao
for c in range(primeiro, decimo, razao):
    print(c, end=' ')