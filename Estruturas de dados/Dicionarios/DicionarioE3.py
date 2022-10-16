from datetime import date

dados = dict()

dados['nome'] = str(input('Nome: ')).capitalize()
idade_total = date.today().year - int(input('Ano de nascimento: '))
dados['idade'] = idade_total
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados['ctps'] == 0:
    for key, value in dados.items():
        print(f' - {key} tem o valor: {value}')
else:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = int(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + \
        ((dados['contratação'] + 35) - date.today().year)
    for key, value in dados.items():
        print(f' - {key} tem o valor: {value}')
