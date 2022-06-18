print('SOMA DE NÚMEROS')
print('CONDIÇAÕ DE PARADA DIGITE 999')
print('-'*30)
n = 0
contador = 0
soma = 0
n = int(input('Digite um valor:  '))
while n != 999:
    contador += 1
    soma = soma + n
    n = int(input('Digite um valor:  '))
print('Foi digitado {} números e a soma foi {}'.format(contador, soma))
