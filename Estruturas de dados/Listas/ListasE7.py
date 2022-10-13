lista_dir, lista_esq = list(), list()
expressao = str(input('digites uma expressão: '))
for simbolo in expressao:
    if '(' in simbolo:
        lista_dir.append(simbolo)
    elif ')' in simbolo:
        lista_esq.append(simbolo)

if len(lista_dir) == len(lista_esq):
    print('Sua expressão está correta!')
else:
    print('sua expressão está errada')
