lista, lista_im, lista_par = list(), list(), list()
decisao = int(input('Quantos numeros deseja digitar [0 finaliza]: '))

if decisao != 0:
    for _ in range(decisao):
        lista.append(int(input('Digite um valor: ')))
        print('adicionando a lista')

    for cont in lista:
        print(lista)
        print(cont)
        if cont % 2 == 0:
            lista_par.append(cont)
        else:
            lista_im.append(cont)

    print(f'A lista Com todos os digitos é: {lista}')
    print(f'Os numeros pares digitados foram: {lista_par}')
    print(f'Os numeros impares digitados foram: {lista_im}')
print('Obrigado por usar o programa')