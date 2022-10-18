jogador_dados, gols_list, jogador_list = dict(), list(), list()
add_jogador = int(input('Quantos jogadores você quer inserir? '))

for c in range(add_jogador):
    jogador_dados['nome'] = str(
        input('\nNome do jogador: ')).capitalize().strip()
    quantidade = int(
        input(f'Quantas partidas {jogador_dados["nome"]} jogou? '))
    total = 0

    for c in range(quantidade):
        info = int(input(f'    Quantos gols na partida {c+1}? '))
        total += info
        gols_list.append(info)
    jogador_dados['gols'] = gols_list[:]
    jogador_dados['total'] = total
    jogador_list.append(jogador_dados.copy())
    gols_list.clear()
    jogador_dados.clear()

print('\n', '-=' * 60)
print('  cod nome   gols    Total')
print('-' * 30)
for cont, value in enumerate(jogador_list):
    print(
        f'  {cont+1}º {value["nome"]:7}{str(value["gols"])}     {str(value["total"]):>3}')
print('-' * 30, '\n')

while True:
    mostrar_jogador = int(
        input('Mostrar dados de qual jogador? [999 para parar]: '))
    if 999 == mostrar_jogador:
        break
    elif 1 < mostrar_jogador > len(jogador_list):
        print(
            f'\ninfelizmente o dado {mostrar_jogador} não existe, tente novamente!')
        mostrar_jogador = int(input('Mostrar dados de qual jogador? '))
    else:
        mostrar_jogador -= 1
        print(
            f' -- LEVANTAMENTE DO JOGADOR {(jogador_list[mostrar_jogador]["nome"]).upper()}\n')
        for value, gol in enumerate(jogador_list[mostrar_jogador]['gols']):
            print(f'   No jogo {value} fez {gol} gols')
        print('-' * 30)
print('VOLTE SEMPRE !!')
