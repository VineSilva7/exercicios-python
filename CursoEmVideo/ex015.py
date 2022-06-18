dias = int(input('Dias alugados: '))
kmpercorrido = float(input('Km percorridos: '))
calculodias = dias * 60
calculokmpercorrido = kmpercorrido * 0.15
calculototal = calculodias + calculokmpercorrido
print('O total a pagar é de R${:.2f}'.format(calculototal))