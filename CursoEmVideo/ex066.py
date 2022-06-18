c = p = 0
while True:
    n = int(input('Digite um numero [PARAR:999]:  '))
    if n == 999:
        break
    c += 1
    p += n
print(f'Foram digitados {c} e a soma é {p}')
