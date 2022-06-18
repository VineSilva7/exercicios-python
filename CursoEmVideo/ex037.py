numero = int(input('Digite um número inteiro: '))
binario = (bin(numero)[2:])
octal = (oct(numero)[2:])
hexa = (hex(numero)[2:])
print('[1] - BINÁRIO')
print('[2] - OCTAL')
print('[3] - HEXADECIMAL')
escolha = int(input('Digite a opção para converter: '))
if escolha == 1:
    print(binario)
elif escolha == 2:
    print(octal)
elif escolha == 3:
    print(hexa)
else:
    print('Opção inexistente')
