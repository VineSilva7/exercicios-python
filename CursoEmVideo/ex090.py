aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] < 5:
    aluno['resultado'] = 'Reprovado'
elif 5 <= aluno['media'] < 7:
    aluno['resultado'] = 'Recuperação'
if aluno['media'] >= 7:
    aluno['resultado'] = 'Aprovado'
print('-'*40)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')
