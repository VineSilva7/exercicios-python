from datetime import date
ano = int(input('Digite um ano ou colque 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print('O {} é um ano BISSEXTO!'.format(ano))
else:
    print('O {} NÂO é um ano BISSEXTO!'.format(ano))