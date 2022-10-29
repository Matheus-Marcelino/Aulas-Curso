from os import path, system

def estilo(palavra: str, tamanho: int) -> None:
    print('-' * tamanho)
    print(f'{palavra}'.center(tamanho))
    print('-' * tamanho)


def leiaInt(informacao: str) -> int:
    print('-' * 40)
    while True:
        try:
            numero = int(input(informacao))
            break
        except (ValueError, TypeError):
            print('Um erro de digitação ocorreu! tente denovo!\n')
    print('-' * 40)
    return numero


def clear() -> None:
    system('cls')


def ArquivoINTL() -> None:
    from shutil import rmtree

    if path.exists('__pycache__'):
        rmtree('__pycache__')


ArquivoINTL()
