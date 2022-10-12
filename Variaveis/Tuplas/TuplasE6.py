PALAVRAS = ('Matheus', 'Maria', 'Josh', 'Kauan')

for palavra in PALAVRAS:
    print(f'\nNa palavra {palavra.upper()} temos: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
print()
