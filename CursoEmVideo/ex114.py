import urllib
import urllib.request
site=str(input('Insira o site: '))
try:
    site1 = urllib.request.urlopen(f'http://www.{site}')
except urllib.request.URLError:
    print('O Site não está acessível no momento')
else:
    print('Consegui abrir o site com sucesso!')


'''import urllib
import urllib.request)
try:
    site = urllib.request.urlopen(f'http://www.pudim.com.br')
except urllib.error.URLError:
    print('O Site não está acessível no momento')
else:
    print('Consegui abrir o site com sucesso!')'''