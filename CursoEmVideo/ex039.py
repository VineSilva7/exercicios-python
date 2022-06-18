from datetime import date
anonasc = int(input('Qual é o ano do seu nascimento? '))
anoatual = date.today().year
idade = (anoatual - anonasc)
if idade < 18:
    print('Voce ainda deve se alistar ao serviço militar')
    print('faltam {} anos'.format(18-idade))
    print('E seu alistamento será em {}'.format(anonasc+18))
elif idade == 18:
    print('Esta na hora de você se alistar ao serviço militar')
elif idade >18:
    print('Já passou o tempo de alistamento')
    print('Você deveria ter se alistado a {} anos'.format(idade-18))
    print('E seu alistamento seria em {}'.format(anonasc + 18))