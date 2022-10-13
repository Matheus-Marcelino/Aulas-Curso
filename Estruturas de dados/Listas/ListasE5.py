lista = list()
decisao = int(input('Quantos numeros deseja digitar [0 finaliza]: '))

if decisao != 0:
    for c in range(decisao):
        lista.append(int(input('Digite um valor: ')))
        print('adicionando a lista')
    print(f'O total de números digitados foi: {len(lista)}')
    lista.sort(reverse=True)
    print(f'A lista em forma decrescente é: {lista}')
    if 5 in lista:
        print('O valor cinco está na lista!')
    else:
        print('o valor 5 não está na lista!')

print('Obrigado por usar o programa')
