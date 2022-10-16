pessoas = {'nome': 'Matheus', 'sexo': 'M', 'idade': '22'}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.values())  # mostra os valores das keys como [Matheus, M, 22]
print(pessoas.keys())  #mostra as keys como [nome, sexo, idade ]
print(pessoas.items())  # mostra O dicionario todo com keys e valores
print('\n', '-=' * 40, '\n')
"""
del pessoas['sexo']  # irá excluir apenas o elemento sexo

pessoas['nome'] = 'Josh'  # irá substituir o value por Josh e apagará o Matheus

pessoas['peso'] = 60.0  # irá criar uma nova key com o value 60.0
"""

for key in pessoas.keys():
    print(key)

for value in pessoas.values():
    print(value)
    
for key, value in pessoas.items():
    print(f'{key} = {value}')

print('\n', '-=' * 40, '\n')

brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])  # mostra o value de uf do elemento 0 
print(brasil[1]['sigla']) # mostra o value de sigla do elemento 1
print('\n', '-=' * 40, '\n')

brasil.clear()
estado = dict()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))    
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())  # .copy() substitiu o [:]
    
for estate in brasil:  # varrendo a lista
    for key, value in estate.items():  # varrendo os dicionarios
        print(f'O campo {key} tem valor {value}')
