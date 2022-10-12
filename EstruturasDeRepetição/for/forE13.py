idade_menor = 0
idade_maior = 0
idatot = float(0)
nomevelho = ''

for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('sexo [F/M]: ')).strip().lower()

    ''' sexo in 'Mm' '''
    # Verificando o homem mais velho
    if p == 1 and 'm' in sexo:
        idade_maior = idade
        nomevelho = nome
    ''' Pegando o dado do primeiro 'p' gerado.
        Verificando ele pelos if, no segundo if caso a idade seja a maior permanecerá
        na variavel '''
    if 'm' in sexo and idade > idade_maior:
        idade_maior = idade
        nomevelho = nome
    # Fim

    if p == 1:  # verificando as menores idades femininas abaixo de 20
        if idade < 20 and 'f' in sexo:
            idade_menor += 1
    else:
        if idade < 20 and 'f' in sexo:
            idade_menor += 1

    idatot += idade  # somando as idades

print(f'\nO nome do homem mais velho é {nomevelho} e sua idade é {idade_maior}')
print(f'Um total de {idade_menor} mulheres que têm idade abaixo de 20')   
print(f'A idade média do grupo é: {idatot / p:.1f}') 
