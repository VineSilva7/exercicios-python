def leiadinheiro(msg):
    validade = False
    while not validade:
        num = str(input(msg)).replace(',', '.').strip()
        if num.isalpha() or num == '':
            print(f'\033[0;31mERRO! "{num}" É UM PREÇO INVALIDO.\033[m')
        else:
            validade = True
            return float(num)
