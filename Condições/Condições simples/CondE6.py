n = float(input('Digite um valor:'))
n1 = float(input('Digite o segundo valor:'))
n2 = float(input('Digite o terceiro valor:'))
menor = n
# verificando o menor
if n1 < n and n1 < n2:
    menor = n1
if n2 < n and n2 < n1:
    menor = n2
# verificando o maior
maior = n
if n1 > n and n1 > n2:
    maior = n1
if n2 > n and n2 > n1:
    maior = n2

print(f'O maior numero é {maior}')
print(f'O menor número é {menor}')
