lanche = ('Hambúrguer', 'Suco', 'Pizza', 'pudim')  # tupla
# tuplas são imutaveis
print(lanche)
print(lanche[1])
print(lanche[-2])  # contagem regressiva até o -2
print(lanche[1:3])  # desconsiderando o ultimo
print(sorted(lanche))  # coloca em ordem os elementos
print()

for comida in lanche:
    print(comida, end=', ')
print()

for cont in range(0, len(lanche)):
    print(lanche[cont], cont)  # mostrar o lanche na posição cont
print()

for pos, c in enumerate(lanche):
    print(pos, c)  # posição e o elemento
print()

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(b + a)
print(len(c))
print(c.count(5))
print(c.index(8))  # mostra a posição
print(c.index(2, 4))  # a partir da posição 4 me mostre o dois
print()

pessoa = ('Matheus', 17, 'M', 61.00)
# del(pessoa) #  # del() serve para apagar uma variavel #
print(pessoa)
