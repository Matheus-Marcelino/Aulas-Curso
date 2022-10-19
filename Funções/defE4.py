"""
maneira de como eu fiz o exercicio

def maior():
    print(f'O maior numero foi {max(numeros)}')
    print(f'O menor numero foi {min(numeros)}')


numeros = list()
quantidade = int(input('Quantos numeros deseja digitar? '))

for _ in range(quantidade):
    numeros.append(int(input('Digite um valor: '))) 

maior()
"""
from time import sleep


def maior(*num):
    print('-=' * 40)
    print('Analisando os valores passados...')
    for c in num:
        print(f'{c}', end=' ', flush=True)
        sleep(0.5)
    print(f'Foram informados {len(num)} valores no total')
    print(f'O maior valor foi {max(num)}')


maior(4, 5, 2, 1)
maior(4, 5, 5, 3, 40)
maior(1, 0, 5)
