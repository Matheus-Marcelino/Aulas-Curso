n = int(input('Digite um numero: '))

while True:
    if n >= 10000:
        break

    print(f'Processando o seu número: {n}')
    print(f'Seu número tem: {len(str(n))} caracteres')
    print(f'A unidade do seu numero é: {int(n / 1 % 10)}')
    print(f'A dezena do seu numero é: {int(n / 10 % 10)}')
    print(f'A centena do seu número é: {int(n / 100 % 10)}')
    print(f'O milhar do seu número é: {int(n / 1000 % 10)}')
    break
