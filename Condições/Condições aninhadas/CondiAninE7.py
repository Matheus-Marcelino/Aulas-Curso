peso = float(input('Digite o seu peso: (kg) '))
altura = float(input('Digite a sua altura: (m) '))
massa = peso / (altura ** 2)

if massa <= 18.5:
    print('Abaixo do peso')
elif massa <= 24.9 :
    print('Peso ideal')
elif massa <= 25:
    print('Sobrepeso')
elif massa <= 30:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
