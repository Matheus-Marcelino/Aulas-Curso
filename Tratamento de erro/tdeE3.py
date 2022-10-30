from time import sleep
from tdeE3Mol.cadastro import cadastrar, mostrar_cadastro
from tdeE3Mol import estilo, leiaInt, clear

while True:
    estilo('MENU PRINCIPAL', 40)
    print('\033[1;33m1 -\033[m \33[1;35mCadastrar nova Pessoa\033[m'
          '\n\033[1;33m2 -\033[m \033[1;35mVer pessoas cadastradas\033[m'
          '\n\033[1;33m3 -\033[m \033[1;35mSair do programa\033[m'
          '\n\033[1;33m4 -\033[m \033[1;35mLimpar Terminal\033[m')
    decisao = leiaInt('Sua opção: ')

    if decisao == 1:
        estilo('CADASTRO', 40)
        cadastrar()
    elif decisao == 2:
        estilo(" LOGGIN'S ", 40)
        datas = mostrar_cadastro()
        for i in range(len(datas)):
            for j in range(len(datas[i])):
                if j % 2 == 0:
                    print('{:<30}'.format(datas[i][j].replace('_', ' ')), end='')
                else:
                    print(f'{datas[i][j]} Anos')
            print()
        sleep(2)
    elif decisao == 3:
        clear()
        print('\033[1;33mFinalizando...\033[m')
        sleep(2)
        break
    elif decisao == 4:
        clear()
    else:
        print(f'\033[1;31mCaracter "{decisao}" não foi reconhecido pelo sistema, '
              'porfavor faça uma escolha valida!\033[m')
print('\033[1;32mVolte sempre :)\033[m')
sleep(1.5)
