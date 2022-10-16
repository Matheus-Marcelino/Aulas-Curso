ficha = list()
while True:
    decisao = int(input('Quantos alunos deseja cadrastar [0 finaliza]: '))
    print()

    for _ in range(decisao):
        nome = str(input('Nome: '))
        nota1 = float(input('Nota 1: '))
        nota2 = float(input('Nota 2: '))
        media = (nota1 + nota2) / 2
        ficha.append([nome, [nota1, nota2], media])
        print(f'Boletim do {ficha[0][0]} foi processado!\n')

    for pos, dado in enumerate(ficha):
        print(f'{pos} {dado[0]} {dado[2]}')

    while True:
        aluno = int(input('\ndeseja ver a nota de algum aluno?[999 finaliza] '))
        if aluno == 999:
            break
        else:
            print(ficha[aluno][1])
    
    if aluno == 999:
            break
