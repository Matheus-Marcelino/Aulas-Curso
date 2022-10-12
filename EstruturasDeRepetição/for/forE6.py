n = int(input('Digite um numero para Tabuada ser feita: '))
quant = int(input('tamanho da tabuada: '))

for c in range(0, quant + 1):
    print(f'{n} x {c} = {c * n}')
