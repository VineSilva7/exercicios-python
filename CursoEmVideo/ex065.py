maior = menor = 0
r = 'S'
soma = contador = 0
while r == 'S':
    n = int(input('Digite um numero: '))
    soma = soma + n
    contador = contador + 1
    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Quer Continuar?[S/N]')).strip().upper()[0]
media = soma / contador
print('Foi digitado {} números e a média foi {}'.format(contador, media))
print('O maior número foi {}'.format(maior))
print('O menor número foi {}'.format(menor))
