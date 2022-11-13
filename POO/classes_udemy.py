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
    # o primeiro parametro n precisa se chamar self, mas por convenção é ' self '
    def __init__(salsicha, nome: str, email: str, senha: str) -> None:
        salsicha.nome = nome
        salsicha.email = email
        salsicha.senha = senha


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
    contador = 0

    def __init__(self, nome: str, descricao: str, valor: float) -> None:
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


'''
-- primeira parte 

p1 = Produto('PlayStation 5', 'Video game', 4.556)
p2 = Produto('Xbox S', 'Video game', 3856.87)

print(p1.imposto)  # acesso possivel, mas incorreto de um atributo de classe

print(p1.valor)
print(p2.valor)

# não precisamos criar uma instancia de uma classe para fazer acesso a um atributo de classe

print(Produto.imposto, '\n')

print(p1.id)  # toda vez que a classe for chamada o id dela irá aumentar
print(p2.id)  # atributos de classe == atributos estáticos:
'''


# Atributos Dinamicos -> Um atributo de instancia que pode ser criado em tempo de execução
# O atributo dinamico será exclusivo da instancia quer o criou

p1 = Produto('PlayStation 5', 'Video game', 4.556)
p2 = Produto('Arroz', 'Alimento', 3856.87)

p2.peso = '5kg'  # não existe o atributo peso na classe Produto

print(
    f'Produto: {p2.nome},\nDescrição: {p2.descricao}\nValor: {p2.valor}\nPeso: {p2.peso}')

# print(f'Produto: {p1.nome},\nDescrição: {p1.descricao}\nValor: {p1.valor}\nPeso: {p1.peso}')
# -- irá dar um erro pois o atributo dinamico do p1 n foi criado

print(p2.__dict__)  # informações do produtos 2
# print(Produto.__dict__)
del p2.peso  # irá apagar o atributo peso
