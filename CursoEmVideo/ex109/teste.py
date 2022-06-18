from ex109 import moeda
p = float(input('Digite um preço: R$'))
print(f'A metade de R${moeda.moeda(p)} é R${moeda.metade(p, True)}')
print(f'O dobro de R${moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'com aumento de 10% temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13% do preço temos {moeda.diminuir(p, 13, True)}')