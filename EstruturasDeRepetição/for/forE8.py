num = int(input('Primeiro termo: '))
razão = int(input('Razão: '))

for c in range(num, num + (10 -1) * razão, razão):  # progressão aritimética
    print(c, end = ' > ')
print('Acabou')
