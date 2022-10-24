from time import sleep


def Fatorial(numero, show=False):
    numero
    fat = cont = 1
    while cont <= numero:
        if show:
            sleep(0.5)
            print(cont, flush=show, end=' > ')
        fat = fat*cont
        cont += 1

    print(f'O valor de {numero}! eh = ' + str(fat))

print('-' * 40)
Fatorial(5)
