velocidade = float(input('Velovidade do Veículo em Km/h: '))
if velocidade > 80:
    print('Voce foi Multado, você estava a {} Km/h'.format(velocidade))
    valor = (velocidade-80)*7
    print('E o valor da sua multa é de R${:.2f}'.format(valor))
else:
    print('Você esta abaixo do limíte de velocidade, continue assim!!')