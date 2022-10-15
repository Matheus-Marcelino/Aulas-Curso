matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
maior = soma = soma2 = 0

for i in range (0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))
        if matriz[i][j] % 2 == 0:
            soma += matriz[i][j] 
        if j == 2:
            soma2 += matriz[i][2]
        if matriz[1][j] > maior:
            maior = matriz[1][j]

print('-=-' * 30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()
print('-=-' * 30)

print(f'A soma dos valores pares é: {soma}')
print(f'A soma dos valores da terceira coluna é: {soma2}')
print(f'O maior valor da segunda linha é: {maior}')
