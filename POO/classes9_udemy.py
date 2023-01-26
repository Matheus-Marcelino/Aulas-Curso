"""
Polimorfismo

Poli -> Muitas
Morfis -> Formas


"""


class Animal:  # mesma coisa que -> Animal(object)
    def __init__(self, nome: str) -> None:
        self.__nome: str = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este método')

    def comer(self):
        print(f'{self.__nome} está comendo')


class Cachorro(Animal):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)

    def falar(self):
        return f'{self._Animal__nome} fala Au Au'


class Gato(Animal):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)

    def falar(self):
        return f'{self._Animal__nome} fala Miau Miau'


class Rato(Animal):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)


if __name__ == '__main__':
    gato = Gato('Amogus')
    print(gato.falar())
    gato.comer()

    pluto = Cachorro('Pluto')
    print(pluto.falar())
    pluto.comer()

    mickey = Rato('Mickey')
    mickey.comer()
    print(mickey.falar())
