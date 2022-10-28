from exercicio5.utilidadescev.moeda import resumo


def leiaDinheiro(valor: str) -> None:
    while True:
        print(f'ERRO: "{valor}" é um preço invalido!')
        valor = str(input('Digite o preço: R$'))
        valor = valor.replace(',', '.')
        try:
            float(valor)
            break
        except ValueError:
            pass

    resumo(float(valor))
