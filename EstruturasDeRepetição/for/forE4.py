s = 0  # acumulador
cont = 0  # contador

for c in range(1, 501, 2):  # somando e contando multiplos de 3
    if c % 3 == 0:
        cont += 1
        s += c
print(s)
print (cont)
