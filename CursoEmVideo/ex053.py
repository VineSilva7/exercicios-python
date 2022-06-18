f = str(input('Escreva uma frase: ')).strip().upper()
frase = f.replace(' ', '')
inverso = ''
for letra in range(len(frase) - 1, -1, -1):
    inverso += frase[letra]
print('O contrário de {} é {}'.format(frase, inverso))
if frase == inverso:
    print('É um Palindromo')
else:
    print('Não é um Palindromo')
