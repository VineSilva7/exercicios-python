print('-'*30)
print('SEQUÊNCIA DE FIBONACCI')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
f1 = 0
f2 = 1
c = 0
print(f1, end=' ')
while c < n-1:
    f = f2 + f1
    print(f, end=' ')
    c = c + 1
    f2 = f1
    f1 = f
