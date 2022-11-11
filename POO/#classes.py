# Nomes de classes são em CamelCase -- Pep8
class ControleRemoto:
    # Sempre criar a função init no começo

    def __init__(self, valor_da_cor, altura, profundidade, largura) -> None:
        # ' self ' faz referencia a classe em si

        # Especificar as caracteristicas no __init__
        self.cor = valor_da_cor
        # mesmo que o parametro seja diferente o self.cor será reconhecido no pela classe
        # como uma variavel global dentro da classe ->
        # -> (Precisando do self. para ser reconhecido e tendo o valor alterado)

        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura
        # colocar self nas variaveis para que a classe possa reconhecer como um atributo dela

    # metodos da classe controle remoto
    def passar_canal(self, botao: str) -> None:
        if botao == '+':
            print('Aumentar o canal')
        elif botao == '-':
            print('Diminuir o canal')


controle_remoto = ControleRemoto("Azul", "10cm", "2cm", "3cm")
controle_remoto2 = ControleRemoto("Preto", "10cm", "2cm", "3cm")
# mesmo q um mude o outro não vai mudar

print(controle_remoto.cor)
print(controle_remoto2.cor)
controle_remoto.passar_canal('-')

# Continua -> no '#classes.py'
