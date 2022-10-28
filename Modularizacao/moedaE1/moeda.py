def aumentar(preco: float, taxa: float) -> float:
    return preco + (preco * taxa/100)


def diminuir(preco: float, taxa: float) -> float:
    return preco - (preco * taxa/100)


def dobro(preco: float) -> float:
    return preco * 2


def metade(preco: float) -> float:
    return preco / 2
