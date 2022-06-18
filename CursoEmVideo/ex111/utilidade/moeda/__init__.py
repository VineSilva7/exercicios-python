def dobro(preco=0, forma=False):
    res = preco * 2
    return res if forma is False else moeda(res)


def metade(preco=0, forma=False):
    res = preco / 2
    return res if forma is False else moeda(res)


def aumentar(preco=0, taxa=1, forma=False):
    res = preco + (preco * (taxa / 100))
    return res if forma is False else moeda(res)


def diminuir(preco=0, taxa=1, forma=False):
    res = preco - (preco * (taxa / 100))
    return res if forma is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, aumento=0, reducao=0):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'Preço analizado: \t{moeda(preco):}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preco,aumento, True)}')
    print(f'{reducao}% de redução: \t{diminuir(preco, reducao, True)}')
    print('-' * 30)
