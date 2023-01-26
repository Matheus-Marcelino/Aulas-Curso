"""
-> Cria-se métodos de instância para fazer acesso a atributos de instância

-> métodos de classe não acessam atributos de instância
|
|--> Quando o método não faz nenhum acesso a um atributo de instância, ele pode ser método de classe

métodos de classe são conhecidos como métodos estáticos em outras linguagens

-> Método estático não se tem acesso a classe e nem a estância
"""
from passlib.hash import pbkdf2_sha256 as cryp
from passlib.hash import md5_crypt

class Usuario:
    contador = 0

    @classmethod
    def conta_usuario(cls):  # -> cls == classe em si
        print(f'Temos {cls.contador} usuários no sistema')

    @classmethod
    def ver(cls):
        print('Teste')

    @staticmethod
    def definicao():  # não recebe nada por padrão
        return 'UXR344'

    def __init__(self, nome: str, email: str, senha: str) -> None:
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuario criado: {self.__gera_user()}')

    def pass_verify(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_user(self):  # método privado
        return self.__email.split('@')[0]

    # def ver(self):
    #    print('Teste')

# métodos de classe

# Usuario.conta_usuario()  # acessando o metodo de classe de forma correta
# user.conta_usuario()  # forma incorreta de acessar o metodo de classe
# print(user._Usuario__gera_user())  # acessando um método privado, forma ruim


# métodos estáticos
print(Usuario.contador)  # 0 porque ainda não tem instanciado nenhum usuario
print(Usuario.definicao())

user = Usuario('Matheus', 'matheus@gmail.com', '123456')
print(user.contador)  # 1 porque instanbciou um usuario
print(user.definicao())
