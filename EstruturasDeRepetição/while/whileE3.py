from math import factorial

'''Fatorial'''

n = int(input('Digite seu valor: '))
print(f'o fatorial de {n} é {factorial(n)}')

'''Forma tradicional'''

tot = 1 
c = n
print(f'{n}! = ', end='')
while c > 0:
    print(f'{c}', end ='')
    print(' x ' if c > 1 else ' = ', end = '')
    tot *= c
    c -= 1 
print(end='' f'{tot}')
print('','#' * 10,'')

resultado=1

print(f'{n}! = ', end='')
for cont in range(1,n+1):
    print(f'{cont}', end ='')
    print(' x ' if cont < 10 else ' = ', end = '')
    
    resultado *= cont

print(resultado)
