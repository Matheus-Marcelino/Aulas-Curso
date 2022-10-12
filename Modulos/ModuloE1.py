from math import floor, trunc

n = float(input('Digite um número: '))

print(f'Valor digitado foi {n} e sua porção inteira é {floor(n)}')  # Retorna ao menor valor de n
print(f'Valor digitado foi {n} e sua porção inteira é {trunc(n)}')  # Corta as casas decimais
print(f'Valor digitado foi {n} e sua porção inteira é {int(n)}')  # forma simplificada
