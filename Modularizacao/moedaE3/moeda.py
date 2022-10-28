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
