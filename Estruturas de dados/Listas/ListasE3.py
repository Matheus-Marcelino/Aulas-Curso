lista_User = list()

while True:
    num_User = int(input('\nDigite um valor: '))
    if num_User in lista_User:
        print('infelizmente esse número ja está cadrastado, ensira outro!')
    else:
        lista_User.append(num_User)
        print('Número Cadrastado!')

    decisao = str(input('\nDeseja continuar?[S/N]: '))
    if decisao in 'Nn':
        break
        
print(f'Os números cadrastados foram: {lista_User}')
