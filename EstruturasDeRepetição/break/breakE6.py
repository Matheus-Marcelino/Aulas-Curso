print('=' * 30)
print(f"{'BANCO BRASIL':^30}")
print('=' * 30)

retirada = int(input('Quanto você deseja retirar? R$'))
total = retirada
céd = 100
ContCéd = 0

while True:
    if total >= céd:
        total -= céd
        ContCéd += 1

    else:
        if ContCéd > 0:
            print(f'Total de {ContCéd} cédulas de R${céd}')

        # verificando a cédula atual para modifica-la caso nã for mais necessario #
        if céd == 100:
            céd = 50
        elif céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 1
        ContCéd = 0

        if total == 0:
            print('=' * 30)
            print('Obrigado pela preferência!!')
            break
