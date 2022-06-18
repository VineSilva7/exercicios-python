pa = float(input('Preço antigo do produto: R$'))
pn = pa - (pa * 5 / 100)
print('Preço antigo de R${:.2f} fica R${:.2f} com 5% de desconto'.format(pa, pn))