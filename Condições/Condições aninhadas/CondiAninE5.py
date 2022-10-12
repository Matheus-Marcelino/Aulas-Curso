idade = int(input('Digite a sua idade: '))

if idade <= 9:
    print('O nadador é MIRIM')
elif idade <= 14:
    print('O nadador é INFANTIL')
elif idade <= 19:
    print('O nadador é JÚNIOR')
elif idade <= 25:
    print('O nadador é SÊNIOR')
else:
    print('O nadador é MASTER')
