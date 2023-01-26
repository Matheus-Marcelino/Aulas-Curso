from os import system
from os.path import dirname, realpath, join
from time import sleep
from getpass import getpass
from cript import Hash
from colorama import init
from manager_json import JsonManager


class JLogin(JsonManager, Hash):
    def __init__(self) -> None:
        self.__root = dirname(realpath(__file__))
        self.__path_data = join(self.__root, 'data/data.json')
        self.__hash = Hash(6)
        init()

    def __timer_clear(self, timer: float) -> None:
        """Apenas um auxiliar na hora de programar"""
        sleep(timer)
        system('cls')

    def __home(self, data: dict) -> None:
        """Home page"""
        while True:
            print('\033[1;33m     Menu\033[m\n\033[1;32mSeja Bem-Vindo\033[m'
                  '\n\n1- Alterar Login\n2- Recuperar Senha\n3- Sair')
            try:
                opc = str(input('\n>> '))
            except KeyboardInterrupt:
                print('\033[1;31mShutting down the system\033[m')

            match opc:
                case '1':
                    try:
                        self.__timer_clear(0)
                        self.__update_loggin(data)
                    except KeyboardInterrupt:
                        print('\0331;31mUpdate login canceled\033[m')
                        self.__timer_clear(2)
                case '2':
                    try:
                        self.__timer_clear(0)
                        self.__recovery_pass(data)
                    except KeyboardInterrupt:
                        print('\033[1;31mRecovery canceled\033[m')
                        self.__timer_clear(2)
                case '3':
                    print('\033[1;32mVolte sempre!\033[m')
                    break
                case _:
                    print('\033[1;31mOption invalid!\033[m')
                    self.__timer_clear(2)

    def __update_loggin(self, data: dict) -> None:
        """Atualiza os dados no Database"""
        TOKEN = data["code"]
        print('\033[1;32m--- Update Login ---\033[m')
        username = str(input('Enter new your username: '))

        while self.__hash.cript(username) == data['username']:
            print(
                '\n\033[1;33mThe new username is the same as the old one\033[m')
            confirmation = str(
                input('do you wish to continue [Y/N]: ')).lower().strip()
            match confirmation:
                case 'y' | 'yes':
                    break
                case 'n' | 'no' | 'not':
                    username = str(input('Enter new your username: '))

        while self.__hash.cript(username) != data['username']:
            username = str(input('Enter your username: '))
            confirm_username = str(
                input(f'is this name "{username}" correct? [Y/N]: ')).lower().strip()
            match confirm_username:
                case 'y' | 'yes':
                    break
                case 'n' | 'no' | 'not':
                    print()
                    continue
                case _:
                    print('\033[1;31mOption invalid!\n\033[m')

        password_old = getpass('\nEnter your old password: ')

        while self.__hash.cript(password_old) != data['password']:
            print('\n\033[1;31mOld password invalid!\033[m')
            password_old = getpass('\nEnter your old password: ')

        password_new = getpass('\nEnter your new password: ')

        while self.__hash.cript(password_new) == data['password']:
            print(
                '\n\033[1;31mThe new password cannot be the same as the old one!\033[m')
            password_new = getpass('\nEnter your new password: ')

        while password_new == '':
            print('\033[1;31mYou have to write something in your password\033[m')
            password_new = getpass('\nEnter your new password: ')

        password_new_repeat = getpass('Repeat your new password: ')

        while password_new != password_new_repeat:
            print('\n\033[1;31mNew password do not match!\033[m')
            password_new_repeat = getpass('Repeat your new password: ')

        JsonManager().update_json(self.__path_data,
                                  {'username': self.__hash.cript(username),
                                   'password': self.__hash.cript(password_new_repeat),
                                   'code': TOKEN})
        print('\n\033[1;32mUpdate sucess!\033[m')
        self.__timer_clear(2)

    def __recovery_pass(self, data: dict):
        print('\033[1;32m--- Recovery Passowrd ---\033[m')
        print('\033[1;33mForgot password? no problem, '
              'you can recover it by writing the security code here!\033[m')
        recovery = str(input('Enter the code here >> '))
        while self.__hash.cript(recovery) != data["code"]:
            system('cls')
            print('\033[1;31mInvalid code\033[m - '
                  '\033[1;33mif you want to cancel the action type -> 1\033[m')
            recovery = str(input('Enter the code correctly >> '))
            if recovery == 1:
                break

        if self.__hash.cript(recovery) == data["code"]:
            print(
                f'Your password is: {self.__hash.descript(data["password"])}')
            self.__timer_clear(10)

    def sign_in(self) -> None:
        """cadastrar no sistema"""
        print('\033[1;32m--- Sing In ---\033[m')
        while True:
            username = str(input('Enter your username: '))
            confirm_username = str(
                input(f'is this name "{username}" correct? [Y/N]: ')).lower().strip()
            match confirm_username:
                case 'y' | 'yes':
                    break
                case 'n' | 'no' | 'not':
                    print()
                    continue
                case _:
                    print('\033[1;31mOption invalid!\n\033[m')

        password = getpass('\nEnter your password')

        while password == '':
            print('\033[1;31mYou have to write something in your password\033[m')
            password = getpass('\nEnter your new password: ')

        password_verify = getpass('Repeat your password')

        while password != password_verify:
            print('\n\033[1;31mPassword do not match!\033[m')
            password_verify = getpass('Repeat your password')

        TOKEN = self.__hash.generator_token()

        print('\033[1;32mRegistration done!\033[m')
        print(
            f'\033[1;33mRemember, your verification code is: \033[m\033[1;32m{TOKEN}\033[m')
        sleep(15)
        JsonManager().creat_json(self.__path_data,
                                 {"username": self.__hash.cript(username),
                                  "password": self.__hash.cript(password_verify),
                                  "code": self.__hash.cript(TOKEN)})

    def logging_in(self, data: dict) -> None:
        """method para fazer loggin no sistema"""
        print('\033[1;32m--- Logging In ---\033[m')
        username = str(input('Enter your username: '))

        while self.__hash.cript(username) != data['username']:
            print('\n\033[1;31mUsername invalid!\033[m')
            username = str(input('Enter your username: '))

        cont = 0
        password = getpass('Enter your password: ')

        while self.__hash.cript(password) != data['password']:
            print('\n\033[1;31mPassword invalid!\033[m')
            password = getpass('Enter your password: ')
            cont += 1
            if cont >= 5:
                print(
                    '\n\033[1;33mForgot your password and want to recover it? type 1\033[m')
            if password == '1' and cont >= 5:
                self.__timer_clear(2)
                try:
                    self.__recovery_pass(data)
                except KeyboardInterrupt:
                    print('\033[1;31mRecovery canceled\033[m')
                    self.__timer_clear(2)
                print('\n\033[1;32m--- Logging In ---\033[m')

        print('\n\033[1;32mLogging In sucess\033[m')
        self.__timer_clear(2)

        if self.__hash.cript(password) == data['password']:
            self.__home(data)

    def main(self) -> None:
        """Função principal para inciar o processo"""
        while True:
            data = JsonManager().read_json(self.__path_data)
            if data:
                try:
                    self.logging_in(data)
                    break
                except KeyboardInterrupt:
                    print('\n\033[1;31mLogin canceled\033[m')
                    break
            try:
                self.sign_in()
                self.__timer_clear(2)
            except KeyboardInterrupt:
                print('\n\033[1;31mSing In canceled\033[m')
                break


if __name__ == '__main__':
    login = JLogin()
    login.main()
    # z0Au5g
