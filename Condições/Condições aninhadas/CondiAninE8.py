preço = float(input('Valor das compras: '))
print("1. Pagar à vista/cheque: 10% de desconto\n2. À vista no cartão/Cheque: 5% de desconto\n"
      "3. Em até 2x no cartão: Preço normal\n4. 3x ou mais no cartão: 20% de juros")
opção = int(input('escolha uma opção: '))
print('')

if opção == 1:
    print(
        f'com os 10% de desconto o valor ficará em {preço - (preço * 10/100):.2f}R$')
elif opção == 2:
    print(
        f'com os 5% de desconto o valor ficará em {preço - (preço * 5/100):.2f}R$')
elif opção == 3:
    print(f'você pagará a parcela de 2x em {preço / 2}')
    print(f'sem descontos ou juros valor continuará de {preço}R$')
elif opção == 4:
    parcela = int(input('Quantas vezes será parcelado: '))
    print(
        f'Sua compra será parcelada em {parcela}x e vc pagará por Mês R${(preço *(1 + 20/100) ** parcela) / parcela:.2f}R$')
    print(
        f'com os 20% de juros o valor ficará em {preço *(1 + 20/100) ** parcela:.2f}R$')
else:
    print('Opção invalida!')
