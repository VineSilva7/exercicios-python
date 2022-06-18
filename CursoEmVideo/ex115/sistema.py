from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cadastropessoas.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sitema'])
    if resposta == 1:
        #opção de listar o conteudo do arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #opção de cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Até Logo!')
        break
    else:
        print('\033[31mERRO: por favor, digite um número inteiro válido\033[m')
    sleep(2)

