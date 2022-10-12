import math
import random

num = int(input('digite um numero: '))


def spc(txt):
    print('')
    print(txt)


spc(f'A raiz do número {num} é {math.ceil(math.sqrt(num))}')  # ceil arredonda para cima
spc(f'A raiz do número {num} é {math.floor(math.sqrt(num))}')  # floor arrendoda para baixo

print('#' * 20)
spc(f'Me mostre um numero aleatório {random.random()}')  # random == numero aleatório entre 0 e 1
spc(f'me mostre um numero aleatório inteiro {random.randint(1, 20)}')  # randint  == numero inteiro aleatório limitado
