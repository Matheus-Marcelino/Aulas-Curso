"""
O método super()

O método super() se refere a super classe e pode acessar qualquer elemento da classe pai
"""

class Animal:
    def __init__(self, nome: str, especie: str) -> None:
        self.__nome: str = nome
        self.__especie: str = especie

    def faz_som(self, som: str) -> None:
        print(f'O {self.__nome} fala {som}')


class Cachorro(Animal):
    def __init__(self, nome: str, especie: str, raca: str) -> None:
        super().__init__(nome, especie)
        self.raca: str = raca


class Gato(Animal):
    def __init__(self, nome: str, especie: str, raca: str) -> None:
        super().__init__(nome, especie)
        self.raca: str = raca


if __name__ == '__main__':
    gato = Gato('Niko', 'Felino', 'Angorá')
    cachorro = Cachorro('Amogus', 'Mamifero', 'Husky siberiano')

    cachorro.faz_som('AuAuAuAu')
    gato.faz_som('Miau Miau')
