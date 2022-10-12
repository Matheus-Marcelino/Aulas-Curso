for c in range(6, 0 , -1):  # contagem regressiva de 1 até 6
    print(c)
print('Sexo\n')

for c in range(0, 6):  # faz uma contagem de 0 a 5 exluindo o ultimo número (6)
    print(c)
print('Sexo2\n')

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Pulos: '))

for c in range(i, f+1, p):  # indica o incio, fim +1 para ser o valor certo e a quantidade de pulos
    print(c)
print('fim\n')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))  # cria novas variaveis
    s += n  # pega as variaveis de n e soma
print(f'O somatório de todos os valores é {s}')
