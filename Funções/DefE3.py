"""
Fazendo o exercicio de uma maneira mais inteligente
porque ele não especificou :)

from time import sleep


def contador(inicio, fim, pulos=1):
    if pulos == 0:
        pulos = 1
    
    print('-=' * 40)
    print(f'Contagem de {inicio} até {fim} pulando de {pulos} em {pulos}')
    for cont in range(inicio, fim - 1, pulos):
        if cont < 0:
            print(f'{cont}', end='', flush=True)
            sleep(0.5)
        else:
            print(f'{cont}', end='', flush=True)
            sleep(0.5)
    print('FIM')
    print('\n')


contador(1, 11, 1)
contador(12, -10)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('fim: '))
pulos = int(input('pulos: '))

contador(inicio, fim, pulos)
"""

# exercicio como ele fez
from time import sleep


def contador(i, f, p):
    print('-=' * 20)
    
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} pulando de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM')


contador(1, 11, 1)
contador(12, -10)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('fim: '))
pulos = int(input('pulos: '))
contador(inicio, fim, pulos)