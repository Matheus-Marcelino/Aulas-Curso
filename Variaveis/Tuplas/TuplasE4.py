# procurando numeros na tupla

lista_NUM = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(
    input('Digite um valor: ')), int(input('Digite um valor: ')))
pares = 0

print(f'O 9 apareceu: {lista_NUM.count(9)}')

try:  # index tem um erro, quando ele não acha o valor dentro da variavel
    print(f'O numero 3 está na posição: {lista_NUM.index(3)+1}')
except ValueError:
    print('O valor 3 não estava dentro do contexto')

for num in lista_NUM:
    if num % 2 == 0:
        pares += 1

print(f'Apareceu {pares} numeros pares!')
