frase = 'Curso em Vídeo Python'
# 'capitalize()' Coloca a promeira letra em maiúsculo
# 'title()' Coloca o começo das palavras em maiúsculo
# 'join()'


def spc():
    print('')
    print('#' * 30)
    print('')


print(frase[3:13])  # da quarta letra até a letra 13
print(frase[:13])  # da letra 13 até o final
print(frase[1:15:2])  # da letra 1 até a 15 pulando de 2 em 2
print(frase[::2])  # a frase inteira pulando de 2 em 2
"""[começo: final: 'pulos']"""
spc()
print(f"Letra O: {frase.upper().count('O')}")  # colocando em maiúsculo e contando os "O" maiúsculo
print(f"Letra o: {frase.count('o')}")  # vai contar quantos "o" tem na frase
print(len(frase))  # tamanho da frase
"""print(frase.strip())"""
# '.strip()' Remove os espaços indesejados
spc()

Fras = 'Hi, World!'

""" print(Fras.replace('hi', 'Hello'))
    print(Fras)"""
# Tem que salvar o dado antes de fazer uma alteração

Fras = Fras.replace('Hi', 'Hello')
print(Fras)
print(Fras.find('World'))  # Procura e diz a posição de 'World'
print('World' in Fras)  # diz se existe a 'World' na Fras
print(Fras.find('hello'))  # se não achar aparecerá '-1'
print(Fras.lower().find('hello'))  # passando para minusculo e dando posição

dividido = Fras.split()
print(dividido[1][1])  # separando a frase e dando a poisção [Palavra1, letra1]

