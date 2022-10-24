from colorama import init
init()


def leiaInt(informacao: str) -> int:
    numero = input(informacao)
    while numero.isnumeric() is False:
        print('\033[1;31mERRO! Digite um número inteiro válido\033[m')
        numero = input(informacao)
    return numero


a = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {a}')
