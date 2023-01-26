from string import ascii_lowercase, ascii_uppercase, punctuation, digits
from os import path
from random import choice


class Hash():
    """Uma classe que serve para criptografias"""

    def __init__(self, complexidade: int) -> None:
        self.__root = path.dirname(path.realpath(__file__))
        self.__LETTERS = ' AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
        self.complexidade = complexidade

    def generator_token(self) -> str:
        token = ''.join(choice(ascii_lowercase + ascii_uppercase + digits)
                        for _ in range(self.complexidade))
        return token

    def save_path_creator(self) -> None:
        """Cria o arquivo com a criptografia própria"""
        def auxiliar() -> None:
            with open(f'{self.__root}\coden\key.txt', 'w+', encoding='utf-8') as file:
                file.write(f'complexidade={self.complexidade}\n')
                for digito in digits:
                    file.write(f'{digito}={self.generator_token()}\n')
                for letra in self.__LETTERS:
                    file.write(f'{letra}={self.generator_token()}\n')
                for symbol in punctuation:
                    file.write(f'{symbol}={self.generator_token()}\n')

        def conjunto() -> None:
            file.seek(0, 0)
            file.write(f'complexidade={self.complexidade}\n')
            for digito in digits:
                file.write(f'{digito}={self.generator_token()}\n')
            for letra in self.__LETTERS:
                file.write(f'{letra}={self.generator_token()}\n')
            for symbol in punctuation:
                file.write(f'{symbol}={self.generator_token()}\n')

        if not path.exists('key.txt'):
            auxiliar()
        else:
            try:
                with open(f'{self.__root}\coden\key.txt', 'r+', encoding='utf-8') as file:
                    try:
                        temp = file.readline()[13:]
                        file.truncate(0)
                        self.complexidade = int(temp)
                        if self.complexidade <= 2:
                            self.complexidade = 5
                        conjunto()
                    except ValueError:
                        self.complexidade = self.complexidade
                        conjunto()
            except FileNotFoundError:
                auxiliar()

    def cript(self, text: str) -> str:
        """Criptografa qualquer texto"""
        separador = []
        criptografado = ''

        def main() -> str:
            nonlocal criptografado
            with open(f'{self.__root}\coden\key.txt', 'r', encoding='utf-8') as file:
                for letra in text:
                    analisador = len(file.readline()[13:]) - 1
                    file.seek(13+analisador, 0)
                    for cripto in file:
                        validacao = letra in cripto[:1]
                        if validacao:
                            separador.append(cripto[2:self.complexidade+2])
                            criptografado = ''.join(separador)
                            break
                return criptografado

        try:
            return main()
        except FileNotFoundError:
            self.save_path_creator()
            return main()

    def descript(self, text: str) -> str:
        """Descriptografa o um texto criptografado com a sua key"""
        text = text.strip()
        agrupador = []
        separador = descriptografado = ''
        mem, mem2 = 0, self.complexidade
        # {mem, mem2} usado para avançar pela criptografia no tamanho da complexidade

        def main():
            nonlocal mem, mem2, separador, descriptografado
            with open(f'{self.__root}\coden\key.txt', 'r', encoding='utf-8') as file:
                while True:
                    file.seek(0)
                    separador = text[mem:mem2]
                    mem += self.complexidade
                    mem2 += self.complexidade
                    if separador != '':
                        for cripto in file:
                            validacao = separador in cripto[2:]
                            if validacao:
                                agrupador.append(cripto[:1])
                                descriptografado = ''.join(agrupador)
                                break
                    else:
                        break
                return descriptografado

        try:
            return main()
        except FileNotFoundError:
            self.save_path_creator()
            return main()


if __name__ == '__main__':
    hash = Hash(6)
    #hash.save_path_creator()
    print(hash.cript('Amogus'))
