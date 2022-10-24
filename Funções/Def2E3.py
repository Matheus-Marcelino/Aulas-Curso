def Ficha() -> None:
    jogador = str(input('Nome do jogador: ')).strip().title()
    gols = str(input('Quantidade de gols: ')).strip()
    try:
        gols = int(gols)
    except ValueError:
        gols = 0

    if jogador == '' or jogador == ' ':
        jogador = '<desconhecido>'

    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')


Ficha()
