Lista_Num = [-1, -4, -8, 0, 5, 7, 8]
lista_User = list()

for _ in range(0, 7):
    num_User = int(input('\nDigite um valor: '))
    if num_User in Lista_Num:
        print('infelizmente esse número ja está cadrastado, ensira outro!')
    else:
        lista_User.append(num_User)
        print('Número Cadrastado!')

print(f'Os números cadrastados foram: {lista_User}')
