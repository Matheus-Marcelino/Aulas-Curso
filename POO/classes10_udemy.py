"""
Métodos Mágicos

Métodos Mágicos são todos os métodos que utilizam dunder

dunder init > __init__

dunder repr > representação do objeto
"""

class Livro:
    def __init__(self, titulo: str, autor: str, paginas: int) -> None:
        self.titulo: str = titulo
        self.autor: str = autor
        self.paginas: int = paginas

    def __repr__(self) -> str:  # Sobreescreve a representação
        return f'{self.titulo} escrito por {self.autor}'

    def __str__(self) -> str:  # mesma coisa que o repr, porém o str será executado e o repr não
        return self.titulo

    def __len__(self):  # Você irá definir o len() da sua classe
        return self.paginas  # numero de paginas

    def __del__(self):  # Você pode alterar a lógica, mas nesse caso estou apenas mandando uma mensagem
        print('Um objeto do tipo livro foi deletado da memoria')

    def __add__(self, other):  # Dizendo oque a concatenação irá fazer
        # self - primeiro elemento
        # other - segundo elemento
        return eval(f'{self.paginas} + {other.paginas}')

    def __mul__(self, other):  # permite multiplicação com numeros inteiros
        if isinstance(other, int):  # necessário que faça uma checagem
            return self.paginas * other
        return 'Não posso multiplicar'


if __name__ == '__main__':
    livro = Livro('Amogus', 'Amogus Drip', 57)
    livro2 = Livro('A vida de um chato', 'O chato', 20)
    print(livro)
    print(len(livro))
    print(livro + livro2)  # concatenação
    print(dir(object))

    # está aparecendo a mensagem do del, porque o python apaga todas
    # as variavesi quando o programa termina
