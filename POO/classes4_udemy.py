"""
Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe,
escondendo atríbuto e métodos privados de usuários

-> Herança

OBS: Qaundo uma classe herda de outra classe ela herda todos os atributos e métodos da classe herdada

Quando a classe herda de outra classe, a classe herdada é conhecida por:
    [Pessoa]
    - Super Classe;
    - Classe Mãe;
    - Classe pai;
    - Classe Base;
    - Classe Genérica;

Quando uma classe herda de outra classe, ela é chamada:
    [Cliente, Funcionario]
    - Sub Filha;
    - Classe Filha;
    - Classe Especifica;

Overriding (Sobre Escrita de Método)

Sobre Escrita de Método, Ocorre quando reescrevemos um método presente na
super classe em classe filhas



"""


class Pessoa:
    def __init__(self, nome: str, sobrenome: str, cpf: str) -> None:
        self.__nome: str = nome
        self.__sobrenome: str = sobrenome
        self.__cpf: str = cpf

    def nome_completo(self) -> str:
        return f'{self.__nome} {self.__sobrenome}'


# Cliente Herda de Pessoa
class Cliente(Pessoa):  # A super classe de Cliente é Pessoa
    def __init__(self, nome: str, sobrenome: str, cpf: str, renda: float) -> None:
        Pessoa.__init__(self, nome, sobrenome, cpf,)  # forma incomum de acsessar dados da super classe
        self.__renda: float = renda


# Cliente Herda de Pessoa
class Funcionario(Pessoa):
    def __init__(self, nome: str, sobrenome: str, cpf: str, matricula: int) -> None:
        super().__init__(nome, sobrenome, cpf,)  # forma comum de acessar dados da super classe
        self.__matricula: int = matricula

    def nome_completo(self) -> str:
        print(super().nome_completo())
        print(self._Pessoa__cpf)
        return f'Funcionario: {self.__matricula} nome: {self._Pessoa__nome}'


cliente = Cliente('Angelina', 'Jolie', '123.456.789-09', 5000)
funcionario_1 = Funcionario('Amogus', 'Drip', '098.765.432-12', 1234)

print(cliente.nome_completo())
print(funcionario_1.nome_completo())
