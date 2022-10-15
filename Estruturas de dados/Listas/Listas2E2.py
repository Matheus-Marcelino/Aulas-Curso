lista_NUM = [[], []]

for _ in range(0, 7):
    numero = int(input('Digite um valor: '))
    if numero % 2 == 0:
        lista_NUM[1].append(numero)
    else:
        lista_NUM[0].append(numero)

lista_NUM[0].sort()
lista_NUM[1].sort()
print(f'Os numeros pares são: {lista_NUM[1]}')
print(f'Os numeros impares são: {lista_NUM[0]}')
