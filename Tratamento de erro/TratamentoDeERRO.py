"""
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except:  -> se não especificar erros, ele irá tratar qualquer tipo!
"""

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ZeroDivisionError, ValueError):  # -> especificando erro <-
    # colocar em uma tupla para tratar mais de um erro
    print('Tivemos um problema :(')
else:  # caso der certo
    print(f'O resultado é {r}')
finally:  # será executavel sempre no final do programa
    print('Volte sempre :)')


try:
    a = int(input('\nNumerador2: '))
    b = int(input('Denominador2: '))
    r = a / b
except Exception as error:
    # irá mostrar a classe
    print(f'O problema encontrado foi {error.__class__}')

else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre :)')


try:
    a = int(input('\nNumerador3: '))
    b = int(input('Denominador3: '))
    r = a / b
except TypeError:  # todo try pode ter mais de um except
    pass
except ValueError:
    pass
except ZeroDivisionError:
    pass
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre :)')
