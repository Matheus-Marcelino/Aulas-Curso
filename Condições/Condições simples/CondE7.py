salario = float(input('Digite seu salário: '))

if salario >= 1250.00:
    print(f'O seu aumento é de 10%\nPortanto seu salario ficará em {salario * (10 / 100) + salario:.2f}R$')
else:
    print(f'O seu aumento é de 15%\nPortando seu salário ficará em {salario * (15 / 100) + salario:.2f}R$')
