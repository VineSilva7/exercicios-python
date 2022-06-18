sa = float(input('Salario atual do funcionário: R$'))
ns = sa + (sa * 15 / 100)
print('O salário atual de R${:.2f}, fica R${:.2f} com 15% de desconto'.format(sa, ns))