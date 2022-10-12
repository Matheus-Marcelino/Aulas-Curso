n = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
cont = 1
# Progressão aritimetica
while cont != 10:
    print(f'{n}', end=' >> ')
    cont += 1
    n += razão
print('FIM')
