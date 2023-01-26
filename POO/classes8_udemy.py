"""
MRO - Method Resolution Order

Method Resolution Order (Resolução de Ordem de Métodos), é a ordem de execução de métodos
que será executado primeiro

Em python, a gente pode conferir a ordem de execução dos métodos (MRO) de 3 formas:
    - Via propriedade da classe __mro__
    - Via método mro()
    - Via help
"""

class Animal:  # mesma coisa que -> Animal(object)
    def __init__(self, nome: str) -> None:
        self.__nome: str = nome

    def cumprimentar(self) -> str:
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)

    def nadar(self) -> str:
        return f'{self._Animal__nome} está nadando'

    def cumprimentar(self) -> str:
        return f'Eu sou {self._Animal__nome} do mar!'


class Terrestre(Animal):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)

    def andar(self) -> str:
        return f'{self._Animal__nome} está andando'

    def cumprimentar(self) -> str:
        return f'Eu sou {self._Animal__nome} da terra!'


class Pinguim(Aquatico, Terrestre):  # altere a ordem e veja a mudança
    def __init__(self, nome: str) -> None:
        super().__init__(nome)


if __name__ == '__main__':
    pinguim = Pinguim('Tux')
    print(pinguim.andar())
    print(pinguim.nadar())
    print(pinguim.cumprimentar())  # Method Resolution Order - MRO

    # print(Pinguim.__mro__)
    # print(Pinguim.mro())
    # print(help(Pinguim))
