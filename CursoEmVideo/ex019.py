from ramdom import choice
aluno01 = input('Digite o nome do 1° aluno: ')
aluno02 = input('Digite o nome do 2° aluno: ')
aluno03 = input('Digite o nome do 3° aluno: ')
aluno04 = input('Digite o nome do 4° aluno: ')
lista = [aluno01, aluno02, aluno03, aluno04]
escolhido = choice(lista)
print('O escolhido do sorteio é {}'.format(escolhido))