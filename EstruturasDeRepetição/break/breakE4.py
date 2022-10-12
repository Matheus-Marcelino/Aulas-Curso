maior_ID = quant_HO = quant_MU = 0

while True:
    print('=' * 30)
    print(f"{'CADASTRE UMA PESSOA': ^30}")
    print('=' * 30)

    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().lower()
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().lower()
    print('-' * 25)

    if idade >= 18:
        maior_ID += 1
    if sexo in 'm':
        quant_HO += 1
    if sexo in 'f' and idade < 20:
        quant_MU += 1

    continuar = str(input('deseja continuar? [S/N]: ')).strip().lower()
    if 'n' in continuar:
        break

print(f'{maior_ID} pessoas são maior de idade,\n'
      f'{quant_HO} Homens foram cadastrados\n'
      f'{quant_MU} Mulheres menores de 20 anos')
