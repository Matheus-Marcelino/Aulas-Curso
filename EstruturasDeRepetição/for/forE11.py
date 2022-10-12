from datetime import date

ano_pess = 0
ano_pess2 = 0

for pessoa in range(1, 8):
    ano = int(input(f'ano de nascimento da {pessoa} pessoa: '))

    if date.today().year - ano >= 21:
        ano_pess += 1

    else:
        ano_pess2 += 1

print(f'Tivemos {ano_pess} pessoas maiores de idade')
print(f'tivemos {ano_pess2} pessoas menor de idade')
