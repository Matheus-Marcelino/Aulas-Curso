from random import randint

# aleatorizando numeros nas tuplas

lista_NUM = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9))
print(lista_NUM)

for num in lista_NUM:
    print(num, end=' ')

print(f'\nO maior valor sorteado foi: {max(lista_NUM)}')
print(f'O menor valor sorteado foi: {min(lista_NUM)}')
