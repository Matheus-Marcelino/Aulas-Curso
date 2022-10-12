from colorama import init
init()

while True:
    n = int(input('Quer ver a tubuada de qual valor?: '))
    if n < 0:
        print('\033[1;32mObrigado por usar esse programa :D\033[m')
        break
    for c in range(1, 11):
        print(f'{n} X {c} = {n * c}')
