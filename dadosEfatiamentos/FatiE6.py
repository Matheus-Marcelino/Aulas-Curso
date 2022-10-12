nome = str(input('Digite seu nome: ')).strip()
n = nome.split()

print(f'Seu primeiro nome é: {n[0]}')
print(f'seu ultimo nome é: {n[len(n)- 1]}')  # vai mostrar o ultimo nome colocando o ' -1 '
