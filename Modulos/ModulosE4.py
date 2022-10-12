from random import choice

a = list()

for c in range(0, 4):
    a.append(str(input('Primeiro aluno: ')))  # adicionando a lista

print(f'O aluno/a foi {choice(a)}')  # 'choice' faz uma escolha aleatória da lista
