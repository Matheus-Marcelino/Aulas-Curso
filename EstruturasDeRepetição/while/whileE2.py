dado = int(input('Digite o seu primeiro valor: '))
dado2 = int(input('Digite o seu segundo valor: '))
opção = 0

while opção != 5:
    print('\n[1].Somar\n[2].Multiplicar\n[3].Maior\n[4].Novos números\n[5].Sair do programa')
    opção = int(input('>> '))
    
    if opção == 1:
        print(f'A soma dos seus valores é {dado + dado2}')
        print('=-=' * 10)
    elif opção == 2:
        print(f'A multiplicação dos seus valores é {dado * dado2}')
        print('=-=' * 10)
    elif opção == 3:
        if dado == dado2:
            print('O valores são o mesmo')
        elif dado > dado2:
            print(f'O maior valor é {dado}')
            print('=-=' * 10)
        else:
            print(f'O maior valor é {dado2}')
            print('=-=' * 10)
    elif opção == 4:
        dado = int(input('Novo primeiro valor: '))
        dado2 = int(input('Novo segundo valor: '))
        print('=-=' * 10)
    elif opção == 5:
        print('\nObrigado por usar o programa!')
    else:
        print('Escreva corretamente!')
