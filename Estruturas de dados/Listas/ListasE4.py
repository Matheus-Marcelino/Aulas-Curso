lista_num = list()

for c in range(0, 5):
    numero = int(input('Digite um valor: '))
    print('Adicionando a lista')
    if c == 0 or numero > lista_num[-1]:
        lista_num.append(numero)
    else:
        for pos in range(len(lista_num)):
            if numero <= lista_num[pos]:
                lista_num.insert(pos, numero)
                break

print(f'\nOs dados digitados em ordem crescente é: {lista_num}')
