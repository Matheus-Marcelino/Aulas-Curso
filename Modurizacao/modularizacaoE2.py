from moedaE2 import moeda

preco = float(input('Digite o preço: R$'))

print(
    f'O seu valor de {moeda.moeda(preco)} dobrado fica: {moeda.moeda(moeda.dobro(preco))}')
print(
    f'O seu valor de {moeda.moeda(preco)} pela metade fica: {moeda.moeda(moeda.metade(preco))}')
print(
    f'O seu valor de {moeda.moeda(preco)} aumentado em 10% fica: '
    f'{moeda.moeda(moeda.aumentar(preco, 10))}')
print(
    f'O seu valor de {moeda.moeda(preco)} diminuido em 15% fica: '
    f'{moeda.moeda(moeda.diminuir(preco, 15))}')
