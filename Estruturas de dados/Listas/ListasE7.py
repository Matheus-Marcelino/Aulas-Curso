lista_dir, lista_esq = list(), list()
expressao = str(input('digites uma expressão: '))
for c in expressao:
    if '(' in c:
        lista_dir.append(c)
    elif ')' in c:
        lista_esq.append(c)

if len(lista_dir) == len(lista_esq):
    print('Sua expressão está correta!')
else:
    print('sua expressão está errada')
