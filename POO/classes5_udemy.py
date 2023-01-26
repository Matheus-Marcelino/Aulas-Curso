"""Propriedades

Ao declarar atributos privados nas classes, costuma-se criar métodos para
manipulação desses atributos, nos quais são chamados de getters e setters

-> getters: retornam valor dos atributos
-> setters: alteram o valor do mesmo

forma de se fazer em outros linguagens

    def get_titular(self) -> str:
        return self.__titular

    def get_saldo(self) -> float:
        return self.__saldo

    def get_limite(self) -> None:
        return self.__limite

    def set_titular(self, titular: str) -> None:
        self.__titular = titular
    
    def set_saldo(self, saldo: float) -> None:
        self.__saldo = saldo


"""


class Conta:
    contador: int = 0

    def __init__(self, titular: str, saldo: float, limite: float) -> None:
        self.__numero: int = Conta.contador
        self.__titular: str = titular
        self.__saldo: float = saldo
        self.__limite: float = limite
        Conta.contador += 1

    @property  # declarando uma propriedade da classe
    def numero(self) -> int:
        return self.__numero

    @property
    def titular(self) -> str:
        return self.__titular

    @property
    def saldo(self) -> float:
        return self.__saldo

    @property
    def limite(self) -> float:
        return self.__limite

    @limite.setter
    def limite(self, limite: float) -> None:
        self.__limite = limite

    def extrato(self) -> str:
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor: float) -> None:
        self.__saldo += valor

    def sacar(self, valor: float) -> None:
        self.__saldo -= valor

    def transferir(self, valor: float, destino) -> None:
        self.__saldo -= valor
        destino.__saldo += valor


if __name__ == '__main__':
    conta1 = Conta('Amogus', 3000, 5000)
    conta2 = Conta('Felicity', 2000, 4000)

    soma: float = conta1.saldo + conta2.saldo  # por causa do decorator o acesso sem parenteses é permitido

    print(f'A soma do saldo das duas contas é: {soma}\n')

    print(conta1.__dict__)
    conta1.limite = 465364  # usando como propriedade
    print(conta1.__dict__)
    print(conta1.limite)
