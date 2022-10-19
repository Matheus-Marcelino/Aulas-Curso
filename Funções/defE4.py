def maior():
    print(f'O maior numero foi {max(numeros)}')
    print(f'O menor numero foi {min(numeros)}')


numeros = list()
quantidade = int(input('Quantos numeros deseja digitar? '))

for _ in range(quantidade):
    numeros.append(int(input('Digite um valor: '))) 

maior()
