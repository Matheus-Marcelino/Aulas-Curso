from random import randint
from time import sleep

print('-' * 30)
print(f'{"JOGO DA MEGA SENA":^30}')
print('-' * 30)

decisao = int(input('Quantos jogos você quer que eu sorteie? '))

for c in range(1, decisao+1):
    Lista_palpites = [randint(1, 60), randint(1, 60), randint(1, 60),
                      randint(1, 60), randint(1, 60), randint(1, 60)]
    print(f'jogo {c}: {Lista_palpites}')
    sleep(0.5)
