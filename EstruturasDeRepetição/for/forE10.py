frase = str(input('escreva uma frase: ')).lower().strip()
palavra = frase.split()
junto = ''.join(palavra)  # juntandos as palavras
inverso = ''

""" [::-1] inverteria a frase sem problema algum """

for letras in range(len(junto) -1, -1,-1):  # uma analise regressiva para colocar no inverso 
    inverso += junto[letras]
print(f'''Sua frase "{frase}" e sua frase invertida é "{inverso}" ''')

if junto == inverso:
    print(f'a frase {frase} é um palidromo')
else:
    print(f'a frase {frase} não é um palidromo')
