# Listando produtos

PRODUTOS = ('Lapís', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25.0)

print('=' * 30)
print(f"{'LISTAGEM DE PRODUTOS':^30}")
print('=' * 30, '\n')

for produto in range(0, len(PRODUTOS)):

    if produto % 2 == 0:
        # logica matematica para mostrar os nomes dos produtos
        print((f'{PRODUTOS[produto]:.<30}'), end='')

    if produto % 2 == 1:
        # logica matematica para mostrar os preços dos produtos
        print(f'R$ {PRODUTOS[produto]:.2f}')
