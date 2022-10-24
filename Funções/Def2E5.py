def Notas(*notas: float, sit: bool = False) -> dict:
    """
    -> irá mostrar fazer uma ficha com os dados disponiveis
    notas: vai receber todas as suas notas.
    sit: (opcional) irá mostrar a sua sitaução.
    """

    ficha = dict()
    tot = len(notas)
    maior, menor = max(notas), min(notas)
    media = 0

    for nota in notas:
        media += nota
    media /= tot

    ficha['total'] = tot
    ficha['maior'] = maior
    ficha['menor'] = menor
    ficha['media'] = f'{media:.2f}'

    if sit:
        if media < 5:
            ficha['situação'] = 'RUIM'
        elif 5 <= media <= 7:
            ficha['situação'] = 'RAZOAVEL   '
        else:
            ficha['situação'] = 'ÓTIMO'

    return ficha


resposta = Notas(5.5, 2.5, 1.5, sit=False)
print(resposta)
