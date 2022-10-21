def voto(idade):
    from datetime import date  # scopo de importação, só irá funcionar durante essa função
    print(date.today().year)
    idade = date.today().year - idade
    if 65 > idade >= 18:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
    elif 15 < idade < 18 or idade >= 65:
        print(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        print(f'Com {idade} anos: NÃO VOTA.')


ano = int(input('Em que ano você nasceu: '))
voto(ano)
