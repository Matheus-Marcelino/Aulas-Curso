from os import path, mkdir
from colorama import init
from tdeE3Mol import ArquivoINTL
init()
ArquivoINTL()


def cadastrar() -> None:
    if not path.exists('banco-de-dados'):
        mkdir('banco-de-dados')
    while True:
        nome = str(input('\nDigite o nome a ser cadastrado: ')).title().strip()
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

    nome = nome.replace(' ', '_')

    with open('banco-de-dados/cadastro.txt', 'a+') as file:
        file.write(f'{nome}    {idade}\n')


def mostrar_cadastro() -> list:
    """
    lista_user: pega todos os dados organizados
    datas: recolhe todos os cadatros no arquivo
    return: retorna a lista organizada
    """
    with open('banco-de-dados/cadastro.txt', 'r') as file:
        lista_temp, lista_user = [], []
        datas = file.readlines()
        for data in datas:
            lista_temp.append(data[:-1])
        for c in range(len(lista_temp)):
            lista_user.append(lista_temp[c].split())
        return lista_user
