n = s = 0

while True:
    n = int(input('Digite um numero [999]: '))
    if n == 999:
        break
    s += n

# print('A soma vale {}.format(s)'
print(f'A soma vale {s}')  # "f" minusculo antes das '' serve para substituir o ".format"
print('##########################')

nome = 'José'
idade = 33
salario = 1024.5

print(f'O {nome} tem {idade} anos.')  # f strings. Python 3.6+
print('O {} tem {} anos.'.format(nome, idade))  # Python 3
print('O %s tem %d anos.' % (nome, idade))  # usado no Python 2
print(f'O {nome} tem {idade} anos e ganha {salario:.2f}')  # ':' depois '.2f' ganha mais uma casa decimal
# '{nome^20} '^' centraliza o nome entre 20 espaços
# {nome-<20} alinhar a esquerda
# {nome->20} alinhas a direita
