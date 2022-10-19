from random import randint


def sortear():
    lista = [randint(1, 9), randint(1, 9), randint(
        1, 9), randint(1, 9), randint(1, 9)]
    print(f'Sorteando {len(lista)} valores da lista:', end=' ')
    for c in lista:
        print(c, end=' ')
    print('PRONTO !')
    return lista


def somar_pares(lista):
    soma = 0

    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f'Somando os valores pares de {lista}, temos: {soma}')


lista = sortear()
somar_pares(lista)
