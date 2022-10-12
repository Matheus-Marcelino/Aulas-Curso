sexo = str(input('Qual o seu sexo: [F/M]: ')).lower()[0].strip()

while sexo not in 'mf':
    sexo = str(input('dados invalidos, Qual o seu sexo? [F/M]: ')).lower()[0].strip()

print(f'sexo {sexo} registrado com sucesso!')
