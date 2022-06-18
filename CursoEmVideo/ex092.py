from datetime import datetime
pessoa = {}
while True:
    pessoa['nome'] = str(input('Nome: '))
    nascimento = int(input('Ano de Nascimento: '))
    pessoa['idade'] = (datetime.now().year - nascimento)
    ctps = int(input('Carteira de trabalho (0 não tem): '))
    if ctps == 0:
        pessoa['ctps'] = ctps
        break
    else:
        pessoa['ctps'] = ctps
        pessoa['contratação'] = int(input('Ano de contratação: '))
        pessoa['salário'] = float(input('Salário: R$'))
        pessoa['aposentadoria'] = ((pessoa['contratação'] + 35) - nascimento)
        break
print('-'*30)
for k, v in pessoa.items():
    print(f' - {k} tem o valor {v}')
