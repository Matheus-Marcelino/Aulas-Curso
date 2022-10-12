from colorama import init
init()

lista_NUM = []
maior = menor = 0

for cont in range(0, 5):
    lista_NUM.append(int(input(f'Digite um valor na posição {cont}: ')))
    if cont == 0:
        maior = menor = lista_NUM[0]
    else:
        if lista_NUM[cont] > maior:
            maior = lista_NUM[cont]
        if lista_NUM[cont] < menor:
            menor = lista_NUM[cont]

print(f'\nO maior valor digitado foi \033[1;32m{maior}\033[m na posição', end='')

for indice, valor in enumerate(lista_NUM):
    if valor == maior:
        print(f' {indice}...', end='')

print(f'\nO menor valor digitado foi \033[1;32m{menor}\033[m na posição', end='')

for indice, valor in enumerate(lista_NUM):
    if valor == menor:
        print(f' {indice}...', end='')
