opção = 's'
soma = cont = maior = menor = 0

while opção in 's':
    números = int(input('Digite um número: '))
    soma += números
    cont += 1
    if cont == 1:
        maior = menor = números
    else:
        if números > maior:
            maior = números
        if números < menor:
            menor = números
    opção = str(input('Deseja continuar?[s/n] ')).strip().lower()

print(f'O seu maior número é: {maior}\nO seu menor número é: {menor}\n'
      f'A média entre os números é {float(soma/ cont):.2f}')
