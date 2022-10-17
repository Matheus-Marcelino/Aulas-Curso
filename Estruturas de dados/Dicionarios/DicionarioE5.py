lista_user, dados_user = list(), dict()
soma = maior_masc = maior_fem = 0
while True:
    try:
        quantidade = int(input('Quantas pessoas você quer cadrastar: '))
        break
    except ValueError:
        print('Apenas números inteiros\n')

for _ in range(quantidade):
    dados_user['nome'] = str(input('Nome: ')).capitalize().strip()
    dados_user['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()
    while dados_user['sexo'] not in 'MF':
        dados_user['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()
    while True:
        try:
            dados_user['idade'] = int(input('Idade: '))
            soma += dados_user['idade']
            break
        except ValueError:
            print('Apenas números inteiros\n')
    lista_user.append(dados_user.copy())
    dados_user.clear()
    print('Usuario Cadrastado!', '\n')

print('-=' * 40)
print(f'A) Ao todo temo {len(lista_user)} pessoas cadrastadas')
print(f'B) A média de idade é de {float(soma/quantidade):.2f} anos')
print('C) As mulheres Cadrastadas foram: ', end='')
for dados in lista_user:
    if dados['sexo'] == 'F':
        print(dados['nome'], end=' ')
print()
print('D) Pessoas com idade acima da média: ')
for dados in lista_user:
    if dados['idade'] > soma/quantidade:
        print(f'{   dados["nome"]} com {dados["idade"]}')
