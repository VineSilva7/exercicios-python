distancia = float(input('Qual é a distância da viagem em Km: '))
if distancia <= 200:
    valor01 = distancia * 0.50
    print('o valor da passagem é de R${:.2f}'.format(valor01))
else:
    valor02 = distancia * 0.45
    print('O valor da passagem é de R${:.2f}'.format(valor02))
