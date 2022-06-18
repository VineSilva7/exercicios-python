print('{:=^40}'.format(' LOJA DO VINICIUS '))
valor = float(input('Valor a ser pago: R$'))
print('[1] À VISTA dinheiro ou cheque')
print('[2] À VISTA no cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
pagamento = int(input('Fomma de pagamento escolhida: '))
if pagamento == 1:
    valornovo = valor - (valor * 10 / 100)
    print('O valor ficará: R${:.2f}'.format(valornovo))
elif pagamento == 2:
    valornovo = valor - (valor * 5 / 100)
    print('O valor ficará: R${:.2f}'.format(valornovo))
elif pagamento == 3:
    parcela = valor / 2
    print('O valor ficará: R${:.2f}'.format(valor))
    print('Com 2x de R${:.2f} SEM JUROS'.format(parcela))
elif pagamento == 4:
    valornovo = valor + (valor * 20 / 100)
    totalparcelas = int(input('Quantas parcelas? '))
    parcelas = valornovo / totalparcelas
    print('O valor ficará: R${:.2f}'.format(valornovo))
    print('Com {}x de R${:.2f} COM JUROS'.format(totalparcelas, parcelas))
else:
    print('Opção inexistente, tente novamente!')

