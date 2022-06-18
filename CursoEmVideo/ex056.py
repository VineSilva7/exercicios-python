totmediaidade = 0
totmulheres = 0
idadehomemvelho = 0
nomehomem = ''
for p in range(1, 5):
    print(f'{" {} PESSOA ":-^40}'.format(p))
    nome = str(input('Nome da {} pessoa: '.format(p))).strip().upper()
    idade = int(input('Idade da {} pessoa: '.format(p)))
    sexo = int(input('Tecle: [0]-Feminino ou [1]-Masculino: '))
    totmediaidade += idade
    if sexo == 0 and idade < 20:
        totmulheres += 1
    if sexo == 1 and p == 1:
        idadehomemvelho = idade
        nomehomem = nome
    if sexo == 1 and idade > idadehomemvelho:
        idadehomemvelho = idade
        nomehomem = nome
print('-'*40)
print('A média de idade do grupo é: {:.1f} anos'.format(totmediaidade/p))
print('A idade do homem mais velho é {} e seu nome é {}'.format(idadehomemvelho, nomehomem))
print('tem {} mulheres menores de 20 anos'.format(totmulheres))
