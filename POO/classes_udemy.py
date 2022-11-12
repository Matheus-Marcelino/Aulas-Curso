"""
Programação Orientada a Objetos - POO

- POO é um paradigma de programação que utiliza que mapeamento
de objetos do mundo real para modelos computacionais

- Paradigama de programação é a forma/metodologia utilizada para
pensar/desenvolver sistemas.

Principais elementos da POO
- Classe -> Modelo do objeto do mundo real sendo representado computacionalmente;
- Atributo -> Caracteristicas do objeto.
- Metodo -> Comportamento do objeto (funções).
- Construtor -> Metodo especial utilizado para criar os objetos
- Objetos -> Instância da classe
"""

# Atributos
# em python por convenção, todo atributo de uma classe é publico
# para deixar um atributo privado coloca-se ' __ ' no começo do atributo -- __var


class Lampada:
    def __init__(self, voltagem: float, cor: str | None) -> None:
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrent:
    def __init__(self, numero: float, limite: float, saldo: float) -> None:
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Usuario:
    def __init__(self, nome: str, email: str, senha: str) -> None:
        self.nome = nome
        self.email = email
        self.senha = senha


class Acesso:
    def __init__(self, email: str, senha: str) -> None:
        self.email = email
        self.__senha = senha

    def mostra_senha(self) -> None:
        print(self.__senha)

    def mostra_email(self) -> None:
        print(self.email)


# é apenas uma convenção, ou seja, a linguagem não vai impedir
# que façamos acesso sinalizado como privados fora da classe

user = Acesso('Amogus@gmail.com', '123456')
print(user.email)
# print(user.__senha) --  da um erro
# print(dir(user))
# temos acesso, mas não deveriamos ter o acesso (Name Mangling)
print(user._Acesso__senha)
user.mostra_senha()
user.mostra_email()
print('\n')

# Atributos de instancia
# Significa, que ao criarmos instancia/objetos de uma classe, todas as instancias
# terão estes atributos

user1 = Acesso('Amogus1@gmail.com', '12345')
user2 = Acesso('Amogus2@gmail.com', '54321')
user1.mostra_email()
user2.mostra_email()
print('\n')

# Cada um deles terão um valor diferente


class Produto:
    # atributo de classe
    imposto = 1.05  # 0.05% de imposto

    # o primeiro parametro n precisa se chamar self, mas por convenção é ' self '
    def __init__(salsicha, nome: str, descricao: str, valor: float) -> None:
        salsicha.nome = nome
        salsicha.descricao = descricao
        salsicha.valor = (valor * Produto.imposto)


p1 = Produto('PlayStation 5', 'Video game', 4.556)
p2 = Produto('Xbox S', 'Video game', 3856.87)

print(p1.imposto)  # acesso possivel, mas incorreto de um atributo de classe

print(p1.valor)
print(p2.valor)

# não precisamos criar uma instancia de uma classe para fazer acesso a um atributo de classe

print(Produto.imposto)
