alunos = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if cont in 'N':
        break
print('-'*50)
print(f'{"No":<5}{"NOME":<10}{"MÉDIA":<25}')
print('-'*50)
for i, a in enumerate(alunos):
    print(f'{i:<5}{a[0]:<10}{a[2]:<25.2f}')
print('-'*50)
while True:
    notas = int(input('Mostrar notas de qual aluno? (999 Interrompe) '))
    if notas == 999:
        print('FINALIZADO')
        break
    if notas <= len(alunos)-1:
        print(f'Notas de {alunos[notas][0]} são: {alunos[notas][1]} ')
