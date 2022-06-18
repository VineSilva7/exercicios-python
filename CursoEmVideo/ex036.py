valor = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o sálario do comprador? R$'))
anos = float(input('Em quanto tempo(anos) vai ser pago? '))
mes = anos * 12
prestacao = valor / mes
if prestacao <= (salario * 30 / 100):
    print('Como a prestação não passou de 30% do seu salario então o emprestimo foi aprovado')
    print('A prestação ficou com um valor de R${:.2f}'. format(prestacao))
    print('e será paga em {} meses'.format(mes))
else:
    print('Como o valor da prestação ficou em R${:.2f}, sendo maior que 30% so sálario então seu emprestimo não foi aprovado'.format(prestacao))
