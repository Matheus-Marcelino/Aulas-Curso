medida = float(input('Uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000

print('A medida de {:.2f}m corresponde a {:.2f}cm e {:.2f}mm'.format(medida, cm, mm))
print('=' * 20)
print('Tabuada')
print('')


n = int(input('Digite um numero para Tabuada ser feita: '))
n1 = 0
quant = int(input('tamanho da tabuada: '))
quant2 = range(0, quant + 1)

for c in quant2:
    print(f'{n1} x {n} = {n1 * n}')
    n1 += 1

# forma antiga
"""print('Tabuada do {}\n1 x {:2} = {}\n2 x {:2} = {}\n3 x {:2} = {}\n4 x {:2} = {}\n5 x {:2} = {}\n6 x {:2} = {}'
      '\n7 x {:2} = {}\n8 x {:2} = {}\n9 x {:2} = {}\n10 x {} = {}'.format(n, n, 1 * n, n, 2 * n, n, 3 * n, n, 4 * n, n,
                                                                        5 * n, n, 6 * n, n, 7 * n, n, 8 * n, n, 9 * n,
                                                                           n, 10 * n))"""

print('=' * 20)
print('Porcentagem')
print('')

preço = float(input('qual é o preço do produto?\nR$'))
desconto = float(input('qual é o desconto do produto?\n%'))

print('O preço do produto ficará em:R${:.2f}'.format(preço * desconto / 100))
