def aumentar(preco: float, taxa: float = 1) -> float:
    return preco + (preco * taxa/100)


def diminuir(preco: float, taxa: float = 1) -> float:
    return preco - (preco * taxa/100)


def dobro(preco: float) -> float:
    return preco * 2


def metade(preco: float) -> float:
    return preco / 2


def moeda(preco: float, ident: str = 'R$') -> str:
    return f'{ident}{preco}'.replace('.', ',')
