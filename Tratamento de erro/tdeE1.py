def leiaInt(informacao: str) -> int:
    while True:
        try:
            numero = int(input(informacao))
            break
        except (ValueError, TypeError):
            print('Um erro de digitação ocorreu! tente denovo!\n')
    return numero


def leiafloat(informacao: str) -> float:
    while True:
        try:
            numero = float(input(informacao))
            break
        except (ValueError, TypeError):
            print('Um erro de digitação ocorreu! tente denovo!\n')
    return numero


inteiro = leiaInt('Digite um numero inteiro: ')
real = leiafloat('Digite um número real: ')
print(f'O números digitados foram: int: {inteiro}  Real: {real}')
