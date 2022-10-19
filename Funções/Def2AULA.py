"""
help() para obter ajuda das funções ou bibliotecas
  |
  --> help(input)

print(input.__doc__) __doc__ para mostrar a documentação de uma função
"""


def contador(i, f, p):
    """
    -> faz uma contagem na tela
    :param i: Inicio da contagem
    :param f: fim ada contagem
    :param p: passo do contador
    :return: função sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='')
        c += p
    print('FIM!')


# help(contador)
def teste():
    # global n1 -- ele usa o n1 global
    n1 = 4  # n1 local
    print(n1)


def teste2():
    # n1 -= 1 -- ele requer que n1 seja chamado no contexto global para alterar o valor
    print(n1)


n1 = 1  # n1 global
teste()
teste2()


def somar(a=0, b=0, c=0):  # function com variveis opcionais
    # s = a + b + c
    # return s
    return a + b + c


somar(5, 6, 0)
somar(4)

somar = somar(3, 6, 8)
print(somar)
# print(somar(6, 7, 1))  --  não pode ser utilizado quando se coloca a operação no return


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(6)
f2 = fatorial(18)
f3 = fatorial(5)
print(f'Os resultados são {f1}, {f2} e {f3}')


def par(n=1):
    if n % 2 == 0:
        return True
    return False


num = int(input('digite um numero: '))
print(f'O resultado é: {par(num)}')
