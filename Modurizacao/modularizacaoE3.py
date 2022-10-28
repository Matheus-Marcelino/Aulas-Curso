from moedaE3 import moeda

preco = float(input('Digite o preço: R$'))

print(
    f'O seu valor de {moeda.moeda(preco)} dobrado fica: {moeda.dobro(preco)}')
print(
    f'O seu valor de {moeda.moeda(preco)} pela metade fica: {moeda.metade(preco)}')
print(
    f'O seu valor de {moeda.moeda(preco)} aumentado em 10% fica: {moeda.aumentar(preco, 10)}')
print(
    f'O seu valor de {moeda.moeda(preco)} diminuido em 15% fica: {moeda.diminuir(preco, 15)}')
