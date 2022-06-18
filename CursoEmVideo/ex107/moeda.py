def dobro(preco):
    d = preco * 2
    return d


def metade(preco):
    m = preco / 2
    return m


def aumentar(preco, taxa):
    a = preco + (preco * (taxa / 100))
    return a


def dimunuir(preco, taxa):
    dim = preco - (preco * (taxa / 100))
    return dim
