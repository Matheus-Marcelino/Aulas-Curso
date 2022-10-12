idade = int(input('Digite sua idade: '))

if idade < 18:
    print(f'Você ainda não pode se alistar.. falta {18 - idade} ano[s]')
elif idade == 18:
    print(f'Já está na hora de se alistar!')
else:
    print('Você não pode mais se alistar!')
