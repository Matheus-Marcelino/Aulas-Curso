def escrever(texto: str):
    tamanho = len(texto) + 4

    print('~' * tamanho)
    print(f'  {texto}')
    print('~' * tamanho)


TEXTO = str(input('Digite um texto: '))

escrever(TEXTO)
