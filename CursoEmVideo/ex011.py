a = float(input('Altura da parede em metros: '))
l = float(input('Largura da parede em metros: '))
m2 = a*l
t = (a*l)/2
print('A parede tem {:.2f}m² e e necessita de {:.2f} litros de tinta para pinta-la'.format(m2, t))