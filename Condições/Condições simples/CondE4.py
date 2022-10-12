n = float(input('Sua viagem em Km: '))

if n <= 200:
    print(f'O valor da sua viagem é de {n * 0.50:.2f}')
else:
    print(f'O valor de sua viagem é de {n * 0.45:.2f}')
