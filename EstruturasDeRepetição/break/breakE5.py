tot = acim_1K = barato = cont = 0
nome_barato = ' '

while True:
    nome = str(input('Nome do produto: ')).strip()
    valor = float(input('Valor do produto: R$'))
    tot += valor
    cont += 1

    if valor > 1000:
        acim_1K += 1

    if cont == 1 or valor < barato:
        barato = valor
        nome_barato = nome

    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().lower()
    if continuar == 'n':
        break

print(f'O total das compras foram {tot:.2f}\n'
      f'{acim_1K} produtos acima de 1000.00 R$\n'
      f'O o produto mais barato foi o(a) {nome_barato} custando {barato}')
