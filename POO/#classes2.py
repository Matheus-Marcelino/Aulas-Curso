# teste com POO - Netflix
class Client():
    def __init__(self, nome: str, email: str, plano: str) -> None:
        self.nome = nome
        self.email = email
        self.list_plano = ('basic', 'premium')
        if plano not in self.list_plano:
            # sempre que for usar uma variavel ->
            # -> declarada ja com 'self.' sempre usará ela com 'self.AlgumaCoisa'
            raise Exception('Plano invalido')
        self.plano = plano

    def mudar_plano(self, novo_plano: str) -> None:
        if novo_plano not in self.list_plano:
            raise Exception('Plano invalido')
        self.plano = novo_plano

    def ver_filme(self, filme: str, plano_filme: str) -> None:
        if self.plano == plano_filme:
            print(f'Ver filme {filme}')
        elif self.plano == 'premium':
            print(f'Ver filme {filme}')
        elif self.plano == 'basic' and plano_filme == 'premium':
            print(
                'NECESSÁRIO PLANO PREMIUM:\n   Faça upgrade no seu plano para poder ver esse filme')
        else:
            print('Plano invalido')


client = Client('Matheus', 'matheus@gmail.com', 'basic')
print(client.nome)
client.ver_filme('Harry Potter', 'premium')

client.mudar_plano('premium')
client.ver_filme('Harry Potter', 'premium')
