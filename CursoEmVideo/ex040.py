n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('Sua média ficou em {:.2f}, portanto REPROVADO'.format(media))
elif 5 <= media <= 6.9:
    print('Sua média ficou em {:.2f}, portanto esta em RECUPERAÇÂO'.format(media))
elif media >= 7:
    print('Sua média ficou em {:.2f}, portanto APROVADO!'.format(media))
