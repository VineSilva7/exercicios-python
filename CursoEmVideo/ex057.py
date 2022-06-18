sexo = str(input('Qual é o seu sexo? [F/M] ')).strip().upper()[0]
while sexo not in 'FM':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo? [F/M] ')).strip().upper()[0]
print('Dados registrados, seu sexo é {}'.format(sexo))
