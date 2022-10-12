# extraindo as vogais dos nomes

PALAVRAS = ('Matheus', 'Maria', 'Josh', 'Kauan')

for palavra in PALAVRAS:  # Acessando as palavras
    print(f'\nNa palavra {palavra.upper()} temos: ', end='')
    for letra in palavra:  # acessando as letras
        if letra.lower() in 'aeiou':  # especificando as vogais
            print(letra, end=' ')
print()
