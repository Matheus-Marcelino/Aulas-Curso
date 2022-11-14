"""
- Métodos (funções) -> Representam os comportamentos do objeto. as ações que esse objeto pode
realizar no sistema

Tipos de métodos:
    Método de instância
    Método de Classe

O método Dunder init "__init__" é um método especial chamado de construtor e sua função é
construir uma classe

OBS: Todo elemento que inicia e finalizar com " __ " é chamado de Dunder (Doubler Underline)

OBS: Os métodos/ funções dunder em Python são chamados de métodos mágicos

ATENÇÃO: por mais que possamos criar nossas proprias funções utilizando Dunder, não é aconselhavel.
"""


class Lampada():
    def __init__(self, cor: str, voltagem: float, luminosidade: str) -> None:
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrent:
    contador = 4999

    def __init__(self, limite: float, saldo: float) -> None:
        self.__numero = ContaCorrent.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrent.contador = self.__numero


class Produto:
    contador = 0

    def __init__(self, nome: str, descricao: str, valor: float) -> None:
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem: int) -> float:
        return (self.__valor * (100 - porcentagem)) / 100


class Usuario:
    def __init__(self, nome: str, email: str, senha: str) -> None:
        self.__nome = nome
        self.__email = email
        self.__senha = senha

    def __correr__(self, metros) -> None:  # não recomendavel usar Dunder em metodos
        print(f'{self.__nome} está correndo {metros} metros')


produto = Produto('mexirica', 'Consumivel', 20)
print(produto.desconto(50), '\n')

user1 = Usuario('Matheus','Amogus1@gmail.com', '12345')
user2 = Usuario('Reginaldo', 'Amogus2@gmail.com', '54321')
