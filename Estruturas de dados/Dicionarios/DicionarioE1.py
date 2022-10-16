User = dict()

User['nome'] = str(input('Nome: ')).capitalize()
User['media'] = float(input(f'Média de {User["nome"]}: '))

print('-=' * 40)
print(f'Nome é igual a {User["nome"]}')
print(f'Média é igual a {User["media"]}')
if User['media'] >= 5:
    print('Situação é igual a Aprovado')
else:
    print('Situação é igual a Reprovado')
