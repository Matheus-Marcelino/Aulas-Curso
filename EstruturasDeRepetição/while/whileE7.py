n = cont = soma = 0
n =  int(input('Digite um número [999]: '))

while n != 999:
    cont += 1
    soma += n
    n =  int(input('Digite um número [999]: '))

print(f'A soma entre os números foi: {soma}')  # soma - 999
print(f'você digitou {cont} números')  # cont - 1 
