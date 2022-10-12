from time import sleep
from random import choice

itens = ('Pedra', 'Papel', 'Tesoura')
esc_pc = choice(itens)
print('=' * 12, '\nSuas opções:\n0. Pedra\n1. Papel\n2. Tesoura')
print('=' * 12)
esc = str(input('escolha apção: '))

if esc == '0' or esc == '1' or esc == '2':
    print()
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ')
    sleep(1)
    print()
    print('=-=' * 9)
    print(f'você Jogou: {itens[int(esc)]}\nComputador Jogou: {esc_pc}')
    print('=-=' * 9)

    if itens[int(esc)] == esc_pc:
        print('EMPATE')
    elif itens[int(esc)] == 'Pedra' and esc_pc == 'Tesoura' or \
    itens[int(esc)] == 'Papel' and esc_pc == 'Pedra' or \
    itens[int(esc)] == 'Tesoura' and esc_pc == 'Papel':
        print('JOGADOR VENCEU!!')
    else:
        print('COMPUTADOR VENCEU!!')
else:
    print('Opção invalida!')
