def area(altura: float, largura: float):
    print(f'A area do terreno {altura} x {largura} é de {altura * largura :.2f}m² ')


largura = float(input('Digite a largura (m): '))
altura = float(input('Digite a altura (m): '))

area(altura, largura)
