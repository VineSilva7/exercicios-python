lista = []
for contador in range(0,5):
    valor = (int(input('Digite um valor: ')))
    if contador == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Valor adicionado no final da lista')
    else:
        posicao = 0
        while posicao < len(lista):
            if valor <= lista[posicao]:
                lista.insert(posicao, valor)
                print(f'Adcionado na posição {posicao} da lista')
                break
            posicao += 1
print('-'*30)
print(f'Os valores digitados em ordem foram {lista}')
