from moedaE3 import moeda as md

preco = float(input('Digite o preço: R$'))

print(
    f'O seu valor de {md.moeda(preco)} dobrado fica: {md.dobro(preco)}')
print(
    f'O seu valor de {md.moeda(preco)} pela metade fica: {md.metade(preco)}')
print(
    f'O seu valor de {md.moeda(preco)} aumentado em 10% fica: {md.aumentar(preco, 10)}')
print(
    f'O seu valor de {md.moeda(preco)} diminuido em 15% fica: {md.diminuir(preco, 15)}')
