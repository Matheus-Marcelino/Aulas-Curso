from os import path, mkdir
from colorama import init
#from tdeE3Mol import ArquivoINTL
init()
# ArquivoINTL()


def cadastrar() -> None:
    if not path.exists('banco-de-dados'):
        mkdir('banco-de-dados')
    while True:
        nome = str(input('\nDigite o nome a ser cadrastado: ')).title().strip()
        certificando = str(
            input(f'Esse nome "{nome}" está correto? [S/N]:')).lower().strip()
        if 's' in certificando:
            break

        if 'n' in certificando:
            continue
        else:
            print('\033[1;33mNão entendi oque você quis dizer\033[m')

    while True:
        try:
            idade = int(input(f'\nDigite a idade do(a) {nome}: '))
            break
        except (ValueError, TypeError):
            print('\033[1;31mPOrfavor, apenas números inteiro!\033[m')

    with open('banco-de-dados/cadastro.txt', 'a+') as file:
        file.write(f'{nome}    {idade} Anos\n')


def mostrar_cadastro() -> None:
    with open('banco-de-dados/cadastro.txt', 'r') as file:
        print(file.readlines())


mostrar_cadastro()
