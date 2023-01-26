"""
Uma closure pode ser um decorador se:
-> A função externa receber uma função
-> A função recebida é uma variavel livre
-> retorna a função externa
"""
from time import sleep
from functools import wraps


def decorador(func):
    def interna(*args: any):
        resultado = func(*args)
        return f'Sou uma closure e sua função retornou {resultado}'
    return interna


@decorador
def soma(x: int, y: int):
    return x + y


@decorador
def invert(text: str):
    return text[::-1]

#decorada = decorador(soma)


#print(decorada(10, 10))
print(soma(10, 10))
print(invert('matheus'))


# caso o decorador precisar de um parametro
def cuida_do_parametro(param=None):
    def decorador(func):
        @wraps(func)  # devolver o nome original do name space
        def closure(*args, **kwargs):
            # antiga aninnhada
            print(param)
            print(func.__name__)
            return func(*args, **kwargs)
        return closure
    return decorador


@cuida_do_parametro()
def soma_x(x, y):
    return x + y


print(soma_x(1, 3))
print('-' * 40)


def retry(error: type, vezes, tempo):
    count = 0

    def intermediaria(func):
        def closure(*args, **kwargs):
            nonlocal count
            try:
                return func(*args, **kwargs)
            except error:
                count += 1
                print(f'{func.__name__} error: {error} retry: {count}')
                if count < vezes:
                    sleep(tempo)
                    return closure(*args, **kwargs)
        return closure
    return intermediaria


@retry(ZeroDivisionError, 5, 3)
def div(x, y):
    return x / y


div(3, 0)
