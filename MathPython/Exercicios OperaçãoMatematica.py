numero = int(input('Digite um numero: '))


print('Numero antecessor: {}\nNumero sucessor: {}'.format(numero-1, numero+1))
print('Dobro do numero: {}\nTriplo do numero: {}'.format(numero*2, numero*3))
print('A raiz quadrada: {:.2f}'.format(numero ** (1/2)))
# :.2f: significa que pode ter até duas casa decimais atras da virgula
print('=============================')
print('Calculador de Média')

n1 = float(input('Sua Nota: '))
n2 = float(input('Segunda Nota: '))
n3 = float(input('Terceira Nota: '))
n4 = float(input('Quarta Nota: '))
n5 = float(input('Quinta Nota: '))
media = float(((n1+n2+n3+n4+n5) / 5))


print(('Sua Média é: {:.2f}'.format(media)))
print('=============================')
print('Convertor de Reais para Dolares')

reais = float(input('Sua quantia em Reais: '))


print('Reais para Dolares')
print('Você tem {:.2f} Dolares convertidos'.format(reais / 5.65))
print('=' * 30)

dolar = float(input('sua quantia em dolares: '))


print('Dolares para Reais')
print('Você tem {:.2f} Reais Convertidos'.format(dolar / 0.18))
