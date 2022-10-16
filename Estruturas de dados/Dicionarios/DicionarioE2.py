from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'jogador1': randint(1, 4),'jogador2': randint(1, 4),
             'jogador3': randint(1, 4), 'jogador4': randint(1, 4)}
ranking = list()

for key, value in jogadores.items():
    print(f'{key} tirou {value} no dado.')
    sleep(0.5)
print('-=' *  40)
print(f' {"RANKING DOS JOGADORES" :^10}')

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for c, value in enumerate(ranking):
    print(f'{c+1}º lugar: {value[0]} com {value[1]}')
    sleep(0.5)
