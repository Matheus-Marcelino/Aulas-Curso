from math import hypot

n = float(input('Cateto adjacente: '))
n1 = float(input('Cateto oposto: '))

print(f'A sua hipotenusa é {hypot(n1, n):.2f}')  # hypot hipotenusa
