print(f'{" 10 TERMOS DE UMA PA ":^40}')
print('-'*40)
primeiro = int(input('PRIMEIRO TERMO: '))
razao = int(input('RAZÂO: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print(termo, end=' ')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
