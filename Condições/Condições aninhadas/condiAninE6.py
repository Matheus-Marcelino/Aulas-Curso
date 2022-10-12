r = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))

if r < r2 + r3 and r2 < r3 + r and r3 < r + r2:
    print('Os seguimento acima podem fazer um triangulo')
    if r == r2 ==r3:
        print('EQUILÁTERO')
    elif r != r2 != r3 != r :
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os seguimentos acima não podem fazer um triangulo')
