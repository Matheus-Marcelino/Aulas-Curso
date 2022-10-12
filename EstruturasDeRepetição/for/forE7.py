soma = 0
cont = 0

for c in range(0, 6):  # somando pares
    dado = int(input('digite um valor: '))

    if dado % 2 == 0:
        soma += dado
        cont += 1

print(f'Você informou {cont} números pares e a soma dele é {soma}')
 