def fatorial (n, show=False):
    """
    ==> Calcular o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor de um fatorial de um número n
    """
    s = 1
    cont = n
    if show == False:
        while cont > 0:
            s *= cont
            cont -= 1
        return s
    if show == True:
        while cont > 0:
            print('{}'.format(cont), end='')
            print(' x ' if cont > 1 else ' = ', end='')
            s *= cont
            cont -= 1
        return s


print(fatorial(5, show = True))
help(fatorial)