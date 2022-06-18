peso = float(input('Qual é o seu PESO? (Kg)? '))
altura = float(input('Qual é a sua ALTURA? (m)? '))
imc = peso / (altura ** 2)
print('O seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Status: ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('Status: PESO IDEAL')
elif 25 <= imc < 30:
    print('Status: SOBREPESO')
elif 30 <= imc < 35:
    print('Status: OBESIDADE GRAU I')
elif 35 <= imc < 40:
    print('Status: OBESIDADE GRAU Ii')
else:
    print('OBESIDADE MÓRBIDA')