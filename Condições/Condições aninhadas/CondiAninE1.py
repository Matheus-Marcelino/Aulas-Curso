casa = float(input('Quanto custa a casa: R$'))
salario = float(input('quanto você ganha: R$'))
financiamento = int(input('quer financiar em quantos anos: '))

if casa / (financiamento * 12) >= salario * 30/100:
    print(f'Você vai pagar uma casa de {casa} com salario de {salario}.'
          f'\npor mês você terá que pagar {casa / (financiamento *12):.2f}.\n EMPRESTIMO NEGADO')
else:
    print(f'Você vai pagar uma casa de {casa} com salario de {salario}.'
          f'\npor mês você terá que pagar {casa / (financiamento * 12):.2f}.\n EMPRESTIMO ACEITO!')
