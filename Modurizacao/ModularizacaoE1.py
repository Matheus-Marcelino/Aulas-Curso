from moedaE1 import moeda

preco = float(input('Digite o preço R$'))

print(f'O seu preço dobrado fica: {moeda.dobro(preco)}')
print(f'O seu preco pela metade fica: {moeda.metade(preco)}')
print(f'O seu preço aumentado em 10% fica: {moeda.aumentar(preco)}')
print(f'O seu preço diminuido em 15% fica: {moeda.diminuir(preco)}')
