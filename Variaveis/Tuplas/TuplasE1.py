from colorama import init
init()

extenso = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
    'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
    'dezessete', 'dezoito', 'dezenove', 'vinte'
)

continuacao = ''
while continuacao != 'n':
    try:
        escolha = int(input('qual número entre 0 a 20: '))
        if 0 <= escolha <= 20:
            print(extenso[escolha])
        else:
            print(
                '\033[1;31mOs número inserido não está no intervalo de 0 a 20!\033[m')
        while True:
            continuacao = str(
                input('Deseja continuar?[S/N]: ')).strip().lower()
            if 's' in continuacao:
                print('Bom estudo!')
                break
            elif 'n' in continuacao:
                break
            else:
                print('escreva corretamente!')
    except ValueError:
        print('\033[1;31mApenas números!\033[m\n')
