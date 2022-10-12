from colorama import init
init()

num = int(input('verificar o número: '))  # verificando números inteiro
tot = 0

for c in range(1, num + 1):
    if num % c == 0:  # verificando se o 'num' é divisivel por apenas ele mesmo e o 1
        tot += 1
        print(f'\033[32m{c}\033[m', end=' > ')
    ''' else:
        print(f'\033[31m{c}\033[m', end=' > ')'''
print(f'o seu número {num} teve um total de {tot} divisores')
if tot == 2:
    print('O seu número é primo!')
else:
    print('O seu número não é primo')
