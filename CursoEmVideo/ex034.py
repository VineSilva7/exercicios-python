salario = float(input('Salário antigo: R$'))
if salario > 1250:
    aumento = salario + (salario * 10 / 100)
    print('Com o aumento seu salário ficará R${:.2f}'.format(aumento))
else:
    aumento = salario + (salario * 15 /100)
    print('Com o auemnto seu salário ficará R${:.2f}'.format(aumento))