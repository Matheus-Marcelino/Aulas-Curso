from colorama import init
init()

lista_NUM = list()

for dados in range(0, 5):
    lista_NUM.append(int(input("Digite um valor: ")))

print(f'\nO maior valor digitado foi \033[1;32m{max(lista_NUM)}\033[m')
print(f'O menor valor digitado foi \033[1;32m{min(lista_NUM)}\033[m')
