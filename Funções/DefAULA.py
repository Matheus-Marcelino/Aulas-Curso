def soma(a: int, b: int):
    print(f'A = {a} e B = {b}')
    soma = a + b
    print(f'A soma de A + B = {soma}')


# programa principal
soma(b=4, a=1)
soma(7, 2)
# soma(3, 9, 5) => vai dar erro


def contador(*num):  # permitie colocar quantos valores quisere jogará dentro de uma tupla
    print(num)


contador(2, 4, 5)
contador(2, 7, 3, 0)
contador(9, 7, 0, 2, 1, 54, 67)


valores = [7, 2, 5, 0, 4]


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


dobra(valores)
print(valores)


def soma2(*numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    print(f'somando os valores {numeros} temos {soma}')


soma2(7, 6)
soma2(1, 7, 5, 8, 9)
