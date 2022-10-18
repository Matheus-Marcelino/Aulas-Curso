def contador(inicio, fim, pulos=1):
    if pulos == 0:
        pulos = 1

    print('-=' * 40)
    print(f'Contagem de {inicio} até {fim} pulando de {pulos} em {pulos}')
    for cont in range(inicio, fim - 1, pulos):
        if cont < 0:
            print(f'{cont}', end=' ')
        else:
            print(cont, end=' ')
    print('FIM')
    print('-=' * 40, '\n')


contador(1, 11, 1)
contador(12, -10)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('fim: '))
pulos = int(input('pulos: '))

contador(inicio, fim, pulos)
