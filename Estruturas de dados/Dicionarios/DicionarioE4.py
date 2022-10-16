jogador, gols_list = dict(), list()

jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
quantidade = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
total = 0

for c in range(quantidade):
    info = int(input(f'Quantos gols na partida {c+1}? '))
    total += info
    gols_list.append(info)
jogador['gols'] = gols_list
jogador['total'] = total

print('\n', '-=' * 40)
print(jogador)
print('-=' * 40, '\n')

for key, value in jogador.items():
    print(f'O campo {key} tem valor {value}')
print('\n', '-=' * 40, '\n')

print(f'O jogador {jogador["nome"]} jogou {quantidade} partidas')
for c, gol in enumerate(jogador['gols']):
    print(f'Na partida {c+1}, fez {gol} gols')
print(f'Foi um total de {total} de gols')