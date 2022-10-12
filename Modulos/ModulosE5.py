from random import shuffle

a = list()

for c in range(0, 4):
    a.append(str(input('Nome do aluno/a: ')))
shuffle(a)    # 'shuffle' embaralha os numeros elementos

print(f'Os alunos escolhidos foram {a}')
