"""
Herança Multipla

Herança Multipla é a possibilidade de umka classe herdar de multiplas classes
fazendo com que  aclasse filha herde todos os atributos e métodos  de todas as
classes herdadas.

OBS: A Herança Multipla pode ser feita de duas maneiras:
       - por multiderivação direta:
       - por multiderivação indireta:


# Multiderivação Direta

class Base1:
    pass


class Base2:
    pass



class Base3:
    pass


class MultiDerivada(Base1, Base2, Base3):
    pass


# Multiderivação Indireta


class Base1:
    pass


class Base2(Base1):
    pass



class Base3(Base2):
    pass


class MultiDerivada(Base3):
    pass


OBS: Não importa se a Derivação é direta ou indireta. A classe que realizará a herança herdará
todos os atributo e métodos das super classes
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


class Pinguim(Terrestre, Aquatico):  # altere a ordem e veja a mudança
    def __init__(self, nome: str) -> None:
        super().__init__(nome)


if __name__ == '__main__':
    baleia = Aquatico('Wally')
    print(baleia.nadar())
    print(baleia.cumprimentar())

    tatu = Terrestre('Xim')
    print(tatu.andar())
    print(tatu.cumprimentar())

    pinguim = Pinguim('Tux')
    print(pinguim.andar())
    print(pinguim.nadar())
    print(pinguim.cumprimentar())  # Method Resolution Order - MRO
    print(pinguim.__dir__())
    # Objeto é instancia de ...
    print(f'pinguim é instancia de Pinguim? {isinstance(pinguim, Pinguim)}')  # True
    print(f'pinguim é instancia de Terrestre? {isinstance(pinguim, Terrestre)}')  # True
    print(f'pinguim é instancia de Aquatico? {isinstance(pinguim, Aquatico)}')  # True
    print(f'pinguim é instancia de Animal? {isinstance(pinguim, Animal)}')  # True
    print(f'pinguim é instancia de obeject? {isinstance(pinguim, object)}')  # True
