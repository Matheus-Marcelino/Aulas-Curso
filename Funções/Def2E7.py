from colorama import init
init()


def InteractiveHelp(data) -> None:
    decorador(f'Acessando o manual do comando {data}', '30', '44')
    help(data)
    print('\033[m')


def decorador(txt: str, cor: str | int, fundo: str | int) -> None:
    tamanho = len(txt) + 4
    print(f'\033[1;{cor};{fundo}m')
    print('~' * tamanho)
    print(f'  {txt}')
    print('~' * tamanho)
    print('\033[m')


while True:
    decorador('SISTEMA DE AJUDA PyHELP', '37', '42')
    data = str(input('exit para sair\nFunção ou biblioteca > '))
    if data.lower() == 'exit':
        decorador('OBRIGADO POR USAR', '37', '41')
        break
    else:
        InteractiveHelp(data)
