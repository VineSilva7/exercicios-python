print('Cadastro de Pessoas')
maior = homem = mjovem = 0
while True:
    print('-'*30)
    idade = int(input('Qual é a idade? '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Qual é o sexo? [M/F] ')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mjovem += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Querm continuar [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-'*30)
print(f'Tem {maior} pessoas maiores de 18')
print(f'Tem {homem} homens')
print(f'E Tem {mjovem} mulheres com menos de 20 anos')



