pessoa = {}
cadastro = []
idade = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('ERRO! Responda apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    idade += pessoa['idade']
    cadastro.append(pessoa.copy())
    pessoa.clear()
    while True:
        cont = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if cont in 'SN':
            break
        else:
            print('ERRO! Responda apenas S ou N')
    if cont == 'N':
        break
print(cadastro)
print(f'A) Foram cadastrados {len(cadastro)} pessoas')
media = idade / len(cadastro)
print(f'B) A média de idade do grupo foi {media} anos')
print(f'C) As muleheres da lista foram:', end='')
for c in cadastro:
    if c['sexo'] == 'F':
        print(f' {c["nome"]}.', end='')
print('\nD) Lista de pessoas que estão acima da média de idade')
for c in cadastro:
    if c['idade'] >= media:
        print('   ', end='')
        for k, v in c.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<ENCERRADO>>')
