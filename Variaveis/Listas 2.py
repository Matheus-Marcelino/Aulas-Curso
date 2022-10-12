teste = list()
teste.append('Matheus')
teste.append(17)
galera = list()
galera.append(teste[:])  # " : " para fzr uma copia da lista
teste[0] = 'Maria'
teste[1] = 17
galera.append(teste[:])  # para adicionar maria


print(galera)
print('')

pessoas = [['Marcos', 15], ['Maria', 17], ['Matheus', 17], ['joão', 18]]


print(pessoas)
print(pessoas[2][0])
print('')

for p in pessoas:
    print(p)  # vai mostrar tudo
    print(p[0])  # vai mostrar só os nomes
print('')

a = list()
dado = list()


for c in range(0, 3):  # criando listas temporarias
    dado.append(str(input('Nome: ')))  # adicionando um nome a lista dado
    dado.append(int(input('Idade: ')))
    a.append(dado[:])
    dado.clear()  # limpar os dados
print(a)

totmai = totmen = 0

for c in a:
    if c[1] >= 21:
        print(f'{c[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{c[0]} é menor de idade')
        totmen += 1
print(f'temos {totmai} maiores de idade e {totmen} menores de idade')
