from datetime import date

ano = int(input('Qual ano quer analisar? digite 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year   # pega o ano atual constado no pc
if ano % 4 == 0 or ano % 400 == 0 and ano % 100 != 0:
    print(f'O ano de {ano} é um ano bissexto')
else:
    print(f'O ano de {ano} é um ano comum')
