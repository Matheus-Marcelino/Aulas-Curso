"""
Closures -> Funções que encapsulam funções e as retornam
"""
from unicodedata import normalize


def normaliza(*palavras):
    def ajudante(palavra):
        normalizado = normalize('NFKD', palavra)
        return normalizado.encode('ASCII', 'ignore').decode('ASCII')

    return [ajudante(palavra) for palavra in palavras]


print(normaliza('Érico', 'Sabiá', 'João'))

print('-' * 40)


def soma_x(val_interno):  # criando um partial
    def interna(val_externo):
        return val_externo + val_interno

    return interna


soma_1 = soma_x(1)
soma_10 = soma_x(10)

print(soma_1(10))  # 11
print(soma_10(1))  # 11

# escopo global
def contador(start: int = 0):
    # limbo 
    count = start  # variavel livre

    def interna():
        # escopo local
        nonlocal count
        count += 1
        return count
    return interna


c = contador()
print(c())  # 1
print(c())  # 2