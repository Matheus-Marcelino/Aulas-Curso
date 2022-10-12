n1 = int(input('digite um número inteiro: '))
print('1. Binario\n2. Hexadecimal\n3. Octal')
conversão = int(input('>> '))

if conversão == 1:
    print(f'seu número {n1} convertido em binario é {bin(n1)[2:]}') # 'bin()' converter um número para binario
elif conversão == 2:
    print(f'Seu número {n1} convertido em hexadecimal é {hex(n1)[2:]}') # 'hex()'  converte para hexadecimal
elif conversão == 3:
    print(f'Seu número {n1} convertido em Octal é {oct(n1)[2:]}') # 'oct()' converte para octal  [2:] para retirar a indicação do python
else:
    print('Escreva corretamente!')
