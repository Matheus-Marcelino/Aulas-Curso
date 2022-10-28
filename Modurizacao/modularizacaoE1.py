from moedaE1 import moeda

preco = float(input('Digite o preço: R$'))

print(f'O seu valor de {preco:.2f} dobrado fica: {moeda.dobro(preco):.2f}R$')
print(f'O seu valor de {preco:.2f} pela metade fica: {moeda.metade(preco):.2f}R$')
print(f'O seu valor de {preco:.2f} aumentado em 10% fica: {moeda.aumentar(preco, 10):.2f}R$')
print(f'O seu valor de {preco:.2f} diminuido em 15% fica: {moeda.diminuir(preco, 15):.2f}R$')
