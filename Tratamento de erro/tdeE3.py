from tdeE3Mol import estilo, leiaInt, clear
from tdeE3Mol.cadastro import cadastrar, mostrar_cadastro

while True:
    estilo('MENU PRINCIPAL', 40)
    print('\033[1;33m1 -\033[m \33[1;35mCdrastar nova Pessoa\033[m'
          '\n\033[1;33m2 -\033[m \033[1;35mVer pessoas cadrastadas\033[m'
          '\n\033[1;33m3 -\033[m \033[1;35mSair do programa\033[m')
    decisao = leiaInt('Sua opção: ')

    if decisao == 1:
        cadastrar()
    elif decisao == 2:
        mostrar_cadastro()
    elif decisao == 3:
        break
    else:
        print(f'\033[m1;31mPalavra "{decisao}" não reconhecida pelo sistema, '
              'porfavor faça uma escolah valida!\033[m')
print('acabou')
