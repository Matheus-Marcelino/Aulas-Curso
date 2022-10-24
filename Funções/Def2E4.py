from colorama import init
init()


def leiaInt(informacao=...) -> int:
    numero = input(informacao)
    while numero.isnumeric() is False:
        print('\033[1;31mERRO! Digite um número inteiro válido\033[m')
        numero = input(informacao)
    return numero


a = leiaInt('Digite: ')
print(f'Você acabou de digitar o número {a}')
