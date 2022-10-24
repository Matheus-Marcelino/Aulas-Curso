def Notas(*notas: float, sit: bool = False) -> dict:
    """
    -> irá mostrar fazer uma ficha com os dados disponiveis
    notas: vai receber todas as suas notas.
    sit: (opcional) irá mostrar a sua sitaução.
    """

    ficha = dict()
    media = sum(notas) / len(notas)
    # sum() função para somar os numeros da tupla
    ficha['total'] = len(notas)
    ficha['maior'] = max(notas)
    ficha['menor'] = min(notas)
    ficha['media'] = f'{media:.2f}'

    if sit:
        if media < 5:
            ficha['situação'] = 'RUIM'
        elif 5 <= media <= 7:
            ficha['situação'] = 'RAZOAVEL'
        else:
            ficha['situação'] = 'ÓTIMO'

    return ficha


resposta = Notas(5.5, 2.5, 1.5)
print(resposta)
print('-=' * 40)
resposta = Notas(5.6, 7.5, 3.5, sit=True)
print(resposta)
