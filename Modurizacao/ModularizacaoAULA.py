import uteis
# from uteis import * -> importa tudo
# from uteis import fatorial, dobro, uteis -> importa separadamente

num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {uteis.dobro(num)}')
print(f'O triplo de {num} é {uteis.triplo(num)}')
"""
|
|
---> Pacotes são as pastas 
        |
        |
        ---> Modulos são os arquivos
"""