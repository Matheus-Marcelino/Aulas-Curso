maior = menor = 0

for pessoa in range(1,6):
    peso = float(input(f'Peso da {pessoa} pessoa: '))

    if pessoa == 1:  # verificando o primeiro peso
        maior = peso
        menor = peso
    else:  # verificando os outros pesos
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso foi {maior}Kg')
print(f'O menor peso foi {menor}Kg')
