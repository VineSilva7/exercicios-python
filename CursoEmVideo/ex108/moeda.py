def dobro(preco=0):
    d = preco * 2
    return d


def metade(preco=0):
    m = preco / 2
    return m


def aumentar(preco=0, taxa=1):
    a = preco + (preco * (taxa / 100))
    return a


def dimunuir(preco=0, taxa=1):
    dim = preco - (preco * (taxa / 100))
    return dim


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
