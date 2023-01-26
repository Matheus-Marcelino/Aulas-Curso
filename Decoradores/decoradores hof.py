"""
Estender ou restringir funcionalidades de uma função

Decoradores são um açúcar sintático para o funcionamento de closures especificas

Closures -> são um caso especial de aninhamento de funções de ordem superios, que armazenam varaiáveis livres

Funções aninhadas -> são funções definidas dentro de funções
Funções de ordem superior -> Quer dizer que função podem receber ou retornar funções de primeira classe
Variáveis livres -> Variáveis que não pertencem ao escopo global ou local

hof -> São só as funções que recebem ou retornam uma função, 
mas todas as funções são objetos de primeira classe
"""

from time import sleep
from functools import cache
from medidor_de_tempo import medidor_de_tempo


@medidor_de_tempo
@cache
def delay(sec):
    sleep(sec)
    return sec


print(delay(2), delay(2), delay(2))

print('-' * 40)

from functools import reduce  # adiciona


def soma(x, y):
    return x + y


resultado = reduce(soma, [1, 2, 3, 4, 5])

print(resultado)

print('-' * 40)


def maior_que_5(valor):
    return valor > 5


resultado = filter(maior_que_5, [3, 4, 5, 6, 7])

print(list(resultado))

print('-' * 40)

from functools import partial  # fica um valor

soma_1 = partial(soma, y=1) #podendo escolher até os parametros
soma_10 = partial(soma, 10)

print('-' * 40)


def zip_with(func, iter_a, iter_b):
    return list(map(func, iter_a, iter_b))


print(zip_with(soma, [1, 2, 3], [1, 2, 3]))  # ele soma cada elemento com o seu correspondente -> elemento 1 mais 1
