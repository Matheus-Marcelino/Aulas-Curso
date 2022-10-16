User = dict()

User['nome'] = str(input('Nome: ')).capitalize()
User['media'] = float(input(f'Média de {User["nome"]}: '))

print('-=' * 40)
print(f' - Nome é igual a {User["nome"]}')
print(f' - Média é igual a {User["media"]:.2f}')
if User['media'] >= 5.0:
    User['situação'] = 'Aprovado'
else:
    User['situação'] = 'Reprovado'

print(f' - Situação é igual a {User["situação"]}')
