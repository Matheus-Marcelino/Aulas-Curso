n = str(input('Digíte uma frase: ')).strip().lower()

print(f'A letra A aparace {n.count("a")} na frase')
print(f'A primeira letra A apareceu na posição {n.find("a")+ 1}')
print(f'A última letra A apareceu na posição {n.rfind("a")+ 1}')  # começa contando da esquerda para direita
