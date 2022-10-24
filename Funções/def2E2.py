from time import sleep


def Fatorial(numero, show=False):
    numero
    fat = 1
    for cont in range(1, numero+1):
        if show:
            sleep(0.2)
            print(cont, flush=show, end=' > ')
        fat *= cont
        cont += 1

    print(f'O valor de {numero}! eh = ' + str(fat))

print('-' * 40)
Fatorial(5, True)
