from random import randint

cont = 0

while True:
    soma = 0
    n = int(input('Escolha um número: '))
    esc = str(input('Par ou impar [P/I]: ')).upper().strip()

    if n > 10:
        print('\nO valor maximo é 10!')

    elif esc in 'P' or esc in 'I':
        n_PC = randint(0, 10)
        soma = n + n_PC

        print('=' * 50,)
        print(f'Você jogou {n} e o Computador {n_PC}, a soma deu {soma}')
        print('=' * 50)

        if soma % 2 == 0 and esc in 'P' or soma % 2 != 0 and esc in 'I':
            print('O jogador venceu!')
            cont += 1
        else:
            print(f'O Computador venceu!\nVocê teve {cont} vitórias!')
            break

    else:
        print('\nEscolha corretamente!')
