soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print('Voce informou {} numeros pares e a sua soma foi {}'.format(cont, soma))
