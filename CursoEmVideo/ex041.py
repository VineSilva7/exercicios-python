from datetime import date
anonascimento = int(input('Ano de nascimento: '))
anoatual = date.today().year
idade = (anoatual - anonascimento)
print('Voce tem {} anos'.format(idade))
if idade <= 9:
    print('Categoria: MIRIM')
elif 9 < idade <= 14:
    print('categoria: INFANTIL')
elif 14 < idade <= 19:
    print('Categoria: JUNIOR')
elif 19 < idade <= 25:
    print('Categoria: SENIOR')
elif 25 < idade:
    print('Categoria: MASTER')
