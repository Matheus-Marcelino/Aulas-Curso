def moeda(preco: float, ident: str = 'R$') -> str:
    return f'{ident}{preco:.2f}'.replace('.', ',')


def aumentar(preco: float, taxa: float = 1, ident: str = 'R$') -> str:
    return moeda(preco + (preco * taxa/100), ident)


def diminuir(preco: float, taxa: float = 1, ident: str = 'R$') -> str:
    return moeda(preco - (preco * taxa/100), ident)


def dobro(preco: float, ident: str = 'R$') -> str:
    return moeda(preco * 2, ident)


def metade(preco: float, ident: str = 'R$') -> str:
    return moeda(preco / 2, ident)


def resumo(valor: int, acrescimo: int=10, reducao: int=5) -> None:
    print('-' * 50)
    print('RESUMO DO VALOR'.center(50))  # centraliza a string
    print('-' * 50)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor)}')
    print(f'Metade do preço: \t{metade(valor)}')
    print(f'{acrescimo}% de aumento: \t{aumentar(valor, acrescimo)}')
    print(f'{reducao}% de reducao: \t{diminuir(valor, reducao)}')
    print('-' * 50)
