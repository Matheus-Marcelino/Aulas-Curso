def Notas(*notas: float, sit: bool = False) -> dict:
    """
    -> irá mostrar fazer uma ficha com os dados disponiveis
    notas: vai receber todas as suas notas.
    sit: (opcional) irá mostrar a sua sitaução.
    """

    ficha = dict()
    tot = len(notas)
    maior, menor = max(notas), min(notas)
    media = sum(notas) / tot
    # sum() função para somar os numeros da tupla
    ficha['total'] = tot
    ficha['maior'] = maior
    ficha['menor'] = menor
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
