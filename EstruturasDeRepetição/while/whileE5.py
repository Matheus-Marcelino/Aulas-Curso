n = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
cont = 1
total = 0
opção = 10

# Super Progressão aritimetica
while opção != 0:
    total += opção
    while cont != total:
        print(f'{n}', end=' >> ')
        cont += 1
        n += razão
    print('pausa')
    opção = int(input('Gostaria de receber mais quantos termos?: '))
print(f'Você teve um total de {cont - 1} termos')
