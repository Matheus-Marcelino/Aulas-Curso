quant = int(input('Quantos termos você quer mostrar?: '))
n = 0
n2 = 1
cont = 3

print('0 >> ', end='')  # fibonacci
while cont != quant:
    N3 = n + n2
    print(f'{N3} >> ', end='')
    n2 = n
    n = N3
    cont += 1
print('fim')
