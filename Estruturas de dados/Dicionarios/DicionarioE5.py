lista_user, dados_user= list(), dict()

try:
    quantidade = int(input('Quantas pessoas você quer cadrastar: '))
except ValueError:
    print('Apenas números inteiros')
    quantidade = int(input('Quantas pessoas você quer cadrastar: '))

for c in range(quantidade):
    dados_user['nome'] = str(input('Nome: ')).capitalize().strip()
    dados_user['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()
    while dados_user['sexo'] not in 'M' or dados_user['sexo'] not in 'F':    
        dados_user['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()
    try:
        dados_user['idade'] = int(input('Idade: '))
    except ValueError:
        print('Apenas números inteiros')
        dados_user['idade'] = int(input('Idade: '))
    lista_user.append(dados_user.copy)
