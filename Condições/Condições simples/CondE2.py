print('\033[1;31mVELOCIDADE MAXIMA DE 80KM\033[m')
print('')

radar = float(input('Velocidade do carro: '))

if radar > 80:
    print('\033[1;31mVOCÊ EXCEDEU O LIMITE')
    print(f'SUA MULTA É DE\033[m \033[1;33m{(radar - 80) * 7 :.2f}R$\033[m')
else:
    print('\033[1;32mVocê está dentro do limite, continue assim!\033[m')
