lista_temp, lista_users = list(), list()
decisao = int(input('Quantas pessoas voce deseja cadrastar [0 finaliza]: '))
maior = menor = 0

for c in range(decisao):
    print(c)
    lista_temp.append(str(input('Nome: ')))
    lista_temp.append(float(input('peso: ')))
    print('Adicionando dados..\n')
    if len(lista_users) == 0:
        maior = menor = lista_temp[1]
    else:
        if lista_temp[1] > maior:
            maior = lista_temp[1]
        if lista_temp[1] < menor:
            menor = lista_temp[1]
    lista_users.append(lista_temp[:])
    lista_temp.clear()

print(f'A quantidade de pessoas cadrastadas froma: {len(lista_users)}')
print(f'O maior peso foi de {maior}Kg do/s ', end='')
for user in lista_users:
    if user[1] == maior:
        print(f'{user[0]}')
print(f'O menor peso foi de {menor}Kg do/s ', end='')
for user in lista_users:
    if user[1] == menor:
        print(f'{user[0]}')
