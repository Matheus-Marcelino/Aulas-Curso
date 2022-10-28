from uteis_aula import numeros
# from uteis import * -> importa tudo
# from uteis import numeros, strings, datas -> importa separadamente

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
print(f'O triplo de {num} é {numeros.triplo(num)}')
"""
|
|
---> Pacotes são as pastas 
        |
        |
        ---> Modulos são os arquivos
"""
