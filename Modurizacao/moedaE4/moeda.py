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


def resumo(valor: int, acrescimo: int, reducao: int) -> None:
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'Preço analisado: {moeda(valor):>6}')
    print(f'Dobro do preço: {dobro(valor):>6}')
    print(f'Metade do preço: {metade(valor):>6}')
    print(f'{acrescimo}% de aumento: {aumentar(valor, acrescimo):>6}')
    print(f'{reducao}% de reducao: {diminuir(valor, reducao):>6}')
    print('-' * 30)
