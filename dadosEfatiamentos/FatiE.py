from time import sleep

nome = str(input('Digite seu nome completo: ')).strip()

for c in range(1):
    print('analisando seu nome...')
    sleep(1.5)
    print(f'Seu nome em maisuculas: {nome.upper()}')
    sleep(1)
    print(f'Seu nome me minusculas: {nome.lower()}')
    sleep(1)
    print(f'Seu nome tem {len(nome) - nome.count(" ")} letras')  # o tamanho do nome menos os espaços contados
    sleep(1)
    """print(f'Seu primeiro nome tem: {nome.find(" ")}')
    # pesquisar o primeiro espaço para contar o primeiro nome"""
    print(f'Seu primeiro nome tem: {len(nome.split()[0])} letras')
