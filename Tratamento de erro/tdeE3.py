from time import sleep
from tdeE3Mol.cadastro import cadastrar, mostrar_cadastro
from tdeE3Mol import estilo, leiaInt, clear

while True:
    estilo('MENU PRINCIPAL', 43)
    print('\033[1;33m1 -\033[m \33[1;35mCadastrar nova Pessoa\033[m'
          '\n\033[1;33m2 -\033[m \033[1;35mVer pessoas cadastradas\033[m'
          '\n\033[1;33m3 -\033[m \033[1;35mLimpar Terminal\033[m'
          '\n\033[1;33m4 -\033[m \033[1;35mSair do programa\033[m')
    decisao = leiaInt('Sua opção: ')

    if decisao == 1:
        estilo('CADASTRO', 43)
        cadastrar()
        print('\033[1;32mCADASTRADO COM SUCESSO!\033[m\n')

    elif decisao == 2:
        estilo(" LOGGIN'S ", 43)
        try:
            datas = mostrar_cadastro()
            if datas == 'vazio':
                print('\033[1;33mInfelizmente ninguém foi encontrado na \nbase de dados. '
                      '\033[1;32mCadastre alguém!\033[m')
                continue
            for i in range(len(datas)):
                for j in range(len(datas[i])):
                    if j % 2 == 0:
                        print('{:<30}'.format(
                            datas[i][j].replace('_', ' ')), end='')
                    else:
                        print(f'{datas[i][j]} Anos')
                print(end='')
            sleep(2)
        except FileNotFoundError:
            print('\033[1;31mO arquivo não existe!\033[m, \033[1;32mclique "1" para \n'
                  'cadrastar uma pessoa para ele ser criado\033[m')
    elif decisao == 3:
        clear()

    elif decisao == 4:
        clear()
        print('\033[1;33mFinalizando...\033[m')
        sleep(2)
        break

    else:
        print(f'\033[1;31mO comando "{decisao}" não foi reconhecido pelo\n'
              'sistema, porfavor faça uma escolha valida!\033[m')
print('\033[1;32mVolte sempre :)\033[m')
sleep(1.5)
