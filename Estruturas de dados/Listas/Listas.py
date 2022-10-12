num = [2, 5, 9, 1]
num[2] = 3  # listas são mutaveis
num.append(7)  # adiciona um numero no final da lista
num.sort()  # coloca em ordem crescente
"""num.sort(reverse=True) "  # coloca em ordem decrecente"""
num.insert(2, 0)  # está inserindo o numero 0 na posição 2 sem exluir os demais
num.pop()  # pop sem especificação irá excluir o ultimo numero da lista


def spc():
    print('')
    print('#' * 30)
    print('')


print(num)
print(f'Essa lista tem {len(num)} números')
spc()

# valores = list(range(4, 11)) # ele declara um lista e adiciona os numeros que estão no range
valores = list()  # ou pode iniciar uma lista na VAR só com " [] "
valores.append(5)
valores.append(9)
valores.append(4)
valores.sort(reverse=True)

for v in valores:  # para cada valor (v) em valores
    print(f'{v}...', end='')  # 'end' coloca na mesma linha

print('\n')

for c, v in enumerate(valores):  # vê a posição dos valores e mostra os mesmos
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei no final dessa lista')

spc()

n = list()

for cont in range(0, 5):
    n.append(int(input('Digite um valor: ')))  # adicionando elementos a lista

for y, x in enumerate(n):
    print(f'na posição {y} encontrei o valor {x}!')
print('cheguei no final da lista')


spc()

a = [2, 1, 4, 6]
b = a  # ligação entre as listas
# b = a[:] # O ' b ' irá copiar todos os elementos de ' a ' sem criar uma ligação
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
